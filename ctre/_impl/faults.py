# validated: 2018-01-14 DV a68a0c3ebf0b libraries/driver/include/ctre/phoenix/MotorControl/Faults.h
from .faultsbase import FaultsBase


__all__ = ['Faults']


class Faults(FaultsBase):
    fields = ['underVoltage', 'forwardLimitSwitch', 'reverseLimitSwitch', 'forwardSoftLimit', 'reverseSoftLimit',
              'hardwareFailure', 'resetDuringEn', 'sensorOverflow', 'sensorOutOfPhase', 'hardwareESDReset',
              'remoteLossOfSignal']