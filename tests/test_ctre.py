import phoenix5


def test_wpi_talonsrx():
    m = phoenix5.WPI_TalonSRX(0)
    m.setNeutralMode(phoenix5.NeutralMode.Brake)
    m.set(0.5)
    assert m.get() == 0.5
    del m


def test_wpi_victorspx():
    m = phoenix5.WPI_VictorSPX(2)
    m.setNeutralMode(phoenix5.NeutralMode.Brake)
    m.set(0.5)
    assert m.get() == 0.5
    del m


def test_follow():
    m1 = phoenix5.WPI_TalonSRX(3)
    m2 = phoenix5.WPI_VictorSPX(4)
    m2.follow(m1)
    m1.set(0.5)
    assert m1.get() == 0.5
