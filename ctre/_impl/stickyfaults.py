# validated: 2018-01-06 EN d090f9cdc6a1 libraries/driver/include/ctre/phoenix/MotorControl/StickyFaults.h
from .faultsbase import FaultsBase

__all__ = ['StickyFaults']


class StickyFaults(FaultsBase):
    fields = ['underVoltage', 'forwardLimitSwitch', 'reverseLimitSwitch', 'forwardSoftLimit', 'reverseSoftLimit',
              'resetDuringEn', 'sensorOverflow', 'sensorOutOfPhase', 'hardwareESDReset', 'remoteLossOfSignal']