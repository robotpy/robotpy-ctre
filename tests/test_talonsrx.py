import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture(scope='function')
def talon(ctre):
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
    assert cdata['value'] == 1

def test_talon_set3(talon, cdata):
    talon.set(talon.ControlMode.Position, 1, 55)
    assert talon.get() != 1
    assert cdata['control_mode'] == talon.ControlMode.Position
    assert cdata['value'] == 1

def test_talon_set4(talon, cdata):
    talon.set(talon.ControlMode.Current, 1.1)
    assert cdata['control_mode'] == talon.ControlMode.Current
    assert cdata['value'] == 1100

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


@pytest.mark.xfail(raises=NotImplementedError)
def test_talon_configForwardLimitSwitchSource(talon):
    talon.configForwardLimitSwitchSource(1, 2, 3)


@pytest.mark.xfail(raises=NotImplementedError)
def test_talon_configReverseLimitSwitchSource(talon):
    talon.configReverseLimitSwitchSource(1, 2, 3)


@pytest.mark.xfail(raises=NotImplementedError)
def test_talon_configPeakCurrentLimit(talon):
    talon.configPeakCurrentLimit(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_talon_configPeakCurrentDuration(talon):
    talon.configPeakCurrentDuration(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_talon_configContinuousCurrentLimit(talon):
    talon.configContinuousCurrentLimit(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
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


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_clearStickyFaults(talon):
    talon.clearStickyFaults(1)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configAllowableClosedloopError(talon):
    talon.configAllowableClosedloopError(1, 2, 3)


@pytest.mark.xfail(raises=NotImplementedError)
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


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configGetParameter(talon):
    talon.configGetParameter(1,2,3)

def test_basemotorcontroller_configMaxIntegralAccumulator(talon, cdata):
    talon.configMaxIntegralAccumulator(1, 2.0, 3)
    assert cdata['profile1_max_iaccum'] == 2.0


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configMotionAcceleration(talon):
    talon.configMotionAcceleration(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configMotionCruiseVelocity(talon):
    talon.configMotionCruiseVelocity(1,2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configNeutralDeadband(talon):
    talon.configNeutralDeadband(1,2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configNominalOutputForward(talon):
    talon.configNominalOutputForward(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configNominalOutputReverse(talon):
    talon.configNominalOutputReverse(1,2)


def test_basemotorcontroller_configOpenLoopRamp(talon, cdata):
    talon.configOpenLoopRamp(1,2)
    assert cdata['open_loop_ramp'] == 1


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configPeakOutputForward(talon):
    talon.configPeakOutputForward(1,2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configPeakOutputReverse(talon):
    talon.configPeakOutputReverse(1,2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configRemoteFeedbackFilter(talon):
    talon.configRemoteFeedbackFilter(1,2,3,4)


def test_basemotorcontroller_configReverseSoftLimitEnable(talon, cdata):
    talon.configReverseSoftLimitEnable(True,2)
    assert cdata['soft_limit_rev_enable'] == True


def test_basemotorcontroller_configReverseSoftLimitThreshold(talon, cdata):
    talon.configReverseSoftLimitThreshold(1,2)
    assert cdata['soft_limit_rev'] == 1


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configSensorTerm(talon):
    talon.configSensorTerm(1,2,3)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configSetCustomParam(talon):
    talon.configSetCustomParam(1,2,3)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configSetParameter(talon):
    talon.configSetParameter(1,2,3,4,5)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configVelocityMeasurementPeriod(talon):
    talon.configVelocityMeasurementPeriod(1,2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configVelocityMeasurementWindow(talon):
    talon.configVelocityMeasurementWindow(1,2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configVoltageCompSaturation(talon):
    talon.configVoltageCompSaturation(1,2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_configVoltageMeasurementFilter(talon):
    talon.configVoltageMeasurementFilter(1,2)


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


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_enableHeadingHold(talon):
    talon.enableHeadingHold(True)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_enableVoltageCompensation(talon):
    talon.enableVoltageCompensation(True)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_follow(talon, ctre):
    master = ctre.WPI_TalonSRX(3)
    talon.follow(master)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getActiveTrajectoryHeading(talon):
    talon.getActiveTrajectoryHeading()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getActiveTrajectoryPosition(talon):
    talon.getActiveTrajectoryPosition()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getActiveTrajectoryVelocity(talon):
    talon.getActiveTrajectoryVelocity()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getBaseID(talon):
    talon.getBaseID()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getBusVoltage(talon):
    talon.getBusVoltage()


def test_basemotorcontroller_getClosedLoopError(talon, cdata):
    cdata['pid1_error'] = 42
    assert talon.getClosedLoopError(1) == 42


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getControlMode(talon):
    talon.getControlMode()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getDeviceID(talon):
    talon.getDeviceID()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getErrorDerivative(talon):
    talon.getErrorDerivative(1)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getFaults(talon, ctre):
    errcode, faults = talon.getFaults()


def test_basemotorcontroller_getFirmwareVersion(talon):
    talon.getFirmwareVersion()


def test_basemotorcontroller_getIntegralAccumulator(talon, cdata):
    cdata['pid1_iaccum'] = 22.0
    assert talon.getIntegralAccumulator(1) == 22.0


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getLastError(talon):
    talon.getLastError()


def test_basemotorcontroller_getMotionProfileStatus(talon, ctre):
    with patch('ctre._impl.MotController._getMotionProfileStatus_2') as mock:
        mock.return_value = in_val = (1, 2, 3, True, False, True, False, 4, 5 , 6, 7)
        m = talon.getMotionProfileStatus()

        for i in range(10):
            assert m[i] == in_val[i]


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getMotionProfileTopLevelBufferCount(talon):
    talon.getMotionProfileTopLevelBufferCount()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getMotorOutputPercent(talon):
    talon.getMotorOutputPercent()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_getMotorOutputVoltage(talon):
    talon.getMotorOutputVoltage()


def test_basemotorcontroller_getOutputCurrent(talon, cdata):
    cdata['output_current'] = 42.0
    assert 41.99 < talon.getOutputCurrent() < 42.01

@pytest.mark.xfail(raises=NotImplementedError)
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


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_hasResetOccurred(talon):
    talon.hasResetOccurred()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_isMotionProfileTopLevelBufferFull(talon):
    talon.isMotionProfileTopLevelBufferFull()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_neutralOutput(talon):
    talon.neutralOutput()


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_overrideLimitSwitchesEnable(talon):
    talon.overrideLimitSwitchesEnable(True)


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


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_selectDemandType(talon):
    talon.selectDemandType(True)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_selectProfileSlot(talon):
    talon.selectProfileSlot(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_setControlFramePeriod(talon):
    talon.setControlFramePeriod(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_setIntegralAccumulator(talon):
    talon.setIntegralAccumulator(1, 2, 3)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_setInverted(talon):
    talon.setInverted(True)

    assert talon.getInverted() == True


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_setNeutralMode(talon):
    talon.setNeutralMode(1)


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


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_setSensorPhase(talon):
    talon.setSensorPhase(True)


@pytest.mark.xfail(raises=NotImplementedError)
def test_basemotorcontroller_setStatusFramePeriod(talon):
    talon.setStatusFramePeriod(1, 2, 3)


def test_basemotorcontroller_valueUpdated(talon):
    talon.valueUpdated()
