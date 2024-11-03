# Hack to get around needing to depend on phoenix 6's binaries and
# they aren't exported directly


from os.path import abspath, join, dirname
import phoenix6

_root = abspath(dirname(phoenix6.__file__))

libinit_import = "phoenix5._init_phoenix6"
depends = []
pypi_package = "phoenix6"


def get_include_dirs():
    return []


def get_library_dirs():
    return [join(_root, "lib")]


def get_library_dirs_rel():
    return ["lib"]


def get_library_names():
    return [
        "CTRE_PhoenixTools_Sim",
        "CTRE_SimCANCoder",
        "CTRE_SimPigeonIMU",
        "CTRE_SimProCANcoder",
        "CTRE_SimProPigeon2",
        "CTRE_SimProTalonFX",
        "CTRE_SimTalonSRX",
        "CTRE_SimVictorSPX",
    ]


def get_library_full_names():
    return [
        "libCTRE_PhoenixTools_Sim.dylib",
        "libCTRE_SimCANCoder.dylib",
        "libCTRE_SimPigeonIMU.dylib",
        "libCTRE_SimProCANcoder.dylib",
        "libCTRE_SimProPigeon2.dylib",
        "libCTRE_SimProTalonFX.dylib",
        "libCTRE_SimTalonSRX.dylib",
        "libCTRE_SimVictorSPX.dylib",
    ]
