
import re

_annotations = {
    'short': int,
    'int': 'int',
    'uint32_t': 'int',
    'double': 'float',
    'char': 'str',
    'bool': 'bool',
    'ctre::phoenix::ErrorCode': 'int',
}

def _to_annotation(ctypename):
    return _annotations[ctypename]


def function_hook(fn, data):
    '''Called for each function in the header'''

    # Mangle the name appropriately
    m = re.match(r'c_%s_(.*)' % data['module_name'], fn['name'])
    if not m:
        raise Exception("Unexpected fn %s" % fn['name'])

    x_name = m.group(1)
    x_name = x_name[0].lower() + x_name[1:]

    # Setup the data for wrapping the CCI interface

    returns = fn['returns']

    x_in_params = []
    x_out_params = []

    # returns can be an out param
    # -> but in a check, it's not

    # final_out is really what we want?

    # parameter names, types

    # inner call

    # return

    x_ret_names = []
    x_ret_types = []

    param_offset = 0 if x_name.startswith('create') else 1

    for i, p in enumerate(fn['parameters'][param_offset:]):
        if p['name'] == '':
            p['name'] = 'param%s' % i
        p['x_type'] = p['raw_type']
        p['x_callname'] = p['name']

        # Python annotations for sim
        p['x_pyann_type'] = _to_annotation(p['raw_type'])
        p['x_pyann'] = '%(name)s: %(x_pyann_type)s' % p

        if p['pointer']:
            p['x_callname'] = '&%(x_callname)s' % p
            x_out_params.append(p)
        elif p['array']:
            asz = p.get('array_size', 0)
            if asz:
                p['x_pyann_type'] = 'list'
                p['x_type'] = 'std::array<%s, %s>' % (p['x_type'], asz)
                p['x_callname'] = '%(x_callname)s.data()' % p
            else:
                # it's a vector
                pass

            x_out_params.append(p)
        else:
            x_in_params.append(p)


        p['x_decl'] = '%s %s' % (p['x_type'], p['name'])

    # if there are out params, then change returns to be a tuple
    if x_out_params:
        p = ', '.join([p['x_type'] for p in x_out_params])
        returns = 'std::tuple<%s, %s>' % (fn['returns'], p)

    x_callend = ''
    x_return = ''

    if returns == 'void':
        x_callstart = ''
        x_pyann_ret = 'None'
    else:
        #if returns == 'ctre::phoenix::ErrorCode':
        #    x_callstart = 'auto __ret = CheckCTRCode('
        #    x_callend = ')'
        #else:

        # TODO: should we throw on a CTRE error? Their Java APIs don't,
        #       so we probably shouldn't either
        x_callstart = 'auto __ret = '

        if x_out_params:
            x_return = 'return std::make_tuple(__ret, %s);'
            x_return %= ', '.join([p['name'] for p in x_out_params])

            x_pyann_ret = 'typing.Tuple(%s, %s)'
            x_pyann_ret %= (_to_annotation(fn['returns']),
                            ', '.join([p['x_pyann_type'] for p in x_out_params]))
        else:
            x_return = 'return __ret;'
            x_pyann_ret = _to_annotation(returns)

    # Temporary values to store out parameters in
    x_temprefs = ''
    if x_out_params:
        x_temprefs = \
            ';'.join([
                '%(x_type)s %(name)s' % p for p in x_out_params
            ]) + ';'

    py_self_comma = ', ' if x_in_params else ''

    # x_call_params

    data = data.get('data', {}).get(fn['name'])

    # lazy :)
    fn.update(locals())
