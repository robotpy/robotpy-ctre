
from .wpi_talonsrx import WPI_TalonSRX
from .wpi_victorspx import WPI_VictorSPX
from .canifier import CANifier
from .pigeonimu import PigeonIMU

try:
    from .version import __version__
except ImportError:     # pragma: nocover
    __version__ = 'master'
