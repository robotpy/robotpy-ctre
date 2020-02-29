import sys

from . import _init_ctre

# autogenerated by 'robotpy-build create-imports ctre ctre._ctre'
from ._ctre import (
    AbsoluteSensorRange,
    AbsoluteSensorRangeRoutines,
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
    CANCoder,
    CANCoderConfigUtils,
    CANCoderConfiguration,
    CANCoderFaults,
    CANCoderStatusFrame,
    CANCoderStickyFaults,
    CANifier,
    CANifierConfigUtils,
    CANifierConfiguration,
    CANifierControlFrame,
    CANifierFaults,
    CANifierStatusFrame,
    CANifierStickyFaults,
    CANifierVelocityMeasPeriod,
    CANifierVelocityMeasPeriodRoutines,
    ControlFrame,
    ControlFrameEnhanced,
    ControlFrameRoutines,
    ControlMode,
    CustomParamConfigUtil,
    CustomParamConfiguration,
    DemandType,
    ErrorCode,
    Faults,
    FeedbackDevice,
    FeedbackDeviceRoutines,
    FilterConfigUtil,
    FilterConfiguration,
    FollowerType,
    IFollower,
    IMotorController,
    IMotorControllerEnhanced,
    InvertType,
    LimitSwitchNormal,
    LimitSwitchRoutines,
    LimitSwitchSource,
    MagnetFieldStrength,
    MotionProfileStatus,
    MotorCommutation,
    NeutralMode,
    Orchestra,
    ParamEnum,
    PigeonIMU,
    PigeonIMUConfigUtils,
    PigeonIMUConfiguration,
    PigeonIMU_ControlFrame,
    PigeonIMU_Faults,
    PigeonIMU_StatusFrame,
    PigeonIMU_StickyFaults,
    RemoteFeedbackDevice,
    RemoteLimitSwitchSource,
    RemoteSensorSource,
    RemoteSensorSourceRoutines,
    SensorCollection,
    SensorInitializationStrategy,
    SensorInitializationStrategyRoutines,
    SensorTerm,
    SensorTermRoutines,
    SensorTimeBase,
    SensorTimeBaseRoutines,
    SensorVelocityMeasPeriod,
    SensorVelocityMeasPeriodRoutines,
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
    TalonSRX,
    TalonSRXConfigUtil,
    TalonSRXConfiguration,
    TalonSRXFeedbackDevice,
    TalonSRXPIDSetConfiguration,
    TrajectoryPoint,
    VelocityMeasPeriod,
    VelocityMeasPeriodRoutines,
    VictorConfigUtil,
    VictorSPX,
    VictorSPXConfiguration,
    VictorSPXPIDSetConfigUtil,
    VictorSPXPIDSetConfiguration,
    WPI_BaseMotorController,
    WPI_TalonFX,
    WPI_TalonSRX,
    WPI_VictorSPX,
)

__all__ = [
    "AbsoluteSensorRange",
    "AbsoluteSensorRangeRoutines",
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
    "CANCoder",
    "CANCoderConfigUtils",
    "CANCoderConfiguration",
    "CANCoderFaults",
    "CANCoderStatusFrame",
    "CANCoderStickyFaults",
    "CANifier",
    "CANifierConfigUtils",
    "CANifierConfiguration",
    "CANifierControlFrame",
    "CANifierFaults",
    "CANifierStatusFrame",
    "CANifierStickyFaults",
    "CANifierVelocityMeasPeriod",
    "CANifierVelocityMeasPeriodRoutines",
    "ControlFrame",
    "ControlFrameEnhanced",
    "ControlFrameRoutines",
    "ControlMode",
    "CustomParamConfigUtil",
    "CustomParamConfiguration",
    "DemandType",
    "ErrorCode",
    "Faults",
    "FeedbackDevice",
    "FeedbackDeviceRoutines",
    "FilterConfigUtil",
    "FilterConfiguration",
    "FollowerType",
    "IFollower",
    "IMotorController",
    "IMotorControllerEnhanced",
    "InvertType",
    "LimitSwitchNormal",
    "LimitSwitchRoutines",
    "LimitSwitchSource",
    "MagnetFieldStrength",
    "MotionProfileStatus",
    "MotorCommutation",
    "NeutralMode",
    "Orchestra",
    "ParamEnum",
    "PigeonIMU",
    "PigeonIMUConfigUtils",
    "PigeonIMUConfiguration",
    "PigeonIMU_ControlFrame",
    "PigeonIMU_Faults",
    "PigeonIMU_StatusFrame",
    "PigeonIMU_StickyFaults",
    "RemoteFeedbackDevice",
    "RemoteLimitSwitchSource",
    "RemoteSensorSource",
    "RemoteSensorSourceRoutines",
    "SensorCollection",
    "SensorInitializationStrategy",
    "SensorInitializationStrategyRoutines",
    "SensorTerm",
    "SensorTermRoutines",
    "SensorTimeBase",
    "SensorTimeBaseRoutines",
    "SensorVelocityMeasPeriod",
    "SensorVelocityMeasPeriodRoutines",
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
    "TalonSRX",
    "TalonSRXConfigUtil",
    "TalonSRXConfiguration",
    "TalonSRXFeedbackDevice",
    "TalonSRXPIDSetConfiguration",
    "TrajectoryPoint",
    "VelocityMeasPeriod",
    "VelocityMeasPeriodRoutines",
    "VictorConfigUtil",
    "VictorSPX",
    "VictorSPXConfiguration",
    "VictorSPXPIDSetConfigUtil",
    "VictorSPXPIDSetConfiguration",
    "WPI_BaseMotorController",
    "WPI_TalonFX",
    "WPI_TalonSRX",
    "WPI_VictorSPX",
]

from .version import version as __version__

from ._ctre import platform
sys.modules["ctre.platform"] = platform
