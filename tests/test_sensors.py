import phoenix5.sensors


def test_pigeon():
    imu = phoenix5.sensors.PigeonIMU(0)
    imu.getFusedHeading()
