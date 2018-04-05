import math
import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture(scope='function')
def talon(ctre):
    ctre.WPI_TalonSRX.Notifier = None
    return ctre.WPI_TalonSRX(1)

@pytest.fixture(scope='function')
def cdata(talon, hal_data):
    return hal_data['CAN'][1]



def test_talon_init(ctre, hal_data):
    assert 1 not in hal_data['CAN']
    ctre.WPI_TalonSRX(1)
    assert 1 in hal_data['CAN']
    assert hal_data['CAN'][1]['type'] == 'talonsrx'


def test_talon_get(talon):
    assert talon.get() == 0


def test_talon_set1(talon, cdata):
    talon.set(1)
    assert talon.get() == 1
    assert cdata['control_mode'] == talon.ControlMode.PercentOutput
    assert cdata['value'] == 1

def test_talon_set2(talon, cdata):
    talon.set(talon.ControlMode.Velocity, 1)
    print(talon.get())
    assert talon.get() != 1
    assert cdata['control_mode'] == talon.ControlMode.Velocity
    assert cdata['pid0_target'] == 1

def test_talon_set3(talon, cdata):
    talon.set(talon.ControlMode.Position, 1, 55)
    assert talon.get() != 1
    assert cdata['control_mode'] == talon.ControlMode.Position
    assert cdata['pid0_target'] == 1

def test_talon_set4(talon, cdata):
    talon.set(talon.ControlMode.Current, 1.1)
    assert cdata['control_mode'] == talon.ControlMode.Current
    assert cdata['pid0_target'] == 1100

def test_talon_set5(ctre, talon, cdata):
    print(talon, dir(talon))
    ctre.TalonSRX.set(talon, talon.ControlMode.Current, 1.1, talon.DemandType.ArbitraryFeedForward, 0.4)
    assert cdata['control_mode'] == talon.ControlMode.Current
    assert cdata['pid0_target'] == 1100
    # TODO: demand1 not stored anywhere..

def test_talon_disable(talon, cdata):
    talon.disable()
    assert cdata['control_mode'] == talon.ControlMode.Disabled
    assert cdata['value'] == 0

def test_talon_stopMotor(talon, cdata):
    talon.stopMotor()
    assert cdata['control_mode'] == talon.ControlMode.Disabled
    assert cdata['value'] == 0

def test_talon_setinverted(talon, cdata):
    assert cdata['inverted'] == False
    talon.setInverted(True)
    assert cdata['inverted'] == True


def test_talon_initSendable(talon, sendablebuilder):
    talon.set(4)

    talon.initSendable(sendablebuilder)

    sendablebuilder.updateTable()

    assert sendablebuilder.getTable().getNumber("Value", 0.0) == 4

    sendablebuilder.properties[0].setter(3)

    assert talon.get() == 3


def test_talon_configPeakCurrentLimit(talon):
    talon.configPeakCurrentLimit(1, 2)


def test_talon_configPeakCurrentDuration(talon):
    talon.configPeakCurrentDuration(1, 2)


def test_talon_configContinuousCurrentLimit(talon):
    talon.configContinuousCurrentLimit(1, 2)


def test_talon_enableCurrentLimit(talon):
    talon.enableCurrentLimit(True)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_changeMotionControlFramePeriod(talon):
    talon.changeMotionControlFramePeriod(1)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_clearMotionProfileHasUnderrun(talon):
    talon.clearMotionProfileHasUnderrun(1)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_clearMotionProfileTrajectories(talon):
    talon.clearMotionProfileTrajectories()


def test_basemotorcontroller_clearStickyFaults(talon):
    talon.clearStickyFaults(1)


def test_basemotorcontroller_configClosedLoopRamp(talon):
    talon.configClosedLoopRamp(1,2)


def test_basemotorcontroller_configForwardSoftLimitEnable(talon, cdata):
    talon.configForwardSoftLimitEnable(True, 2)
    assert cdata['soft_limit_for_enable'] == True


def test_basemotorcontroller_configForwardSoftLimitThreshold(talon, cdata):
    talon.configForwardSoftLimitThreshold(1, 2)
    assert cdata['soft_limit_for'] == 1


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configGetCustomParam(talon):
    talon.configGetCustomParam(1, 2)


config_data = [
    ("eOpenloopRamp", 0, "open_loop_ramp", 0.5),
    ("eClosedloopRamp", 0, "closed_loop_ramp", 0.5),
    ("eNeutralDeadband", 0, "neutral_deadband", 0.5),
    ("ePeakPosOutput", 0, "peak_fwd_output", 0.5),
    ("eNominalPosOutput", 0, "nom_fwd_output", 0.5),
    ("ePeakNegOutput", 0, "peak_rev_output", 0.5),
    ("eNominalNegOutput", 0, "nom_rev_output", 0.5),
    ("eProfileParamSlot_P", 0, "profile0_p", 0.1),
    ("eProfileParamSlot_P", 1, "profile1_p", 0.2),
    ("eProfileParamSlot_I", 0, "profile0_i", 0.1),
    ("eProfileParamSlot_I", 1, "profile1_i", 0.2),
    ("eProfileParamSlot_D", 0, "profile0_d", 0.1),
    ("eProfileParamSlot_D", 1, "profile1_d", 0.2),
    ("eProfileParamSlot_F", 0, "profile0_f", 0.1),
    ("eProfileParamSlot_F", 1, "profile1_f", 0.2),
    ("eProfileParamSlot_IZone", 0, "profile0_izone", 200.0),
    ("eProfileParamSlot_IZone", 1, "profile1_izone", 300.0),
    ("eProfileParamSlot_AllowableErr", 0, "profile0_allowableError", 400.0),
    ("eProfileParamSlot_AllowableErr", 1, "profile1_allowableError", 401.0),
    ("eProfileParamSlot_MaxIAccum", 0, "profile0_max_iaccum", 101.0),
    ("eProfileParamSlot_MaxIAccum", 1, "profile1_max_iaccum", 102.0),
    ("eSampleVelocityPeriod", 0, "vel_measurement_period", 2.0),
    ("eSampleVelocityWindow", 0, "vel_measurement_window", 1.0),
    ("eMotMag_Accel", 0, "motionmagic_acceleration", 1.0),
    ("eMotMag_VelCruise", 0, "motionmagic_velocity", 1.0),
    ("eClearPositionOnLimitF", 0, "clear_pos_on_limit_fwd", 1.0),
    ("eClearPositionOnLimitR", 0, "clear_pos_on_limit_rev", 1.0),
]

@pytest.mark.parametrize("param_name, slot, cdata_key, value", config_data)
def test_basemotorcontroller_configGetParameter(talon, ctre, cdata, param_name, cdata_key, value, slot):
    param = ctre.ParamEnum[param_name]
    cdata[cdata_key] = value
    assert talon.configGetParameter(param, slot, 0) == value


@pytest.mark.parametrize("param_name, slot, cdata_key, value", config_data)
def test_basemotorcontroller_configSetParameter(talon, ctre, cdata, param_name, cdata_key, value, slot):
    param = ctre.ParamEnum[param_name]
    talon.configSetParameter(param, value, 0, slot, 0)
    assert cdata[cdata_key] == value


def test_clear_position_on_limit_forward(talon, cdata, ctre):
    talon.selectProfileSlot(0, 0)
    talon.configSelectedFeedbackSensor(talon.FeedbackDevice.QuadEncoder, 0, 0)
    talon.configSetParameter(ctre.ParamEnum.eClearPositionOnLimitF, 1, 0, 0, 0)
    cdata['limit_switch_closed_for'] = 0
    cdata['quad_position'] = 10
    talon._calculate_1ms()
    assert cdata['quad_position'] == 10
    cdata['limit_switch_closed_for'] = 1
    talon._calculate_1ms()
    assert cdata['quad_position'] == 0


def test_clear_position_on_limit_reverse(talon, cdata, ctre):
    talon.selectProfileSlot(0, 0)
    talon.configSelectedFeedbackSensor(talon.FeedbackDevice.QuadEncoder, 0, 0)
    talon.configSetParameter(ctre.ParamEnum.eClearPositionOnLimitR, 1, 0, 0, 0)
    cdata['limit_switch_closed_rev'] = 0
    cdata['quad_position'] = 10
    talon._calculate_1ms()
    assert cdata['quad_position'] == 10
    cdata['limit_switch_closed_rev'] = 1
    talon._calculate_1ms()
    assert cdata['quad_position'] == 0


def test_basemotorcontroller_configMaxIntegralAccumulator(talon, cdata):
    talon.configMaxIntegralAccumulator(1, 2.0, 3)
    assert cdata['profile1_max_iaccum'] == 2.0


def test_basemotorcontroller_configNeutralDeadband(talon, cdata):
    talon.configNeutralDeadband(0.3, 0)
    assert cdata['neutral_deadband'] == 0.3


def test_basemotorcontroller_configNominalOutputForward(talon, cdata):
    talon.configNominalOutputForward(0.7, 0)
    assert cdata['nom_fwd_output'] == 0.7


def test_basemotorcontroller_configNominalOutputReverse(talon, cdata):
    talon.configNominalOutputReverse(-0.7, 0)
    assert cdata['nom_rev_output'] == -0.7


def test_basemotorcontroller_configOpenLoopRamp(talon, cdata):
    talon.configOpenLoopRamp(1,2)
    assert cdata['open_loop_ramp'] == 1


def test_basemotorcontroller_configPeakOutputForward(talon, cdata):
    talon.configPeakOutputForward(0.9, 0)
    assert cdata['peak_fwd_output'] == 0.9


def test_basemotorcontroller_configPeakOutputReverse(talon, cdata):
    talon.configPeakOutputReverse(-0.9, 0)
    assert cdata['peak_rev_output'] == -0.9


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configRemoteFeedbackFilter(talon):
    talon.configRemoteFeedbackFilter(1,2,3,4)


def test_basemotorcontroller_configReverseSoftLimitEnable(talon, cdata):
    talon.configReverseSoftLimitEnable(True,2)
    assert cdata['soft_limit_rev_enable'] == True


def test_basemotorcontroller_configReverseSoftLimitThreshold(talon, cdata):
    talon.configReverseSoftLimitThreshold(1,2)
    assert cdata['soft_limit_rev'] == 1


def test_basemotorcontroller_configSensorTerm(talon, cdata):
    talon.configSensorTerm(5, 6, 0)
    assert cdata['sensor_term'] == (5, 6)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configSetCustomParam(talon):
    talon.configSetCustomParam(1,2,3)


def test_basemotorcontroller_configVelocityMeasurementPeriod(talon, cdata):
    talon.configVelocityMeasurementPeriod(23, 0)
    assert cdata['vel_measurement_period'] == 23


def test_basemotorcontroller_configVelocityMeasurementWindow(talon, cdata):
    talon.configVelocityMeasurementWindow(33, 0)
    assert cdata['vel_measurement_window'] == 33


def test_basemotorcontroller_configVoltageCompSaturation(talon, cdata):
    talon.configVoltageCompSaturation(3, 0)
    assert cdata['voltage_comp_saturation'] == 3


def test_basemotorcontroller_configVoltageMeasurementFilter(talon, cdata):
    talon.configVoltageMeasurementFilter(5, 0)
    assert cdata['voltage_measurement_filter'] == 5


def test_basemotorcontroller_config_IntegralZone(talon, cdata):
    talon.config_IntegralZone(1,2,3)
    assert cdata['profile1_izone'] == 2


def test_basemotorcontroller_config_kD(talon, cdata):
    talon.config_kD(1, 2, 3)
    assert cdata['profile1_d'] == 2


def test_basemotorcontroller_config_kF(talon, cdata):
    talon.config_kF(1, 2, 3)
    assert cdata['profile1_f'] == 2


def test_basemotorcontroller_config_kI(talon, cdata):
    talon.config_kI(1, 2, 3)
    assert cdata['profile1_i'] == 2


def test_basemotorcontroller_config_kP(talon, cdata):
    talon.config_kP(1, 2, 3)
    assert cdata['profile1_p'] == 2


def test_basemotorcontroller_enableHeadingHold(talon):
    talon.enableHeadingHold(True)


def test_basemotorcontroller_enableVoltageCompensation(talon, cdata):
    talon.enableVoltageCompensation(True)
    assert cdata['voltage_comp_enabled'] == True


def test_basemotorcontroller_follow(ctre, talon, cdata):
    master = ctre.WPI_TalonSRX(3)
    talon.follow(master)
    assert cdata['follow_target'] == 3


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getActiveTrajectoryHeading(talon):
    talon.getActiveTrajectoryHeading()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getActiveTrajectoryPosition(talon):
    talon.getActiveTrajectoryPosition()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getActiveTrajectoryVelocity(talon):
    talon.getActiveTrajectoryVelocity()


def test_basemotorcontroller_getBaseID(talon):
    talon.getBaseID()


def test_basemotorcontroller_getBusVoltage(talon, cdata):
    cdata['bus_voltage'] = 12.7
    assert talon.getBusVoltage() == 12.7


def test_basemotorcontroller_getClosedLoopError(talon, cdata):
    cdata['pid1_error'] = 42
    assert talon.getClosedLoopError(1) == 42


def test_basemotorcontroller_getControlMode(talon):
    talon.set(talon.ControlMode.Position, 1)
    assert talon.getControlMode() == talon.ControlMode.Position


def test_basemotorcontroller_getDeviceID(talon):
    talon.getDeviceID()


def test_basemotorcontroller_getErrorDerivative(talon, cdata):
    cdata['pid1_errorDerivative'] = 50.
    assert talon.getErrorDerivative(1) == 50.

def test_basemotorcontroller_limitSwitches(ctre, hal_data, talon, cdata):
    
    # local
    for v in (True, False):
        cdata['limit_switch_closed_for'] = v
        cdata['limit_switch_closed_rev'] = not v
        assert talon.isFwdLimitSwitchClosed() == v
        assert talon.isRevLimitSwitchClosed() == (not v)
        
        assert talon.getLimitSwitchState() == (v, (not v))
    
    # remote
    talon.configForwardLimitSwitchSource(talon.LimitSwitchSource.RemoteTalonSRX,
                                         talon.LimitSwitchNormal.NormallyOpen, 2, 0)
    talon.configReverseLimitSwitchSource(talon.LimitSwitchSource.RemoteTalonSRX,
                                         talon.LimitSwitchNormal.NormallyOpen, 2, 0)
    
    # The above should work without us creating the remote talon?
    talon2 = ctre.WPI_TalonSRX(2)
    cdata2 = hal_data['CAN'][2]
    
    for v in (True, False):
        cdata['limit_switch_closed_for'] = not v
        cdata2['limit_switch_closed_for'] = v
        cdata['limit_switch_closed_rev'] = v
        cdata2['limit_switch_closed_rev'] = not v
        
        assert talon.isFwdLimitSwitchClosed() == v
        assert talon.isRevLimitSwitchClosed() == (not v)
        assert talon2.isFwdLimitSwitchClosed() == v
        assert talon2.isRevLimitSwitchClosed() == (not v)
        
        assert talon.getLimitSwitchState() == (v, (not v))
        assert talon2.getLimitSwitchState() == (v, (not v))


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getFaults(talon, ctre):
    errcode, faults = talon.getFaults()


def test_basemotorcontroller_getFirmwareVersion(talon):
    talon.getFirmwareVersion()


def test_basemotorcontroller_getIntegralAccumulator(talon, cdata):
    cdata['pid1_iaccum'] = 22.0
    assert talon.getIntegralAccumulator(1) == 22.0


def test_basemotorcontroller_getLastError(talon, ctre, cdata):
    cdata['last_error'] = ctre.ErrorCode.OK
    talon.getLastError() == ctre.ErrorCode.OK


def test_basemotorcontroller_getMotionProfileStatus(talon, ctre):
    with patch('ctre._impl.MotController._getMotionProfileStatus_2') as mock:
        mock.return_value = in_val = (1, 2, 3, True, False, True, False, 4, 5 , 6, 7)
        m = talon.getMotionProfileStatus()

        for i in range(10):
            assert m[i] == in_val[i]


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getMotionProfileTopLevelBufferCount(talon):
    talon.getMotionProfileTopLevelBufferCount()


def test_basemotorcontroller_getMotorOutputPercent(talon, cdata):
    cdata['value'] = 2.2
    assert talon.getMotorOutputPercent() == 2.2


def test_basemotorcontroller_getMotorOutputVoltage(talon, cdata):
    cdata['bus_voltage'] = 12.7
    cdata['value'] = 0.5
    assert talon.getMotorOutputVoltage() == 6.35


def test_basemotorcontroller_getOutputCurrent(talon, cdata):
    cdata['output_current'] = 42.0
    assert 41.99 < talon.getOutputCurrent() < 42.01

def test_basemotorcontroller_getSensorCollection(talon):
    talon.getSensorCollection()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getStatusFramePeriod(talon):
    talon.getStatusFramePeriod(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getStickyFaults(talon):
    errcode, stickyfaults = talon.getStickyFaults()


def test_basemotorcontroller_getTemperature(talon, cdata):
    cdata['temp'] = 42.0
    assert talon.getTemperature() == 42.0


def test_basemotorcontroller_hasResetOccurred(talon):
    assert talon.hasResetOccurred() == False


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_isMotionProfileTopLevelBufferFull(talon):
    talon.isMotionProfileTopLevelBufferFull()


def test_basemotorcontroller_neutralOutput(talon):
    talon.neutralOutput()


def test_basemotorcontroller_overrideLimitSwitchesEnable(talon, cdata):
    talon.overrideLimitSwitchesEnable(True)
    assert cdata['limit_switch_usable'] == True


def test_basemotorcontroller_overrideSoftLimitsEnable(talon, cdata):
    talon.overrideSoftLimitsEnable(True)
    assert cdata['soft_limit_usable'] == True
    
    talon.overrideSoftLimitsEnable(False)
    assert cdata['soft_limit_usable'] == False


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_processMotionProfileBuffer(talon):
    talon.processMotionProfileBuffer()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_pushMotionProfileTrajectory(talon, ctre):
    point = ctre.TrajectoryPoint(1, 2, 3, 0, 0, True, True,
                                 ctre.TrajectoryPoint.TrajectoryDuration.T0ms)
    talon.pushMotionProfileTrajectory(point)


def test_basemotorcontroller_selectDemandType(talon):
    talon.selectDemandType(True)


def test_basemotorcontroller_selectProfileSlot(talon, cdata):
    talon.selectProfileSlot(1, 1)
    assert cdata['profile_slot_select'] == 1
    assert cdata['pid_slot_select'] == 1


def test_basemotorcontroller_setControlFramePeriod(talon):
    talon.setControlFramePeriod(1, 2)


def test_basemotorcontroller_setIntegralAccumulator(talon, cdata):
    talon.setIntegralAccumulator(2, 1, 0)
    assert cdata['pid1_iaccum'] == 2


def test_basemotorcontroller_setInverted(talon):
    talon.setInverted(True)

    assert talon.getInverted() == True


def test_basemotorcontroller_setNeutralMode(talon, cdata):
    talon.setNeutralMode(1)
    assert cdata['neutral_mode'] == 1


def test_basemotorcontroller_selectedSensorPosition(talon, cdata):
    # no selected device, should not fail
    talon.setSelectedSensorPosition(32, 0, 0)
    
    assert talon.getSelectedSensorPosition(0) == 0
    assert talon.getSelectedSensorPosition(1) == 0
    
    # select a device
    talon.configSelectedFeedbackSensor(talon.FeedbackDevice.QuadEncoder, 0, 0)
    
    assert cdata['pid0_feedback'] == talon.FeedbackDevice.QuadEncoder
    
    talon.setSelectedSensorPosition(32, 0, 0)
    
    assert cdata['quad_position'] == 32
    assert talon.getSelectedSensorPosition(0) == 32
    assert talon.getSelectedSensorPosition(1) == 0


def test_basemotorcontroller_setSensorPhase(talon, cdata):
    talon.setSensorPhase(True)
    assert cdata['sensor_phase'] == True


def test_basemotorcontroller_setStatusFramePeriod(talon):
    talon.setStatusFramePeriod(1, 2, 3)


def test_basemotorcontroller_getClosedLoopTarget(talon, cdata):
    cdata['pid0_target'] = 44
    cdata['pid1_target'] = 55
    assert talon.getClosedLoopTarget(0) == 44
    assert talon.getClosedLoopTarget(1) == 55


def test_basemotorcontroller_valueUpdated(talon):
    talon.valueUpdated()


def assert_is_almost_equal(expected, actual, rel_tol=0, abs_tol=0.00001):
    assert math.isclose(expected, actual, rel_tol=rel_tol, abs_tol=abs_tol), "expected: %f, got: %f" % (expected, actual)

# simulation logic

@pytest.mark.parametrize('initial_pos, initial_vel, expected_vel, expected_pos', [
    (0, 0, 2.457, 0.02457),
    (1, 0, 2.457, 1.02457),
    (40960, 0, 0, 4096 * 10),
    (40960, 2, 0, 4096 * 10),
    (40960, -2, 0, 4096 * 10),
    (40960, 3, 0.543, 40960 + 0.00543),
    (40960, -3, -0.543, 40960 - 0.00543),
    (38912, 0, 2.457, 38912 + 0.02457),
    (43008, 0, -2.457, 43008 - 0.02457),
    (43008, 1228, 1228-2.457, 43008 + 12.25543),
    (41041, -600, -600+2.457, 41041 - 5.97543),
    (40878, -600, -600+2.457, 40878 - 5.97543),
    (40878, 600, 600-2.457, 40878 + 5.97543),
    (40878, -60, -60+2.457, 40878 - .57543),
    (41041, 60, 60-2.457, 41041 + .57543),
    (-40878, 1300, 1300-2.457, -40878 + 12.97543),
    (90878, -1300, -1300+2.457, 90878 - 12.97543),
    ])
def test_motion_magic_next_target(talon, cdata, initial_pos, initial_vel, expected_vel, expected_pos):
    # an encoder that measures 4096 ticks per revolution, or so we shall assume
    talon.configSelectedFeedbackSensor(talon.FeedbackDevice.QuadEncoder, 0, 0)
    talon.configMotionCruiseVelocity(int(3 * 4096 * 0.1), 0) # 1 rps
    talon.configMotionAcceleration(int(6 * 4096 * 0.1), 0) # 2 rps^2
    talon.configAllowableClosedloopError(0, 2, 0)
    talon.selectProfileSlot(0, 0)

    cdata['quad_position'] = int(initial_pos)
    cdata['quad_velocity'] = int(initial_vel)

    talon.setDemand(talon.ControlMode.MotionMagic, 10 * 4096, 0) # 10 rotations

    assert cdata['pid0_target'] == int(initial_pos)
    assert cdata['motionmagic_acceleration'] == 2457
    assert cdata['motionmagic_cruise_velocity'] == 1228
    assert cdata['motionmagic_target'] == 10 * 4096
    assert cdata['motionmagic_velocity'] == int(initial_vel)

    target = talon._motion_magic_next_target()

    assert_is_almost_equal(expected_vel, cdata['motionmagic_velocity'])
    assert_is_almost_equal(expected_pos, target)


def test_calculate_pid1(talon, cdata):
    # an encoder that measures 4096 ticks per revolution, or so we shall assume
    talon.configSelectedFeedbackSensor(talon.FeedbackDevice.QuadEncoder, 0, 0)
    talon.config_kP(0, 4, 0)
    talon.config_kI(0, 0, 0)
    talon.config_kD(0, 0, 0)
    talon.config_kF(0, 0, 0)
    talon.selectProfileSlot(0, 0)
    cdata['quad_position'] = 0
    talon.set(talon.ControlMode.Position, 4096)

    assert not talon._notFirst
    talon._calculate_1ms()
    assert talon._notFirst

    talon._calculate_1ms()

    assert talon._iAccum == 4096
    assert talon._err == 4096
    assert cdata['pid0_errorDerivative'] == 0
    assert talon._prevErr == 4096
    assert_is_almost_equal(1., cdata['value'])

    cdata['quad_position'] = 3900
    
    talon._calculate_1ms()

    assert talon._iAccum == 4292
    assert talon._err == 196
    assert cdata['pid0_errorDerivative'] == -3900
    assert talon._prevErr == 196
    assert_is_almost_equal(0.766373, cdata['value'])


def test_calculate_pid2(talon, cdata):
    # an encoder that measures 4096 ticks per revolution, or so we shall assume
    talon.configSelectedFeedbackSensor(talon.FeedbackDevice.QuadEncoder, 0, 0)
    talon.config_kP(0, 0, 0)
    talon.config_kI(0, 0.04, 0)
    talon.config_kD(0, 0, 0)
    talon.config_kF(0, 0, 0)
    talon.selectProfileSlot(0, 0)
    cdata['quad_position'] = 0
    talon.set(talon.ControlMode.Position, 4096)

    assert not talon._notFirst
    talon._calculate_1ms()
    assert talon._notFirst

    talon._calculate_1ms()

    assert talon._iAccum == 4096
    assert talon._err == 4096
    assert cdata['pid0_errorDerivative'] == 0
    assert talon._prevErr == 4096
    assert_is_almost_equal(0.160156, cdata['value'])

    cdata['quad_position'] = 3900
    
    talon._calculate_1ms()

    assert talon._iAccum == 4292
    assert talon._err == 196
    assert cdata['pid0_errorDerivative'] == -3900
    assert talon._prevErr == 196
    assert_is_almost_equal(0.167820, cdata['value'])


def test_calculate_pid3(talon, cdata):
    # an encoder that measures 4096 ticks per revolution, or so we shall assume
    talon.configSelectedFeedbackSensor(talon.FeedbackDevice.QuadEncoder, 0, 0)
    talon.config_kP(0, 0, 0)
    talon.config_kI(0, 0, 0)
    talon.config_kD(0, 0.4, 0)
    talon.config_kF(0, 0, 0)
    talon.selectProfileSlot(0, 0)
    cdata['quad_position'] = 0
    talon.set(talon.ControlMode.Position, 4096)

    assert not talon._notFirst
    talon._calculate_1ms()
    assert talon._notFirst

    talon._calculate_1ms()

    assert talon._iAccum == 4096
    assert talon._err == 4096
    assert cdata['pid0_errorDerivative'] == 0
    assert talon._prevErr == 4096
    assert_is_almost_equal(0, cdata['value'])

    cdata['quad_position'] = 3900
    
    talon._calculate_1ms()

    assert talon._iAccum == 4292
    assert talon._err == 196
    assert cdata['pid0_errorDerivative'] == -3900
    assert talon._prevErr == 196
    assert_is_almost_equal(-1, cdata['value'])

    cdata['quad_position'] = 3980
    talon._calculate_1ms()

    assert talon._iAccum == 4408
    assert talon._err == 116
    assert cdata['pid0_errorDerivative'] == -80
    assert talon._prevErr == 116
    assert_is_almost_equal(-0.031281, cdata['value'])


def test_calculate_pid4(talon, cdata):
    # an encoder that measures 4096 ticks per revolution, or so we shall assume
    talon.configSelectedFeedbackSensor(talon.FeedbackDevice.QuadEncoder, 0, 0)
    talon.config_kP(0, 4, 0)
    talon.config_kI(0, 0, 0)
    talon.config_kD(0, 0.0, 0)
    talon.config_kF(0, 0, 0)
    talon.selectProfileSlot(0, 0)
    cdata['quad_position'] = 0
    talon.set(talon.ControlMode.Position, 40960)

    talon._calculate_1ms()

    talon._calculate_1ms()
    assert_is_almost_equal(1, cdata['value'])

    # reset
    talon.set(talon.ControlMode.Position, 0)
    talon._calculate_1ms()
    talon.set(talon.ControlMode.Position, 40960)

    talon.configClosedLoopRamp(3, 0)
    talon._calculate_1ms()
    assert_is_almost_equal(0.000333, cdata['value'])
