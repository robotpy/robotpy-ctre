import pytest


@pytest.fixture(scope='function')
def pigeon(ctre):
    return ctre.PigeonIMU(1)


def test_pigeon_init(ctre):
    ctre.PigeonIMU(1)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_setYaw(pigeon):
    pigeon.setYaw(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_addYaw(pigeon):
    pigeon.addYaw(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_setYawToCompass(pigeon):
    pigeon.setYawToCompass(1)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_setFusedHeading(pigeon):
    pigeon.setFusedHeading(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_addFusedHeading(pigeon):
    pigeon.addFusedHeading(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_setFusedHeadingToCompass(pigeon):
    pigeon.setFusedHeadingToCompass(1)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_setAccumZAngle(pigeon):
    pigeon.setAccumZAngle(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_configTemperatureCompensationEnable(pigeon):
    pigeon.configTemperatureCompensationEnable(True, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_setCompassDeclination(pigeon):
    pigeon.setCompassDeclination(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_setCompassAngle(pigeon):
    pigeon.setCompassAngle(1, 2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_enterCalibrationMode(pigeon, ctre):
    pigeon.enterCalibrationMode(ctre.pigeonimu.CalibrationMode.Temperature, 1)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getGeneralStatus(pigeon, ctre):
    generalStatus = pigeon.getGeneralStatus()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getLastError(pigeon):
    pigeon.getLastError()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_get6dQuaternion(pigeon):
    retcode, qt = pigeon.get6dQuaternion()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getYawPitchRoll(pigeon):
    retcode, angles = pigeon.getYawPitchRoll()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getAccumGyro(pigeon):
    retcode, angles = pigeon.getAccumGyro()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getAbsoluteCompassHeading(pigeon):
    pigeon.getAbsoluteCompassHeading()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getCompassHeading(pigeon):
    pigeon.getCompassHeading()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getCompassFieldStrength(pigeon):
    pigeon.getCompassFieldStrength()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getTemp(pigeon):
    pigeon.getTemp()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getState(pigeon):
    pigeon.getState()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getUpTime(pigeon):
    pigeon.getUpTime()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getRawMagnetometer(pigeon):
    retcode, angles = pigeon.getRawMagnetometer()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getBiasedMagnetometer(pigeon):
    retcode, angles = pigeon.getBiasedMagnetometer()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getBiasedAccelerometer(pigeon):
    retcode, angles = pigeon.getBiasedAccelerometer()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getRawGyro(pigeon):
    retcode, angles = pigeon.getRawGyro()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getAccelerometerAngles(pigeon):
    retcode, angles = pigeon.getAccelerometerAngles()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getFusedHeading1(pigeon):
    pigeon.getFusedHeading()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getFusedHeading2(pigeon, ctre):
    fusionStatus = pigeon.getFusedHeading()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getFirmwareVersion(pigeon):
    pigeon.getFirmwareVersion()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_hasResetOccurred(pigeon):
    pigeon.hasResetOccurred()


@pytest.mark.xfail(raises=AttributeError)
def test_pigeon_configSetCustomParam(pigeon):
    pigeon.configSetCustomParam(1,2,3)


@pytest.mark.xfail(raises=AttributeError)
def test_pigeon_configGetCustomParam(pigeon):
    pigeon.configGetCustomParam(1,2)


@pytest.mark.xfail(raises=AttributeError)
def test_pigeon_configSetParameter(pigeon):
    pigeon.configSetParameter(1,2,3,4,5)


@pytest.mark.xfail(raises=AttributeError)
def test_pigeon_configGetParameter(pigeon):
    pigeon.configGetParameter(1,2,3)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_setStatusFramePeriod(pigeon):
    pigeon.setStatusFramePeriod(1,2,3)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getStatusFramePeriod(pigeon):
    pigeon.getStatusFramePeriod(1,2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_setControlFramePeriod(pigeon):
    pigeon.setControlFramePeriod(1,2)


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getFaults(pigeon, ctre):
    faults = pigeon.getFaults()


@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_getStickyFaults(pigeon, ctre):
    stickyfaults = pigeon.getStickyFaults()
    

@pytest.mark.xfail(raises=NotImplementedError)
def test_pigeon_clearStickyFaults(pigeon):
    pigeon.clearStickyFaults(1)


@pytest.mark.parametrize("heading, isvalid, isfusing, errnom, result", [
    (1.0, False, True, 'OK', 'Fused Heading is not valid.'),
    (1.0, True, False, 'OK', 'Fused Heading is valid.'),
    (1.0, True, True, 'OK', 'Fused Heading is valid and is fusing compass.'),
    (1.0, False, True, 'CAN_INVALID_PARAM', 'Could not receive status frame.  Check wiring and web-config.'),
    ])
def test_fusionstatus_str(ctre, heading, isvalid, isfusing, errnom, result):
    fusionstatus = ctre.pigeonimu.FusionStatus(
        bIsFusing = isfusing,
        bIsValid = isvalid,
        heading = heading,
        lastError = getattr(ctre.pigeonimu.ErrorCode, errnom),
    )
    assert str(fusionstatus) == result


@pytest.mark.parametrize("isbooting, statenom, currentmodenom, errnom, result", [
    (False, 'Ready', 'Temperature', 'CAN_INVALID_PARAM', 'Status frame was not received, check wired connections and web-based config.'),
    (True, 'Ready', 'Temperature', 'OK', 'Pigeon is boot-caling to properly bias accel and gyro.  Do not move Pigeon.  When finished biasing, calibration mode will start.'),
    (False, 'UserCalibration', 'BootTareGyroAccel', 'OK', 'Boot-Calibration: Gyro and Accelerometer are being biased.'),
    (False, 'UserCalibration', 'Temperature', 'OK', 'Temperature-Calibration: Pigeon is collecting temp data and will finish when temp range is reached. \nDo not move Pigeon.'),
    (False, 'UserCalibration', 'Magnetometer12Pt', 'OK', "Magnetometer Level 1 calibration: Orient the Pigeon PCB in the 12 positions documented in the User's Manual."),
    (False, 'UserCalibration', 'Magnetometer360', 'OK', "Magnetometer Level 2 calibration: Spin robot slowly in 360' fashion."),
    (False, 'UserCalibration', 'Accelerometer', 'OK', "Accelerometer Calibration: Pigeon PCB must be placed on a level source.  Follow User's Guide for how to level surface."),
    (False, 'UserCalibration', 'Unknown', 'OK', "Unknown status"),
    (False, 'Ready', 'Unknown', 'OK', "Pigeon is running normally.  Last CAL error code was 0."),
    (False, 'Unknown', 'Unknown', 'OK', "Not enough data to determine status."),
    ])
def test_generalstatus_str(ctre, isbooting, statenom, currentmodenom, errnom, result):
    generalstatus = ctre.pigeonimu.GeneralStatus(
        state=getattr(ctre.pigeonimu.PigeonState, statenom),
        currentMode=getattr(ctre.pigeonimu.CalibrationMode, currentmodenom),
        calibrationError=0,
        bCalIsBooting=isbooting,
        tempC=0,
        upTimeSec=0,
        noMotionBiasCount=0,
        tempCompensationCount=0,
        lastError=getattr(ctre.pigeonimu.ErrorCode, errnom),
    )
    assert str(generalstatus) == result
