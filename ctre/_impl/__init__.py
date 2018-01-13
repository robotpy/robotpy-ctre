import hal
from collections import namedtuple
from .faults import Faults
from .stickyfaults import StickyFaults
from .canifierfaults import CANifierFaults
from .canifierstickyfaults import CANifierStickyFaults
from .pigeonfaults import PigeonIMU_Faults
from .pigeonstickyfaults import PigeonIMU_StickyFaults
from .trajectorypoint import TrajectoryPoint
from .motionprofilestatus import MotionProfileStatus

if hal.isSimulation():
    from .autogen.canifier_sim import CANifier
    from .autogen.motcontroller_sim import MotController
    from .autogen.pigeonimu_sim import PigeonIMU
    from .autogen.ctre_sim_enums import (
        ErrorCode,
        NeutralMode,
        RemoteFeedbackDevice,
        FeedbackDevice,
        StatusFrame,
        StatusFrameEnhanced,
        VelocityMeasPeriod,
        RemoteLimitSwitchSource,
        LimitSwitchNormal,
        LimitSwitchSource,
        ParamEnum,
        CANifierStatusFrame,
        CANifierControlFrame,
        ParamEnum,
        PigeonIMU_StatusFrame,
        PigeonIMU_ControlFrame,
    )
else:
    from .ctre_roborio import (
        CANifier,
        MotController,
        PigeonIMU
    )
    from .ctre_roborio import (
        ErrorCode,
        NeutralMode,
        RemoteFeedbackDevice,
        FeedbackDevice,
        StatusFrame,
        StatusFrameEnhanced,
        VelocityMeasPeriod,
        RemoteLimitSwitchSource,
        LimitSwitchNormal,
        LimitSwitchSource,
        ParamEnum,
        CANifierStatusFrame,
        CANifierControlFrame,
        ParamEnum,
        PigeonIMU_StatusFrame,
        PigeonIMU_ControlFrame,
    )


# todo: eliminate
import enum
from unittest.mock import MagicMock

class ControlMode (enum.IntEnum):
    PercentOutput = 0
    Position = 1
    Velocity = 2
    Current = 3
    Follower = 5
    MotionProfile = 6
    MotionMagic = 7
    MotionMagicArc = 8
    #TimedPercentOutput = 9
    MotionProfileArc = 10
    Disabled = 15


GeneralPin = MagicMock()
