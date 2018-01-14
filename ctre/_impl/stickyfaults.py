# validated: 2018-01-14 DV a68a0c3ebf0b libraries/driver/include/ctre/phoenix/MotorControl/StickyFaults.h
from .faultsbase import FaultsBase

__all__ = ['StickyFaults']


class StickyFaults(FaultsBase):
    fields = ['underVoltage', 'forwardLimitSwitch', 'reverseLimitSwitch', 'forwardSoftLimit', 'reverseSoftLimit',
              'resetDuringEn', 'sensorOverflow', 'sensorOutOfPhase', 'hardwareESDReset', 'remoteLossOfSignal']