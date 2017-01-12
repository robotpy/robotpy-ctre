
from .constants import TalonSRXConst
from enum import Enum

from hal_impl.data import hal_data, NotifyDict

__all__ = ['CTR_Code', 'CanTalonSRX']

class CTR_Code(Enum):
    CTR_OKAY = 0
    CTR_RxTimeout = 1
    CTR_TxTimeout = 2
    CTR_InvalidParamValue = 3
    CTR_UnexpectedArbId = 4
    CTR_TxFailed = 5
    CTR_SigNotUpdated = 6
    CTR_BufferFull = 7

class CanTalonSRX:
    '''
        Simulation implementation for CANTalon
    '''
    
    class param_t(Enum):
        # Signal enumeration for generic signal access
        eProfileParamSlot0_P = 1
        eProfileParamSlot0_I = 2
        eProfileParamSlot0_D = 3
        eProfileParamSlot0_F = 4
        eProfileParamSlot0_IZone = 5
        eProfileParamSlot0_CloseLoopRampRate = 6
        eProfileParamSlot1_P = 11
        eProfileParamSlot1_I = 12
        eProfileParamSlot1_D = 13
        eProfileParamSlot1_F = 14
        eProfileParamSlot1_IZone = 15
        eProfileParamSlot1_CloseLoopRampRate = 16
        eProfileParamSoftLimitForThreshold = 21
        eProfileParamSoftLimitRevThreshold = 22
        eProfileParamSoftLimitForEnable = 23
        eProfileParamSoftLimitRevEnable = 24
        eOnBoot_BrakeMode = 31
        eOnBoot_LimitSwitch_Forward_NormallyClosed = 32
        eOnBoot_LimitSwitch_Reverse_NormallyClosed = 33
        eOnBoot_LimitSwitch_Forward_Disable = 34
        eOnBoot_LimitSwitch_Reverse_Disable = 35
        eFault_OverTemp = 41
        eFault_UnderVoltage = 42
        eFault_ForLim = 43
        eFault_RevLim = 44
        eFault_HardwareFailure = 45
        eFault_ForSoftLim = 46
        eFault_RevSoftLim = 47
        eStckyFault_OverTemp = 48
        eStckyFault_UnderVoltage = 49
        eStckyFault_ForLim = 50
        eStckyFault_RevLim = 51
        eStckyFault_ForSoftLim = 52
        eStckyFault_RevSoftLim = 53
        eAppliedThrottle = 61
        eCloseLoopErr = 62
        eFeedbackDeviceSelect = 63
        eRevMotDuringCloseLoopEn = 64
        eModeSelect = 65
        eProfileSlotSelect = 66
        eRampThrottle = 67
        eRevFeedbackSensor = 68
        eLimitSwitchEn = 69
        eLimitSwitchClosedFor = 70
        eLimitSwitchClosedRev = 71
        eSensorPosition = 73
        eSensorVelocity = 74
        eCurrent = 75
        eBrakeIsEnabled = 76
        eEncPosition = 77
        eEncVel = 78
        eEncIndexRiseEvents = 79
        eQuadApin = 80
        eQuadBpin = 81
        eQuadIdxpin = 82
        eAnalogInWithOv = 83
        eAnalogInVel = 84
        eTemp = 85
        eBatteryV = 86
        eResetCount = 87
        eResetFlags = 88
        eFirmVers = 89
        eSettingsChanged = 90
        eQuadFilterEn = 91
        ePidIaccum = 93
        eStatus1FrameRate = 94  # TALON_Status_1_General_10ms_t
        eStatus2FrameRate = 95  # TALON_Status_2_Feedback_20ms_t
        eStatus3FrameRate = 96  # TALON_Status_3_Enc_100ms_t
        eStatus4FrameRate = 97  # TALON_Status_4_AinTempVbat_100ms_t
        eStatus6FrameRate = 98  # TALON_Status_6_Eol_t
        eStatus7FrameRate = 99  # TALON_Status_7_Debug_200ms_t
        eClearPositionOnIdx = 100
        # reserved
        # reserved
        # reserved
        ePeakPosOutput = 104
        eNominalPosOutput = 105
        ePeakNegOutput = 106
        eNominalNegOutput = 107
        eQuadIdxPolarity = 108
        eStatus8FrameRate = 109  # TALON_Status_8_PulseWid_100ms_t
        eAllowPosOverflow = 110
        eProfileParamSlot0_AllowableClosedLoopErr = 111
        eNumberPotTurns = 112
        eNumberEncoderCPR = 113
        ePwdPosition = 114
        eAinPosition = 115
        eProfileParamVcompRate = 116
        eProfileParamSlot1_AllowableClosedLoopErr = 117
        eStatus9FrameRate = 118  # TALON_Status_9_MotProfBuffer_100ms_t
        eMotionProfileHasUnderrunErr = 119
        eReserved120 = 120
        eLegacyControlMode = 121
    
    def __init__(self, deviceNumber, controlPeriodMs, enablePeriodMs):
        
        assert deviceNumber not in hal_data['CAN']
        
        self.deviceNumber = deviceNumber
        
        # Initialize items based on their param type
        hal_data['CAN'][deviceNumber] = NotifyDict({
            v: 0 for v in _srx_param_map.values()
        })
        
        self.hal_data = hal_data['CAN'][deviceNumber]
        
        # Initialize non-zero items or items that don't have an associated parameter
        self.hal_data.update({
            'type': 'talonsrx',
            
            'override_limit_switch': 0,
            'override_braketype': None,
            
            'pulse_width_velocity': 0,
            'pulse_width_present': 0,
            
            'voltage_compensation_rate': 0,
            
            'battery': 12.0,
            
            # Motion profile stuff
            'mp_position': 0,
            'mp_velocity': 0,
            'mp_timeDurMs': 0,
            'mp_profileSlotSelect': 0,
            
            'mp_flags': 0,
            'mp_topBufferCnt': 0,
            'mp_btmBufferCnt': 0,
            'mp_topBufferRem': 0,
            'mp_zeroPos': 0,
            'mp_outputEnable': TalonSRXConst.kMotionProfile_Disable
        })
        
    def Destroy(self):
        del hal_data['CAN'][self.deviceNumber]
        del self.hal_data
        
    def Set(self, value):
        self.hal_data['value'] = int(value*1023)

    def SetParam(self, paramEnum, value):
        self.hal_data[_srx_param_map[paramEnum]] = value

    def RequestParam(self, paramEnum):
        return self.hal_data[_srx_param_map[paramEnum]]

    def GetParamResponse(self, paramEnum):
        return self.hal_data[_srx_param_map[paramEnum]]

    def GetParamResponseInt32(self, paramEnum):
        return int(self.hal_data[_srx_param_map[paramEnum]])

    def SetPgain(self, slotIdx, gain):
        if slotIdx == 0:
            self.hal_data['profile0_p'] = gain
        else:
            self.hal_data['profile1_p'] = gain

    def SetIgain(self, slotIdx, gain):
        if slotIdx == 0:
            self.hal_data['profile0_i'] = gain
        else:
            self.hal_data['profile1_i'] = gain

    def SetDgain(self, slotIdx, gain):
        if slotIdx == 0:
            self.hal_data['profile0_d'] = gain
        else:
            self.hal_data['profile1_d'] = gain

    def SetFgain(self, slotIdx, gain):
        if slotIdx == 0:
            self.hal_data['profile0_f'] = gain
        else:
            self.hal_data['profile1_f'] = gain

    def SetIzone(self, slotIdx, zone):
        if slotIdx == 0:
            self.hal_data['profile0_izone'] = zone
        else:
            self.hal_data['profile1_izone'] = zone

    def SetCloseLoopRampRate(self, slotIdx, closeLoopRampRate):
        if slotIdx == 0:
            self.hal_data['profile0_closeloopramprate'] = closeLoopRampRate
        else:
            self.hal_data['profile1_closeloopramprate'] = closeLoopRampRate

    def SetVoltageCompensationRate(self, voltagePerMs):
        self.hal_data['voltage_compensation_rate'] = voltagePerMs

    def SetSensorPosition(self, pos):
        data = self.hal_data
        device_type = data['feedback_device']
        data[_srx_pos_map[device_type]] = pos

    def SetForwardSoftLimit(self, forwardLimit):
        self.hal_data['soft_limit_for'] = forwardLimit 

    def SetReverseSoftLimit(self, reverseLimit):
        self.hal_data['soft_limit_rev'] = reverseLimit

    def SetForwardSoftEnable(self, enable):
        self.hal_data['soft_limit_for_enable'] = enable

    def SetReverseSoftEnable(self, enable):
        self.hal_data['soft_limit_rev_enable'] = enable

    def GetPgain(self, slotIdx):
        if slotIdx == 0:
            return self.hal_data['profile0_p']
        else:
            return self.hal_data['profile1_p']

    def GetIgain(self, slotIdx):
        if slotIdx == 0:
            return self.hal_data['profile0_i']
        else:
            return self.hal_data['profile1_i']

    def GetDgain(self, slotIdx):
        if slotIdx == 0:
            return self.hal_data['profile0_d']
        else:
            return self.hal_data['profile1_d']

    def GetFgain(self, slotIdx):
        if slotIdx == 0:
            return self.hal_data['profile0_f']
        else:
            return self.hal_data['profile1_f']

    def GetIzone(self, slotIdx):
        if slotIdx == 0:
            return self.hal_data['profile0_izone']
        else:
            return self.hal_data['profile1_izone']

    def GetCloseLoopRampRate(self, slotIdx):
        if slotIdx == 0:
            return self.hal_data['profile0_closeloopramprate']
        else:
            return self.hal_data['profile1_closeloopramprate']

    def GetVoltageCompensationRate(self):
        return self.hal_data['voltage_compensation_rate']

    def GetForwardSoftLimit(self):
        return self.hal_data['soft_limit_for']

    def GetReverseSoftLimit(self):
        return self.hal_data['soft_limit_rev']

    def GetForwardSoftEnable(self):
        return self.hal_data['soft_limit_for_enable']

    def GetReverseSoftEnable(self):
        return self.hal_data['soft_limit_rev_enable']

    def GetPulseWidthRiseToFallUs(self):
        assert False

    def IsPulseWidthSensorPresent(self):
        return self.hal_data['pulse_width_present']

    def SetStatusFrameRate(self, frameEnum, periodMs):
        pass

    def ClearStickyFaults(self):
        self.hal_data['sticky_overtemp'] = 0
        self.hal_data['stickyfault_undervoltage'] = 0
        self.hal_data['stickyfault_forlim'] = 0
        self.hal_data['stickyfault_revlim'] = 0
        self.hal_data['stickyfault_forsoftlim'] = 0
        self.hal_data['stickyfault_revsoftlim'] = 0
        
    def ChangeMotionControlFramePeriod(self, periodMs):
        pass

    def ClearMotionProfileTrajectories(self):
        pass

    def GetMotionProfileTopLevelBufferCount(self):
        return self.hal_data['mp_topBufferCnt']

    def IsMotionProfileTopLevelBufferFull(self):
        return False

    _push_mp_mask = ~(TalonSRXConst.kMotionProfileFlag_ActTraj_VelOnly | \
                      TalonSRXConst.kMotionProfileFlag_ActTraj_IsLast)

    def PushMotionProfileTrajectory(self, targPos, targVel, profileSlotSelect, timeDurMs, velOnly, isLastPoint, zeroPos):
        data = self.hal_data
        data['mp_position'] = targPos
        data['mp_velocity'] = targVel
        data['mp_profileSlotSelect'] = profileSlotSelect
        data['mp_timeDurMs'] = timeDurMs
        data['mp_zeroPos'] = zeroPos
        
        flags = data['mp_flags']
        flags &= self._push_mp_mask
        
        if velOnly:
            flags |= TalonSRXConst.kMotionProfileFlag_ActTraj_VelOnly
            
        if isLastPoint:
            flags |= TalonSRXConst.kMotionProfileFlag_ActTraj_IsLast

    def ProcessMotionProfileBuffer(self):
        pass

    def GetMotionProfileStatus(self):
        data = self.hal_data
        
        return (data['mp_flags'],
                data['mp_profileSlotSelect'],
                data['mp_position'],
                data['mp_velocity'],
                data['mp_topBufferRem'],
                data['mp_topBufferCnt'],
                data['mp_btmBufferCnt'],
                data['mp_outputEnable'])

    def GetFault_OverTemp(self):
        return self.hal_data['fault_overtemp']

    def GetFault_UnderVoltage(self):
        return self.hal_data['fault_undervoltage']

    def GetFault_ForLim(self):
        return self.hal_data['fault_forlim']

    def GetFault_RevLim(self):
        return self.hal_data['fault_revlim']

    def GetFault_HardwareFailure(self):
        return self.hal_data['fault_hwfailure']

    def GetFault_ForSoftLim(self):
        return self.hal_data['fault_forsoftlim']

    def GetFault_RevSoftLim(self):
        return self.hal_data['fault_revsoftlim']

    def GetStckyFault_OverTemp(self):
        return self.hal_data['stickyfault_overtemp']

    def GetStckyFault_UnderVoltage(self):
        return self.hal_data['stickyfault_undervoltage']

    def GetStckyFault_ForLim(self):
        return self.hal_data['stickyfault_forlim']

    def GetStckyFault_RevLim(self):
        return self.hal_data['stickyfault_revlim']

    def GetStckyFault_ForSoftLim(self):
        return self.hal_data['stickyfault_forsoftlim']

    def GetStckyFault_RevSoftLim(self):
        return self.hal_data['stickyfault_revsoftlim']

    def GetAppliedThrottle(self):
        return self.hal_data['value']

    def GetCloseLoopErr(self):
        return self.hal_data['closeloop_err']

    def GetFeedbackDeviceSelect(self):
        return self.hal_data['feedback_device']

    def GetModeSelect(self):
        return self.hal_data['mode_select']

    def GetLimitSwitchEn(self):
        return self.hal_data['limit_switch_en']

    def GetLimitSwitchClosedFor(self):
        return self.hal_data['limit_switch_closed_for']

    def GetLimitSwitchClosedRev(self):
        return self.hal_data['limit_switch_closed_rev']

    def GetSensorPosition(self):
        # this returns different values depending on the feedback device selected
        data = self.hal_data
        device_type = data['feedback_device']
        return data[_srx_pos_map[device_type]]

    def GetSensorVelocity(self):
        # this returns different values depending on the feedback device selected
        data = self.hal_data
        device_type = data['feedback_device']
        return data[_srx_vel_map[device_type]]

    def GetCurrent(self):
        return self.hal_data['current']

    def GetBrakeIsEnabled(self):
        return self.hal_data['brake_enabled']

    def GetEncPosition(self):
        return self.hal_data['enc_position']

    def GetEncVel(self):
        return self.hal_data['enc_velocity']

    def GetEncIndexRiseEvents(self):
        return self.hal_data['enc_index_rise_events']

    def GetQuadApin(self):
        return self.hal_data['quad_apin']

    def GetQuadBpin(self):
        return self.hal_data['quad_bpin']

    def GetQuadIdxpin(self):
        return self.hal_data['quad_idxpin']

    def GetAnalogInWithOv(self):
        return self.hal_data['analog_in_position']

    def GetAnalogInVel(self):
        return self.hal_data['analog_in_velocity']

    def GetTemp(self):
        return self.hal_data['temp']

    def GetBatteryV(self):
        return self.hal_data['battery']

    def GetResetCount(self):
        return self.hal_data['reset_count']

    def GetResetFlags(self):
        return self.hal_data['reset_flags']

    def GetFirmVers(self):
        return self.hal_data['firmware_version']

    def GetPulseWidthPosition(self):
        return self.hal_data['pulse_width_position']

    def GetPulseWidthVelocity(self):
        return self.hal_data['pulse_width_velocity']

    def GetPulseWidthRiseToRiseUs(self):
        assert False

    def GetActTraj_IsValid(self):
        flags = self.hal_data['mp_flags']
        return (flags & TalonSRXConst.kMotionProfileFlag_ActTraj_IsValid) != 0
        
    def GetActTraj_ProfileSlotSelect(self):
        return self.hal_data['mp_profileSlotSelect']

    def GetActTraj_VelOnly(self):
        flags = self.hal_data['mp_flags']
        return (flags & TalonSRXConst.kMotionProfileFlag_ActTraj_VelOnly) != 0

    def GetActTraj_IsLast(self):
        flags = self.hal_data['mp_flags']
        return (flags & TalonSRXConst.kMotionProfileFlag_ActTraj_IsLast) != 0

    def GetOutputType(self):
        assert False

    def GetHasUnderrun(self):
        flags = self.hal_data['mp_flags']
        return (flags & TalonSRXConst.kMotionProfileFlag_HasUnderrun) != 0

    def GetIsUnderrun(self):
        flags = self.hal_data['mp_flags']
        return (flags & TalonSRXConst.kMotionProfileFlag_IsUnderrun) != 0

    def GetNextID(self):
        assert False

    def GetBufferIsFull(self):
        assert False

    def GetCount(self):
        assert False

    def GetActTraj_Velocity(self):
        return self.hal_data['mp_velocity']

    def GetActTraj_Position(self):
        return self.hal_data['mp_position']

    def SetDemand(self, param):
        self.hal_data['value'] = param

    def SetOverrideLimitSwitchEn(self, param):
        self.hal_data['override_limit_switch'] = param

    def SetFeedbackDeviceSelect(self, param):
        self.hal_data['feedback_device'] = param

    def SetRevMotDuringCloseLoopEn(self, param):
        self.hal_data['rev_motor_during_close_loop'] = param

    def SetOverrideBrakeType(self, param):
        self.hal_data['override_braketype'] = param

    def SetModeSelect(self, param):
        self.hal_data['mode_select'] = param

    def SetModeSelect2(self, modeSelect, demand):
        self.hal_data['mode_select'] = modeSelect
        self.hal_data['value'] = demand

    def SetProfileSlotSelect(self, param):
        self.hal_data['profile_slot_select'] = param

    def SetRampThrottle(self, param):
        self.hal_data['ramp_throttle'] = param

    def SetRevFeedbackSensor(self, param):
        self.hal_data['rev_feedback_sensor'] = param



#############################################################################
# TalonSRX
#############################################################################

def __create_srx_param_map():
    '''Defines the mappings between CANTalon dict items and raw parameter types'''
    param_t = CanTalonSRX.param_t
    return {
        param_t.eProfileParamSlot0_P :                    'profile0_p',
        param_t.eProfileParamSlot0_I :                    'profile0_i',
        param_t.eProfileParamSlot0_D :                    'profile0_d',
        param_t.eProfileParamSlot0_F :                    'profile0_f',
        param_t.eProfileParamSlot0_IZone :                'profile0_izone',
        param_t.eProfileParamSlot0_CloseLoopRampRate :    'profile0_closeloopramprate',
        param_t.eProfileParamSlot1_P :                    'profile1_p',
        param_t.eProfileParamSlot1_I :                    'profile1_i',
        param_t.eProfileParamSlot1_D :                    'profile1_d',
        param_t.eProfileParamSlot1_F :                    'profile1_f',
        param_t.eProfileParamSlot1_IZone :                'profile1_izone',
        param_t.eProfileParamSlot1_CloseLoopRampRate :    'profile1_closeloopramprate',
        param_t.eProfileParamSoftLimitForThreshold :      'soft_limit_for',
        param_t.eProfileParamSoftLimitRevThreshold :      'soft_limit_rev',
        param_t.eProfileParamSoftLimitForEnable :         'soft_limit_for_enable',
        param_t.eProfileParamSoftLimitRevEnable :         'soft_limit_rev_enable',
        param_t.eOnBoot_BrakeMode :                        'onboot_brake_mode',
        param_t.eOnBoot_LimitSwitch_Forward_NormallyClosed : 'onboot_limsw_for_normally_closed',
        param_t.eOnBoot_LimitSwitch_Reverse_NormallyClosed : 'onboot_limsw_rev_normally_closed',
        param_t.eOnBoot_LimitSwitch_Forward_Disable :     'onboot_limsw_for_disable',
        param_t.eOnBoot_LimitSwitch_Reverse_Disable :     'onboot_limsw_rev_disable',
        param_t.eFault_OverTemp :                         'fault_overtemp',
        param_t.eFault_UnderVoltage :                     'fault_undervoltage',
        param_t.eFault_ForLim :                           'fault_forlim',
        param_t.eFault_RevLim :                           'fault_revlim',
        param_t.eFault_HardwareFailure :                  'fault_hwfailure',
        param_t.eFault_ForSoftLim :                       'fault_forsoftlim',
        param_t.eFault_RevSoftLim :                       'fault_revsoftlim',
        param_t.eStckyFault_OverTemp :                    'stickyfault_overtemp',
        param_t.eStckyFault_UnderVoltage :                'stickyfault_undervoltage',
        param_t.eStckyFault_ForLim :                      'stickyfault_forlim',
        param_t.eStckyFault_RevLim :                      'stickyfault_revlim',
        param_t.eStckyFault_ForSoftLim :                  'stickyfault_forsoftlim',
        param_t.eStckyFault_RevSoftLim :                  'stickyfault_revsoftlim',
        param_t.eAppliedThrottle :                        'value',
        param_t.eCloseLoopErr :                           'closeloop_err',
        param_t.eFeedbackDeviceSelect :                   'feedback_device',
        param_t.eRevMotDuringCloseLoopEn :                'rev_motor_during_close_loop',
        param_t.eModeSelect :                             'mode_select',
        param_t.eProfileSlotSelect :                      'profile_slot_select',
        param_t.eRampThrottle :                           'ramp_throttle',
        param_t.eRevFeedbackSensor :                      'rev_feedback_sensor',
        param_t.eLimitSwitchEn :                          'limit_switch_en',
        param_t.eLimitSwitchClosedFor :                   'limit_switch_closed_for',
        param_t.eLimitSwitchClosedRev :                   'limit_switch_closed_rev',
        param_t.eSensorPosition :                         'ERR_DONT_USE_THIS',
        param_t.eSensorVelocity :                         'ERR_DONT_USE_THIS',
        param_t.eCurrent :                                'current',
        param_t.eBrakeIsEnabled :                         'brake_enabled',
        param_t.eEncPosition :                            'enc_position',
        param_t.eEncVel :                                 'enc_velocity',
        param_t.eEncIndexRiseEvents :                     'enc_index_rise_events',
        param_t.eQuadApin :                               'quad_apin',
        param_t.eQuadBpin :                               'quad_bpin',
        param_t.eQuadIdxpin :                             'quad_idxpin',
        param_t.eAnalogInWithOv :                         'analog_in_position',
        param_t.eAnalogInVel :                            'analog_in_velocity',
        param_t.eTemp :                                   'temp',
        param_t.eBatteryV :                               'battery',
        param_t.eResetCount :                             'reset_count',
        param_t.eResetFlags :                             'reset_flags',
        param_t.eFirmVers :                               'firmware_version',
        param_t.eSettingsChanged :                        'settings_changed',
        param_t.eQuadFilterEn :                           'quad_filter_en',
        param_t.ePidIaccum :                              'pid_iaccum',
        #param_t.eStatus1FrameRate : 94  # TALON_Status_1_General_10ms_t,
        #param_t.eStatus2FrameRate : 95  # TALON_Status_2_Feedback_20ms_t,
        #param_t.eStatus3FrameRate : 96  # TALON_Status_3_Enc_100ms_t,
        #param_t.eStatus4FrameRate : 97  # TALON_Status_4_AinTempVbat_100ms_t,
        #param_t.eStatus6FrameRate : 98  # TALON_Status_6_Eol_t,
        #param_t.eStatus7FrameRate : 99  # TALON_Status_7_Debug_200ms_t,
        param_t.eClearPositionOnIdx :                     'clear_position_on_idx',
        
        param_t.ePeakPosOutput :                          'peak_pos_output',
        param_t.eNominalPosOutput :                       'nominal_pos_output',
        param_t.ePeakNegOutput :                          'peak_neg_output',
        param_t.eNominalNegOutput :                       'nominal_neg_output',
        param_t.eQuadIdxPolarity :                        'quad_idx_polarity',
        #param_t.eStatus8FrameRate : 109  # TALON_Status_8_PulseWid_100ms_t,
        param_t.eAllowPosOverflow :                       'allow_pos_overflow',
        param_t.eProfileParamSlot0_AllowableClosedLoopErr: 'profile0_allowable_closed_loop_err',
        param_t.eNumberPotTurns :                         'number_pot_turns',
        param_t.eNumberEncoderCPR :                       'number_encoder_cpr',
        param_t.ePwdPosition :                            'pulse_width_position',
        param_t.eAinPosition :                            'analog_in_position',
        param_t.eProfileParamVcompRate :                  'profile_vcomp_rate',
        param_t.eProfileParamSlot1_AllowableClosedLoopErr : 'profile1_allowable_closed_loop_err',
        #param_t.eStatus9FrameRate : 118  # TALON_Status_9_MotProfBuffer_100ms_t,
        param_t.eMotionProfileHasUnderrunErr :            'motion_profile_has_underrun',
        #param_t.eReserved120 : 120,
        param_t.eLegacyControlMode :                      'legacy_mode'
    }

def __create_srx_sensor_position_map():
    '''Used to determine which dict value is returned based on the currently
       selected feedback_device''' 
    return {
        TalonSRXConst.kFeedbackDev_DigitalQuadEnc:              'enc_position',
        TalonSRXConst.kFeedbackDev_AnalogPot:                   'analog_in_position',
        TalonSRXConst.kFeedbackDev_AnalogEncoder:               'analog_in_position',
        TalonSRXConst.kFeedbackDev_CountEveryRisingEdge:        'analog_in_position',
        TalonSRXConst.kFeedbackDev_CountEveryFallingEdge:       'analog_in_position',
        TalonSRXConst.kFeedbackDev_CtreMagEncoder_Relative:     'pulse_width_position',
        TalonSRXConst.kFeedbackDev_CtreMagEncoder_Absolute:     'pulse_width_position',
        TalonSRXConst.kFeedbackDev_PosIsPulseWidth:             'pulse_width_position',
    }
    
def __create_srx_sensor_velocity_map():
    '''Used to determine which dict value is returned based on the currently
       selected feedback_device'''
    return {
        TalonSRXConst.kFeedbackDev_DigitalQuadEnc:              'enc_velocity',
        TalonSRXConst.kFeedbackDev_AnalogPot:                   'analog_in_velocity',
        TalonSRXConst.kFeedbackDev_AnalogEncoder:               'analog_in_velocity',
        TalonSRXConst.kFeedbackDev_CountEveryRisingEdge:        'analog_in_velocity',
        TalonSRXConst.kFeedbackDev_CountEveryFallingEdge:       'analog_in_velocity',
        TalonSRXConst.kFeedbackDev_CtreMagEncoder_Relative:     'pulse_width_velocity',
        TalonSRXConst.kFeedbackDev_CtreMagEncoder_Absolute:     'pulse_width_velocity',
        TalonSRXConst.kFeedbackDev_PosIsPulseWidth:             'pulse_width_velocity',
    }

_srx_param_map = __create_srx_param_map()
_srx_pos_map = __create_srx_sensor_position_map()
_srx_vel_map = __create_srx_sensor_velocity_map()
