from . import _init_ctre

# autogenerated by 'robotpy-build create-imports ctre'
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
    MotorCommutation,
    MovingAverage,
    NeutralMode,
    Orchestra,
    ParamEnum,
    RemoteFeedbackDevice,
    RemoteLimitSwitchSource,
    RemoteSensorSource,
    SensorCollection,
    SensorTerm,
    SetValueMotionProfile,
    SlotConfigUtil,
    SlotConfiguration,
    StatorCurrentLimitConfiguration,
    StatusFrame,
    StatusFrameEnhanced,
    StatusFrameRoutines,
    StickyFaults,
    SupplyCurrentLimitConfiguration,
    TalonFX,
    TalonFXConfigUtil,
    TalonFXConfiguration,
    TalonFXControlMode,
    TalonFXFeedbackDevice,
    TalonFXInvertType,
    TalonFXPIDSetConfiguration,
    TalonFXSensorCollection,
    TalonFXSimCollection,
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
    WPI_TalonFX,
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
    "MotorCommutation",
    "MovingAverage",
    "NeutralMode",
    "Orchestra",
    "ParamEnum",
    "RemoteFeedbackDevice",
    "RemoteLimitSwitchSource",
    "RemoteSensorSource",
    "SensorCollection",
    "SensorTerm",
    "SetValueMotionProfile",
    "SlotConfigUtil",
    "SlotConfiguration",
    "StatorCurrentLimitConfiguration",
    "StatusFrame",
    "StatusFrameEnhanced",
    "StatusFrameRoutines",
    "StickyFaults",
    "SupplyCurrentLimitConfiguration",
    "TalonFX",
    "TalonFXConfigUtil",
    "TalonFXConfiguration",
    "TalonFXControlMode",
    "TalonFXFeedbackDevice",
    "TalonFXInvertType",
    "TalonFXPIDSetConfiguration",
    "TalonFXSensorCollection",
    "TalonFXSimCollection",
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
    "WPI_TalonFX",
    "WPI_TalonSRX",
    "WPI_VictorSPX",
]


from .version import version as __version__


# backwards compat
# TODO: remove in 2024
def __getattr__(name):
    if name != "sensors":
        from .sensors import __all__

        if name in __all__:
            import warnings
            from . import sensors

            message = f"{__name__}.{name} has moved to {__name__}.sensors"
            warnings.warn(message, FutureWarning, stacklevel=2)
            return getattr(sensors, name)

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
