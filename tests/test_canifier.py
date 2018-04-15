import pytest
from unittest.mock import MagicMock


@pytest.fixture(scope='function')
def canifier(ctre):
    return ctre.CANifier(1)
    
@pytest.fixture(scope='function')
def cdata(canifier, hal_data):
    return hal_data['CAN'][1]


def test_canifier_init(ctre, hal_data):
    assert 1 not in hal_data['CAN']
    ctre.CANifier(1)
    assert 1 in hal_data['CAN']
    
def test_canifier_setLEDOutput(canifier, cdata):
    canifier.setLEDOutput(0.1, canifier.LEDChannel.C)
    # TODO pytest bug?
    # assert cdata['led_c'] == pytest.approx(0.1, 0.01)

def test_canifier_setGeneralOutput(canifier, cdata):
    canifier.setGeneralOutput(canifier.GeneralPin.QUAD_A, True, True)
    assert cdata['general_pin_outputs'] == 0x04
    assert cdata['general_pin_is_output'] == 0x04

def test_canifier_setGeneralOutputs(canifier, cdata):
    canifier.setGeneralOutputs(2, 1)
    assert cdata['general_pin_outputs'] == 2
    assert cdata['general_pin_is_output'] == 1

@pytest.mark.xfail(raises=AttributeError)
def test_canifier_getGeneralInputs(ctre, canifier):
    pin_values = ctre.canifier.PinValues()
    canifier.getGeneralInputs(pin_values)

def test_canifier_getGeneralInput(canifier, cdata):
    assert canifier.getGeneralInput(2) == False
    assert canifier.getGeneralInput(3) == False
    cdata['general_pin_inputs'] = 0x04
    assert canifier.getGeneralInput(2) == True
    assert canifier.getGeneralInput(3) == False
    cdata['general_pin_inputs'] = 0x08
    assert canifier.getGeneralInput(2) == False
    assert canifier.getGeneralInput(3) == True

def test_canifier_lastError(ctre, canifier, cdata):
    canifier.setLastError(int(ctre.ErrorCode.GeneralWarning))
    assert canifier.getLastError() == ctre.ErrorCode.GeneralWarning

def test_canifier_setPWMOutput(canifier, cdata):
    output = 102 / 1023.0
    canifier.setPWMOutput(canifier.PWMChannel.C2, output)
    # TODO: pytest bug?
    #assert cdata['pwm_2'] == pytest.approx(output, 0.001)

def test_canifier_enablePWMOutput(canifier, cdata):
    canifier.enablePWMOutput(canifier.PWMChannel.C1, True)
    assert cdata['pwm_1_en'] == True

def test_canifier_getPWMInput(canifier, cdata):
    dutyCycle, period = canifier.getPWMInput(canifier.PWMChannel.C1)
    #assert dutyCycle == pytest.approx(0.0042, 0.01)
    # TODO: pytest bug?

@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_configSetCustomParam(canifier, cdata):
    canifier.configSetCustomParam(1, 2, 3)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_configGetCustomParam(canifier, cdata):
    canifier.configGetCustomParam(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_configSetParameter(canifier, cdata):
    canifier.configSetParameter(1, 2, 3, 4, 5)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_configGetParameter(canifier, cdata):
    canifier.configGetParameter(1, 2, 3)

def test_canifier_statusFramePeriod(canifier, cdata):
    canifier.setStatusFramePeriod(canifier.StatusFrame.Status_1_General, 2, 0)
    assert canifier.getStatusFramePeriod(canifier.StatusFrame.Status_1_General, 0) == 2

def test_canifier_setControlFramePeriod(canifier, cdata):
    canifier.setControlFramePeriod(canifier.ControlFrame.CANifier_Control_1_General, 2)
    assert cdata['control_1'] == 2

def test_canifier_getFirmwareVersion(canifier, cdata):
    assert canifier.getFirmwareVersion() == 0

def test_canifier_hasResetOccurred(canifier, cdata):
    assert canifier.hasResetOccurred() == False
    cdata['reset_occurred'] = True
    assert canifier.hasResetOccurred() == True
    assert canifier.hasResetOccurred() == False


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_getFaults(canifier, cdata):
    canifier.getFaults()


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_getStickyFaults(canifier, cdata):
    canifier.getStickyFaults()


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_clearStickyFaults(canifier, cdata):
    canifier.clearStickyFaults(1)

def test_canifier_getBusVoltage(canifier, cdata):
    canifier.getBusVoltage()
