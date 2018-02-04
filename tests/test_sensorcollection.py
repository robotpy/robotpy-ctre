import pytest


@pytest.fixture(scope='function')
def sensorcollection(ctre):
    talon = ctre.WPI_TalonSRX(1)
    sensorcollection = talon.getSensorCollection()
    return sensorcollection


def test_sensorcollection_getAnalogIn(sensorcollection):
    sensorcollection.getAnalogIn()


def test_sensorcollection_setAnalogPosition(sensorcollection):
    sensorcollection.setAnalogPosition(1, 2)


def test_sensorcollection_getAnalogInRaw(sensorcollection):
    sensorcollection.getAnalogInRaw()


def test_sensorcollection_getAnalogInVel(sensorcollection):
    sensorcollection.getAnalogInVel()


def test_sensorcollection_getQuadraturePosition(sensorcollection):
    sensorcollection.getQuadraturePosition()


def test_sensorcollection_setQuadraturePosition(sensorcollection):
    sensorcollection.setQuadraturePosition(1, 2)


def test_sensorcollection_getQuadratureVelocity(sensorcollection):
    sensorcollection.getQuadratureVelocity()


def test_sensorcollection_getPulseWidthPosition(sensorcollection):
    sensorcollection.getPulseWidthPosition()


def test_sensorcollection_setPulseWidthPosition(sensorcollection):
    sensorcollection.setPulseWidthPosition(1, 2)


def test_sensorcollection_getPulseWidthVelocity(sensorcollection):
    sensorcollection.getPulseWidthVelocity()


def test_sensorcollection_getPulseWidthRiseToFallUs(sensorcollection):
    sensorcollection.getPulseWidthRiseToFallUs()


def test_sensorcollection_getPulseWidthRiseToRiseUs(sensorcollection):
    sensorcollection.getPulseWidthRiseToRiseUs()


def test_sensorcollection_getPinStateQuadA(sensorcollection):
    sensorcollection.getPinStateQuadA()


def test_sensorcollection_getPinStateQuadB(sensorcollection):
    sensorcollection.getPinStateQuadB()


def test_sensorcollection_getPinStateQuadIdx(sensorcollection):
    sensorcollection.getPinStateQuadIdx()


def test_sensorcollection_isFwdLimitSwitchClosed(sensorcollection):
    sensorcollection.isFwdLimitSwitchClosed()


def test_sensorcollection_isRevLimitSwitchClosed(sensorcollection):
    sensorcollection.isRevLimitSwitchClosed()
