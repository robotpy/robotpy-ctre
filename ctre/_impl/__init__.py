
import hal

if hal.isSimulation():
    from .autogen.canifier_sim import CANifier
    from .autogen.motcontroller_sim import MotController
    from .autogen.pigeonimu_sim import PigeonIMU
else:
    from .ctre_roborio import (
        CANifier,
        MotController,
        PigeonIMU
    )
