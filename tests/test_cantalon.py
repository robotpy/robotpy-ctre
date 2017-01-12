
import ctre
from hal_impl.data import hal_data

import pytest

@pytest.fixture(scope='function')
def cantalon_and_data():
    ct = ctre.CANTalon(2)

    
    data = hal_data['CAN'][2]
    return ct, data


def test_ct_basic(cantalon_and_data):
    ct, data = cantalon_and_data
    
    assert data['mode_select'] == ctre.CANTalon.ControlMode.Disabled
    ct.set(0)
    
    assert data['mode_select'] == ctre.CANTalon.ControlMode.PercentVbus
    assert ct.get() == 0
    
    ct.set(1)
    assert ct.get() == 1
    
    ct.setInverted(True)
    ct.set(1)
    assert ct.get() == -1
    
    # test P/I/D setting
    for i in [0, 1]:
        ct.setProfile(i)
        idx = i*4
        
        ct.setP(idx+1)
        assert data['profile%s_p' % i] == idx+1
        assert ct.getP() == idx+1
        
        ct.setI(idx+2)
        assert data['profile%s_i' % i] == idx+2
        assert ct.getI() == idx+2
        
        ct.setD(idx+3)
        assert data['profile%s_d' % i] == idx+3
        assert ct.getD() == idx+3
        
        ct.setF(idx+4)
        assert data['profile%s_f' % i] == idx+4
        assert ct.getF() == idx+4
        
    # Limit switches
    data['limit_switch_closed_for'] = 0
    assert ct.isFwdLimitSwitchClosed() == True
    
    data['limit_switch_closed_for'] = 1
    assert ct.isFwdLimitSwitchClosed() == False
    
    data['limit_switch_closed_rev'] = 0
    assert ct.isRevLimitSwitchClosed() == True
    
    data['limit_switch_closed_rev'] = 1
    assert ct.isRevLimitSwitchClosed() == False
    
    
    # test direct sensor positions, velocities
    # encoder
    data['enc_position'] = 1
    data['enc_velocity'] = 2
    assert ct.getEncPosition() == 1
    assert ct.getEncVelocity() == 2
    
    ct.setEncPosition(11)
    assert ct.getEncPosition() == 11
    
    # analog
    data['analog_in_position'] = 3
    data['analog_in_velocity'] = 4
    assert ct.getAnalogInPosition() == 3
    assert ct.getAnalogInVelocity() == 4
    
    ct.setAnalogPosition(33)
    assert ct.getAnalogInPosition() == 33
    
    # pulse width device
    data['pulse_width_position'] = 6
    data['pulse_width_velocity'] = 7
    assert ct.getPulseWidthPosition() == 6
    assert ct.getPulseWidthVelocity() == 7
    
    ct.setPulseWidthPosition(66)
    assert ct.getPulseWidthPosition() == 66
    
    # test sensor position by selecting feedback device
    ct.setFeedbackDevice(ctre.CANTalon.FeedbackDevice.QuadEncoder)
    assert ct.getPosition() == 11
    
    ct.setFeedbackDevice(ctre.CANTalon.FeedbackDevice.AnalogPot)
    assert ct.getPosition() == 33
    
    ct.setFeedbackDevice(ctre.CANTalon.FeedbackDevice.PulseWidth)
    assert abs(ct.getPosition() - (66/ctre.CANTalon.kNativePwdUnitsPerRotation)) < 0.001
    
    # test motion profile thing
    traj = ctre.CANTalon.TrajectoryPoint()
    
    ct.pushMotionProfileTrajectory(traj)
    
    status = ctre.CANTalon.MotionProfileStatus()
    ct.getMotionProfileStatus(status)
    
    
    