
from .wpi_talonsrx import WPI_TalonSRX
from .wpi_victorspx import WPI_VictorSPX
from .canifier import CANifier
from .pigeonimu import PigeonIMU

from ._impl import (
    ControlMode,
    ErrorCode,
    FeedbackDevice,
    RemoteFeedbackDevice,
    NeutralMode,
)

from .trajectorypoint import TrajectoryPoint

try:
    from .version import __version__
except ImportError:     # pragma: nocover
    __version__ = 'master'
