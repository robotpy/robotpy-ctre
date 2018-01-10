import pytest


@pytest.fixture(scope='function')
def sensorcollection(ctre):
    talon = ctre.WPI_TalonSRX(1)
    sensorcollection = talon.getSensorCollection()
    return sensorcollection


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_getAnalogIn(sensorcollection):
    sensorcollection.getAnalogIn()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_setAnalogPosition(sensorcollection):
    sensorcollection.setAnalogPosition(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_getAnalogInRaw(sensorcollection):
    sensorcollection.getAnalogInRaw()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_getAnalogInVel(sensorcollection):
    sensorcollection.getAnalogInVel()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_getQuadraturePosition(sensorcollection):
    sensorcollection.getQuadraturePosition()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_setQuadraturePosition(sensorcollection):
    sensorcollection.setQuadraturePosition(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_getQuadratureVelocity(sensorcollection):
    sensorcollection.getQuadratureVelocity()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_getPulseWidthPosition(sensorcollection):
    sensorcollection.getPulseWidthPosition()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_setPulseWidthPosition(sensorcollection):
    sensorcollection.setPulseWidthPosition(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_getPulseWidthVelocity(sensorcollection):
    sensorcollection.getPulseWidthVelocity()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_getPulseWidthRiseToFallUs(sensorcollection):
    sensorcollection.getPulseWidthRiseToFallUs()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_getPulseWidthRiseToRiseUs(sensorcollection):
    sensorcollection.getPulseWidthRiseToRiseUs()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_getPinStateQuadA(sensorcollection):
    sensorcollection.getPinStateQuadA()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_getPinStateQuadB(sensorcollection):
    sensorcollection.getPinStateQuadB()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_getPinStateQuadIdx(sensorcollection):
    sensorcollection.getPinStateQuadIdx()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_isFwdLimitSwitchClosed(sensorcollection):
    sensorcollection.isFwdLimitSwitchClosed()


@pytest.mark.xfail(raises=NotImplementedError)
def test_sensorcollection_isRevLimitSwitchClosed(sensorcollection):
    sensorcollection.isRevLimitSwitchClosed()
