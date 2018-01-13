import pytest
from unittest.mock import MagicMock


@pytest.fixture(scope='function')
def canifier(ctre):
    return ctre.CANifier(1)


def test_canifier_init(ctre):
    ctre.CANifier(1)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_setLEDOutput(canifier):
    canifier.setLEDOutput(0.1, 3)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_setGeneralOutput(canifier):
    canifier.setGeneralOutput(2, True, True)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_setGeneralOutputs(canifier):
    canifier.setGeneralOutputs(2, 1)


def test_canifier_getGeneralInputs(ctre, canifier):
    pin_values = ctre.canifier.PinValues()
    canifier.getGeneralInputs(pin_values)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_getGeneralInput(canifier):
    canifier.getGeneralInput(2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_getLastError(canifier):
    canifier.getLastError()


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_setPWMOutput(canifier):
    canifier.setPWMOutput(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_enablePWMOutput(canifier):
    canifier.enablePWMOutput(2, True)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_getPWMInput(canifier):
    retcode, inputs = canifier.getPWMInput(2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_configSetCustomParam(canifier):
    canifier.configSetCustomParam(1, 2, 3)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_configGetCustomParam(canifier):
    canifier.configGetCustomParam(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_configSetParameter(canifier):
    canifier.configSetParameter(1, 2, 3, 4, 5)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_configGetParameter(canifier):
    canifier.configGetParameter(1, 2, 3)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_setStatusFramePeriod(canifier):
    canifier.setStatusFramePeriod(1, 2, 3)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_getStatusFramePeriod(canifier):
    canifier.getStatusFramePeriod(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_setControlFramePeriod(canifier):
    canifier.setControlFramePeriod(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_getFirmwareVersion(canifier):
    canifier.getFirmwareVersion()


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_hasResetOccurred(canifier):
    canifier.hasResetOccurred()


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_getFaults(canifier):
    toFill = MagicMock()
    canifier.getFaults(toFill)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_getStickyFaults(canifier):
    toFill = MagicMock()
    canifier.getStickyFaults(toFill)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_clearStickyFaults(canifier):
    canifier.clearStickyFaults(1)


@pytest.mark.xfail(raises=NotImplementedError)
def test_canifier_getBusVoltage(canifier):
    canifier.getBusVoltage()


