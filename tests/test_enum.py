
# Ensure that our enum renaming works correctly

def test_enum(ctre):
    
    from ctre._impl.autogen import ctre_sim_enums as e
    
    # Prefix removal
    assert e.PigeonIMU_StatusFrame.CondStatus_1_General == 0X042000
    
    # Number stuff
    assert e.TrajectoryDuration.T0ms == 0
    
