import pytest


@pytest.fixture(scope='function')
def victor(ctre, MotController):
    return ctre.WPI_VictorSPX(1)


def test_victor_init(ctre):
    ctre.WPI_VictorSPX(1)


def test_victor_get(victor, ControlMode):
    assert victor.get() == 0


@pytest.mark.xfail(raises=NotImplementedError)
def test_victor_set1(victor, ControlMode):
    victor.set(1)
    assert victor.get() == 1
    victor.impl.setDemand.assert_called_with(victor.handle, ControlMode.PercentOutput, 1023, 0)


@pytest.mark.xfail(raises=NotImplementedError)
def test_victor_set2(victor, ControlMode):
    victor.set(ControlMode.Velocity, 1)
    assert victor.get() != 1
    victor.impl.setDemand.assert_called_with(victor.handle, ControlMode.Velocity, 1, 0)


@pytest.mark.xfail(raises=NotImplementedError)
def test_victor_set3(victor, ControlMode):
    victor.set(ControlMode.Position, 1, 55)
    assert victor.get() != 1
    victor.impl.setDemand.assert_called_with(victor.handle, ControlMode.Position, 1, 0)


@pytest.mark.xfail(raises=NotImplementedError)
def test_victor_set4(victor, ControlMode):
    victor.set(ControlMode.Current, 1.1)
    victor.impl.setDemand.assert_called_with(victor.handle, ControlMode.Current, 1100, 0)


@pytest.mark.xfail(raises=NotImplementedError)
def test_victor_disable(victor, ControlMode):
    victor.disable()
    victor.impl.setDemand.assert_called_with(victor.handle, ControlMode.Disabled, 0, 0)


@pytest.mark.xfail(raises=NotImplementedError)
def test_victor_stopMotor(victor, ControlMode):
    victor.stopMotor()
    victor.impl.setDemand.assert_called_with(victor.handle, ControlMode.Disabled, 0, 0)


@pytest.mark.xfail(raises=NotImplementedError)
def test_victor_initSendable(victor, ControlMode, sendablebuilder):
    victor.set(4)

    victor.initSendable(sendablebuilder)

    sendablebuilder.updateTable()

    assert sendablebuilder.getTable().getNumber("Value", 0.0) == 4

    sendablebuilder.properties[0].setter(3)

    assert victor.get() == 3
