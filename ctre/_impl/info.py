
class Info:
    
    def module_info(self):
        from .. import version
        return 'CTRE bindings', version.__version__, version.__ctre_version__
    