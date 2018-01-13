# validated: 2018-01-06 EN d090f9cdc6a1 libraries/driver/include/ctre/phoenix/MotorControl/Faults.h
from .faultsbase import FaultsBase


__all__ = ['Faults']


class Faults(FaultsBase):
    fields = ['underVoltage', 'forwardLimitSwitch', 'reverseLimitSwitch', 'forwardSoftLimit', 'reverseSoftLimit',
              'hardwareFailure', 'resetDuringEn', 'sensorOverflow', 'sensorOutOfPhase', 'hardwareESDReset',
              'remoteLossOfSignal']