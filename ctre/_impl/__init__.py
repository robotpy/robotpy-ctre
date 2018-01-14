import hal
from collections import namedtuple
from .faults import Faults
from .stickyfaults import StickyFaults
from .canifierfaults import CANifierFaults
from .canifierstickyfaults import CANifierStickyFaults
from .pigeonfaults import PigeonIMU_Faults
from .pigeonstickyfaults import PigeonIMU_StickyFaults
from .motionprofilestatus import MotionProfileStatus

if hal.isSimulation():
    from .autogen.canifier_sim import CANifier
    from .autogen.motcontroller_sim import MotController
    from .autogen.pigeonimu_sim import PigeonIMU
    from .autogen.ctre_sim_enums import (
        ControlMode,
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
        GeneralPin,
        PigeonIMU_StatusFrame,
        PigeonIMU_ControlFrame,
        TrajectoryDuration,
    )
else:
    from .ctre_roborio import (
        CANifier,
        MotController,
        PigeonIMU
    )
    from .ctre_roborio import (
        ControlMode,
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
        GeneralPin,
        PigeonIMU_StatusFrame,
        PigeonIMU_ControlFrame,
        TrajectoryDuration,
    )
