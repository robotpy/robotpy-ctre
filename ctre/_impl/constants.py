
class TalonSRXConst:
    kDefaultControlPeriodMs = 10

    # mode select enumerations
    kMode_DutyCycle = 0
    kMode_PositionCloseLoop = 1
    kMode_VelocityCloseLoop = 2
    kMode_CurrentCloseLoop = 3
    kMode_VoltCompen = 4
    kMode_SlaveFollower = 5
    kMode_MotionProfile = 6
    kMode_NoDrive = 15

    # limit switch enumerations
    kLimitSwitchOverride_UseDefaultsFromFlash = 1
    kLimitSwitchOverride_DisableFwd_DisableRev = 4
    kLimitSwitchOverride_DisableFwd_EnableRev = 5
    kLimitSwitchOverride_EnableFwd_DisableRev = 6
    kLimitSwitchOverride_EnableFwd_EnableRev = 7

    # brake override enumerations
    kBrakeOverride_UseDefaultsFromFlash = 0
    kBrakeOverride_OverrideCoast = 1
    kBrakeOverride_OverrideBrake = 2

    # feedback device enumerations
    kFeedbackDev_DigitalQuadEnc = 0
    kFeedbackDev_AnalogPot = 2
    kFeedbackDev_AnalogEncoder = 3
    kFeedbackDev_CountEveryRisingEdge = 4
    kFeedbackDev_CountEveryFallingEdge = 5
    kFeedbackDev_CtreMagEncoder_Relative = 6
    kFeedbackDev_CtreMagEncoder_Absolute = 7
    kFeedbackDev_PosIsPulseWidth = 8
    
    # feedback device status enumerations
    kFeedbackDevStatus_Unknown = 0
    kFeedbackDevStatus_Present = 1
    kFeedbackDevStatus_NotPresent = 2

    # ProfileSlotSelect enumerations
    kProfileSlotSelect_Slot0 = 0
    kProfileSlotSelect_Slot1 = 1

    # status frame rate types
    kStatusFrame_General = 0
    kStatusFrame_Feedback = 1
    kStatusFrame_Encoder = 2
    kStatusFrame_AnalogTempVbat = 3
    kStatusFrame_PulseWidth = 4
    kStatusFrame_MotionProfile = 5
    
    # Motion Profile status bits
    kMotionProfileFlag_ActTraj_IsValid = 0x1
    kMotionProfileFlag_HasUnderrun = 0x2
    kMotionProfileFlag_IsUnderrun = 0x4
    kMotionProfileFlag_ActTraj_IsLast = 0x8
    kMotionProfileFlag_ActTraj_VelOnly = 0x10
    
    # Motor output is neutral, Motion Profile Executer is not running.
    kMotionProfile_Disable = 0
    # Motor output is updated from Motion Profile Executer, MPE will
    # process the buffered points.
    kMotionProfile_Enable = 1
    # Motor output is updated from Motion Profile Executer, MPE will
    # stay processing current trajectory point.
    kMotionProfile_Hold = 2
