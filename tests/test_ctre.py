import phoenix5
import sys
import pytest


@pytest.mark.skipif(sys.platform == "darwin", reason="OSX CI failure")
def test_wpi_talonsrx():
    m = phoenix5.WPI_TalonSRX(0)
    m.setNeutralMode(phoenix5.NeutralMode.Brake)
    m.set(0.5)
    assert m.get() == 0.5
    del m


@pytest.mark.skipif(sys.platform == "darwin", reason="OSX CI failure")
def test_wpi_talonfx():
    m = phoenix5.WPI_TalonFX(1)
    m.setNeutralMode(phoenix5.NeutralMode.Brake)
    m.set(0.5)
    assert m.get() == 0.5
    del m


@pytest.mark.skipif(sys.platform == "darwin", reason="OSX CI failure")
def test_wpi_victorspx():
    m = phoenix5.WPI_VictorSPX(2)
    m.setNeutralMode(phoenix5.NeutralMode.Brake)
    m.set(0.5)
    assert m.get() == 0.5
    del m


@pytest.mark.skipif(sys.platform == "darwin", reason="OSX CI failure")
def test_follow():
    m1 = phoenix5.WPI_TalonFX(3)
    m2 = phoenix5.WPI_TalonFX(4)
    m2.follow(m1)
    m1.set(0.5)
    assert m1.get() == 0.5
