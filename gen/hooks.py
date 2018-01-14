
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

def _gen_check(pname, ptype):

    # TODO: This does checks on normal types, but if you pass a ctypes value
    #       in then this does not check those properly.

    if ptype == 'bool':
        return 'isinstance(%s, bool)' % pname

    elif ptype in ['float', 'double']:
        return 'isinstance(%s, (int, float))' % pname

    #elif ptype is C.c_char:
    #    return 'isinstance(%s, bytes) and len(%s) == 1' % (pname, pname)
    #elif ptype is C.c_wchar:
    #    return 'isinstance(%s, str) and len(%s) == 1' % (pname, pname)
    #elif ptype is C.c_char_p:
    #    return "%s is None or isinstance(%s, bytes) or getattr(%s, '_type_') is _C.c_char" % (pname, pname, pname)
    #elif ptype is C.c_wchar_p:
    #    return '%s is None or isinstance(%s, bytes)' % (pname, pname)

    elif ptype in ['int', 'long']:
        return 'isinstance(%s, int)' % pname
    #elif ptype in [C.c_byte, C.c_int8]:
    #    return 'isinstance(%s, int) and %s < %d and %s > -%d' % (pname, pname, 1<<7, pname, 1<<7)
    elif ptype in ['short', 'int16_t']:
        return 'isinstance(%s, int) and %s < %d and %s > -%d' % (pname, pname, 1<<15, pname, 1<<15)
    elif ptype == 'int32_t':
        return 'isinstance(%s, int) and %s < %d and %s > -%d' % (pname, pname, 1<<31, pname, 1<<31)
    elif ptype == 'int64_t':
        return 'isinstance(%s, int) and %s < %d and %s > -%d' % (pname, pname, 1<<63, pname, 1<<63)

    elif ptype == 'size_t':
        return 'isinstance(%s, int)' % (pname)
    elif ptype == 'uint8_t':
        return 'isinstance(%s, int) and %s < %d and %s >= 0' % (pname, pname, 1<<8, pname)
    elif ptype == 'uint16_t':
        return 'isinstance(%s, int) and %s < %d and %s >= 0' % (pname, pname, 1<<16, pname)
    elif ptype == 'uint32_t':
        return 'isinstance(%s, int) and %s < %d and %s >= 0' % (pname, pname, 1<<32, pname)
    elif ptype == 'uint64_t':
        return 'isinstance(%s, int) and %s < %d and %s >= 0' % (pname, pname, 1<<64, pname)

    elif ptype is None:
        return '%s is None' % pname

    else:
        # TODO: do validation here
        #return 'isinstance(%s, %s)' % (pname, type(ptype).__name__)
        return None


def _to_annotation(ctypename):
    return _annotations[ctypename]

def header_hook(header, data):
    '''Called for each header'''

    # fix enum names
    for e in header.enums:
        ename = e['name'].split('_')[0] + '_'
        for v in e['values']:
            name = v['name']
            if name.startswith(ename):
                name = name[len(ename):]
            if name == 'None':
                name = 'NONE'
            v['x_name'] = name

def function_hook(fn, data):
    '''Called for each function in the header'''

    # only output functions if a module name is defined
    if 'module_name' not in data:
        return

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

    x_param_checks = []

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
            chk = _gen_check(p['name'], p['raw_type'])
            if chk:
                x_param_checks.append('assert %s' % chk)
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

            x_pyann_ret = 'typing.Tuple[%s, %s]'
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
    if data is None:
        # ensure every function is in our yaml
        print('WARNING', fn['name'])
        data = {}
        #assert False, fn['name']

    # lazy :)
    fn.update(locals())
