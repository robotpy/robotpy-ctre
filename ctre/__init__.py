from .talonsrx import TalonSRX
from .victorspx import VictorSPX
from .wpi_talonsrx import WPI_TalonSRX
from .wpi_victorspx import WPI_VictorSPX
from .canifier import CANifier
from .pigeonimu import PigeonIMU

from ._impl import (
    ControlMode,
    ParamEnum,
    ErrorCode,
    FeedbackDevice,
    RemoteFeedbackDevice,
    RemoteSensorSource,
    LimitSwitchSource,
    LimitSwitchNormal,
    NeutralMode,
)

from .trajectorypoint import TrajectoryPoint

try:
    from .version import __version__
except ImportError:     # pragma: nocover
    __version__ = 'master'
