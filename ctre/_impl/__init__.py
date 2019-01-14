import hal

from .autogen.faults import (
    CANifierFaults,
    CANifierStickyFaults,
    Faults,
    StickyFaults,
    PigeonIMU_Faults,
    PigeonIMU_StickyFaults,
)
from .motionprofilestatus import MotionProfileStatus

if hal.isSimulation():
    from .autogen.bufftrajpointstream_sim import BuffTrajPointStream
    from .autogen.canifier_sim import CANifier
    from .autogen.motcontroller_sim import MotController
    from .autogen.pigeonimu_sim import PigeonIMU
    from .autogen import ctre_sim_enums as _enum_module
else:
    from .ctre_roborio import BuffTrajPointStream, CANifier, MotController, PigeonIMU
    from . import ctre_roborio as _enum_module

# enums
ControlMode = _enum_module.ControlMode
DemandType = _enum_module.DemandType
ErrorCode = _enum_module.ErrorCode
NeutralMode = _enum_module.NeutralMode
RemoteFeedbackDevice = _enum_module.RemoteFeedbackDevice
RemoteSensorSource = _enum_module.RemoteSensorSource
FeedbackDevice = _enum_module.FeedbackDevice
FollowerType = _enum_module.FollowerType
InvertType = _enum_module.InvertType
SetValueMotionProfile = _enum_module.SetValueMotionProfile
StatusFrame = _enum_module.StatusFrame
StatusFrameEnhanced = _enum_module.StatusFrameEnhanced
VelocityMeasPeriod = _enum_module.VelocityMeasPeriod
RemoteLimitSwitchSource = _enum_module.RemoteLimitSwitchSource
LimitSwitchNormal = _enum_module.LimitSwitchNormal
LimitSwitchSource = _enum_module.LimitSwitchSource
ParamEnum = _enum_module.ParamEnum
CANifierStatusFrame = _enum_module.CANifierStatusFrame
CANifierControlFrame = _enum_module.CANifierControlFrame
GeneralPin = _enum_module.GeneralPin
PigeonIMU_StatusFrame = _enum_module.PigeonIMU_StatusFrame
PigeonIMU_ControlFrame = _enum_module.PigeonIMU_ControlFrame

del _enum_module
