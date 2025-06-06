from . import _init_phoenix6
from . import _init__ctre


from .version import version as __version__

# autogenerated by 'semiwrap create-imports phoenix5 phoenix5._ctre'
from ._ctre import (
    BaseMotorController,
    BaseMotorControllerConfiguration,
    BaseMotorControllerUtil,
    BasePIDSetConfiguration,
    BaseTalon,
    BaseTalonConfigUtil,
    BaseTalonConfiguration,
    BaseTalonPIDSetConfigUtil,
    BaseTalonPIDSetConfiguration,
    BufferedTrajectoryPointStream,
    CANBusAddressable,
    CANifier,
    CANifierConfigUtils,
    CANifierConfiguration,
    CANifierControlFrame,
    CANifierFaults,
    CANifierStatusFrame,
    CANifierStickyFaults,
    CANifierVelocityMeasPeriod,
    ControlFrame,
    ControlFrameEnhanced,
    ControlMode,
    CustomParamConfigUtil,
    CustomParamConfiguration,
    DemandType,
    ErrorCode,
    Faults,
    FeedbackDevice,
    FilterConfigUtil,
    FilterConfiguration,
    FollowerType,
    IFollower,
    IGadgeteerUartClient,
    IInvertable,
    ILoopable,
    IMotorController,
    IMotorControllerEnhanced,
    IOutputSignal,
    IProcessable,
    InvertType,
    LimitSwitchNormal,
    LimitSwitchRoutines,
    LimitSwitchSource,
    MotionProfileStatus,
    MovingAverage,
    NeutralMode,
    ParamEnum,
    RemoteFeedbackDevice,
    RemoteLimitSwitchSource,
    RemoteSensorSource,
    SensorCollection,
    SensorTerm,
    SetValueMotionProfile,
    SlotConfigUtil,
    SlotConfiguration,
    StatusFrame,
    StatusFrameEnhanced,
    StatusFrameRoutines,
    StickyFaults,
    SupplyCurrentLimitConfiguration,
    TalonSRX,
    TalonSRXConfigUtil,
    TalonSRXConfiguration,
    TalonSRXControlMode,
    TalonSRXFeedbackDevice,
    TalonSRXPIDSetConfiguration,
    TalonSRXSimCollection,
    TrajectoryPoint,
    Unmanaged,
    VelocityMeasPeriod,
    VictorConfigUtil,
    VictorSPX,
    VictorSPXConfiguration,
    VictorSPXControlMode,
    VictorSPXPIDSetConfigUtil,
    VictorSPXPIDSetConfiguration,
    VictorSPXSimCollection,
    WPI_BaseMotorController,
    WPI_TalonSRX,
    WPI_VictorSPX,
)

__all__ = [
    "BaseMotorController",
    "BaseMotorControllerConfiguration",
    "BaseMotorControllerUtil",
    "BasePIDSetConfiguration",
    "BaseTalon",
    "BaseTalonConfigUtil",
    "BaseTalonConfiguration",
    "BaseTalonPIDSetConfigUtil",
    "BaseTalonPIDSetConfiguration",
    "BufferedTrajectoryPointStream",
    "CANBusAddressable",
    "CANifier",
    "CANifierConfigUtils",
    "CANifierConfiguration",
    "CANifierControlFrame",
    "CANifierFaults",
    "CANifierStatusFrame",
    "CANifierStickyFaults",
    "CANifierVelocityMeasPeriod",
    "ControlFrame",
    "ControlFrameEnhanced",
    "ControlMode",
    "CustomParamConfigUtil",
    "CustomParamConfiguration",
    "DemandType",
    "ErrorCode",
    "Faults",
    "FeedbackDevice",
    "FilterConfigUtil",
    "FilterConfiguration",
    "FollowerType",
    "IFollower",
    "IGadgeteerUartClient",
    "IInvertable",
    "ILoopable",
    "IMotorController",
    "IMotorControllerEnhanced",
    "IOutputSignal",
    "IProcessable",
    "InvertType",
    "LimitSwitchNormal",
    "LimitSwitchRoutines",
    "LimitSwitchSource",
    "MotionProfileStatus",
    "MovingAverage",
    "NeutralMode",
    "ParamEnum",
    "RemoteFeedbackDevice",
    "RemoteLimitSwitchSource",
    "RemoteSensorSource",
    "SensorCollection",
    "SensorTerm",
    "SetValueMotionProfile",
    "SlotConfigUtil",
    "SlotConfiguration",
    "StatusFrame",
    "StatusFrameEnhanced",
    "StatusFrameRoutines",
    "StickyFaults",
    "SupplyCurrentLimitConfiguration",
    "TalonSRX",
    "TalonSRXConfigUtil",
    "TalonSRXConfiguration",
    "TalonSRXControlMode",
    "TalonSRXFeedbackDevice",
    "TalonSRXPIDSetConfiguration",
    "TalonSRXSimCollection",
    "TrajectoryPoint",
    "Unmanaged",
    "VelocityMeasPeriod",
    "VictorConfigUtil",
    "VictorSPX",
    "VictorSPXConfiguration",
    "VictorSPXControlMode",
    "VictorSPXPIDSetConfigUtil",
    "VictorSPXPIDSetConfiguration",
    "VictorSPXSimCollection",
    "WPI_BaseMotorController",
    "WPI_TalonSRX",
    "WPI_VictorSPX",
]
