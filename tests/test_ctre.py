import ctre
import sys
import pytest


@pytest.mark.skipif(sys.platform == "darwin", reason="OSX CI failure")
def test_wpi_talonsrx():
    m = ctre.WPI_TalonSRX(0)
    m.setNeutralMode(ctre.NeutralMode.Brake)
    m.set(0.5)
    assert m.get() == 0.5
    del m


@pytest.mark.skipif(sys.platform == "darwin", reason="OSX CI failure")
def test_wpi_talonfx():
    m = ctre.WPI_TalonFX(1)
    m.setNeutralMode(ctre.NeutralMode.Brake)
    m.set(0.5)
    assert m.get() == 0.5
    del m


@pytest.mark.skipif(sys.platform == "darwin", reason="OSX CI failure")
def test_wpi_victorspx():
    m = ctre.WPI_VictorSPX(2)
    m.setNeutralMode(ctre.NeutralMode.Brake)
    m.set(0.5)
    assert m.get() == 0.5
    del m


@pytest.mark.skipif(sys.platform == "darwin", reason="OSX CI failure")
def test_follow():
    m1 = ctre.WPI_TalonFX(3)
    m2 = ctre.WPI_TalonFX(4)
    m2.follow(m1)
    m1.set(0.5)
    assert m1.get() == 0.5
