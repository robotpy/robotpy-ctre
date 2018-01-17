# validated: 2018-01-05 EN 8f8595a20145 java/src/com/ctre/phoenix/CANifier.java
#----------------------------------------------------------------------------
#  Software License Agreement
#
# Copyright (C) Cross The Road Electronics.  All rights
# reserved.
# 
# Cross The Road Electronics (CTRE) licenses to you the right to 
# use, publish, and distribute copies of CRF (Cross The Road) firmware files (*.crf) and Software
# API Libraries ONLY when in use with Cross The Road Electronics hardware products.
# 
# THE SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT
# WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT
# LIMITATION, ANY WARRANTY OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT SHALL
# CROSS THE ROAD ELECTRONICS BE LIABLE FOR ANY INCIDENTAL, SPECIAL, 
# INDIRECT OR CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF
# PROCUREMENT OF SUBSTITUTE GOODS, TECHNOLOGY OR SERVICES, ANY CLAIMS
# BY THIRD PARTIES (INCLUDING BUT NOT LIMITED TO ANY DEFENSE
# THEREOF), ANY CLAIMS FOR INDEMNITY OR CONTRIBUTION, OR OTHER
# SIMILAR COSTS, WHETHER ASSERTED ON THE BASIS OF CONTRACT, TORT
# (INCLUDING NEGLIGENCE), BREACH OF WARRANTY, OR OTHERWISE
#----------------------------------------------------------------------------
import enum
import hal

from ._impl import (
    GeneralPin,
    ParamEnum,
    CANifierStatusFrame,
    CANifierControlFrame,
    CANifierFaults,
    CANifierStickyFaults,
    CANifier as CANifierImpl,
)


__all__ = ['CANifier']


class PinValues:
    """Class to hold the pin values."""
    def __init__(self):
        self.QUAD_IDX = False
        self.QUAD_B = False
        self.QUAD_A = False
        self.LIMR = False
        self.LIMF = False
        self.SDA = False
        self.SCL = False
        self.SPI_CS_PWM3 = False
        self.SPI_MISO_PWM2 = False
        self.SPI_MOSI_PWM1 = False
        self.SPI_CLK_PWM0 = False


class CANifier(CANifierImpl):
    """CTRE CANifier
        
    Device for interfacing common devices to the CAN bus.
    """
    
    ControlFrame = CANifierControlFrame
    StatusFrame = CANifierStatusFrame
    
    Faults = CANifierFaults
    StickyFaults = CANifierStickyFaults

    class LEDChannel(enum.IntEnum):
        """Enum for the LED Output Channels"""
        A = 0
        B = 1
        C = 2

    class PWMChannel(enum.IntEnum):
        """Enum for the PWM Input Channels"""
        C0 = 0
        C1 = 1
        C2 = 2
        C3 = 3

    PWMChannelCount = len(PWMChannel)

    GeneralPin = GeneralPin

    def __init__(self, deviceId: int):
        """
        Constructor.

        :param deviceId: The CAN Device ID of the CANifier.
        """
        super().__init__()
        self._create1(deviceId)
        # python-specific: tempPins not needed
        hal.report(hal.UsageReporting.kResourceType_CANifier, deviceId + 1)

    def setLEDOutput(self, percentOutput: float, ledChannel: LEDChannel):
        """
        Sets the LED Output

        :param percentOutput: Output duty cycle expressed as percentage.
        :param ledChannel: Channel to set the output of.
        """
        if percentOutput > 1:
            percentOutput = 1
        if percentOutput < 0:
            percentOutput = 0
        dutyCycle = int(percentOutput * 1023) # [0,1023]

        super().setLEDOutput(dutyCycle, ledChannel)

    def getGeneralInputs(self, allPins: PinValues):
        """
        Gets the state of all General Pins

        :param allPins: A structure to fill with the current state of all pins.
        """
        _, tempPins = super().getGeneralInputs()
        allPins.LIMF = tempPins[GeneralPin.LIMF]
        allPins.LIMR = tempPins[GeneralPin.LIMR]
        allPins.QUAD_A = tempPins[GeneralPin.QUAD_A]
        allPins.QUAD_B = tempPins[GeneralPin.QUAD_B]
        allPins.QUAD_IDX = tempPins[GeneralPin.QUAD_IDX]
        allPins.SCL = tempPins[GeneralPin.SCL]
        allPins.SDA = tempPins[GeneralPin.SDA]
        allPins.SPI_CLK_PWM0 = tempPins[GeneralPin.SPI_CLK_PWM0P]
        allPins.SPI_MOSI_PWM1 = tempPins[GeneralPin.SPI_MOSI_PWM1P]
        allPins.SPI_MISO_PWM2 = tempPins[GeneralPin.SPI_MISO_PWM2P]
        allPins.SPI_CS_PWM3 = tempPins[GeneralPin.SPI_CS]

    def setPWMOutput(self, pwmChannel: int, dutyCycle: float):
        """
        Sets the PWM Output
        Currently supports PWM 0, PWM 1, and PWM 2

        :param pwmChannel: Index of the PWM channel to output.
        :param dutyCycle: Duty Cycle (0 to 1) to output.  Default period of the signal is 4.2 ms.
        """
        dutyCycle = max(dutyCycle, 0)
        dutyCycle = min(dutyCycle, 1)
        pwmChannel = max(pwmChannel, 0)

        dutyCyc10bit = int(1023 * dutyCycle)

        super().setPWMOutput(pwmChannel, dutyCyc10bit)

    def enablePWMOutput(self, pwmChannel: int, bEnable: bool):
        """
        Enables PWM Outputs
        Currently supports PWM 0, PWM 1, and PWM 2

        :param pwmChannel: Index of the PWM channel to enable.
        :param bEnable: True" enables output on the pwm channel.
        """
        pwmChannel = max(pwmChannel, 0)
        super().enablePWMOutput(pwmChannel, bEnable)

    def getFaults(self, toFill: CANifierFaults):
        """
        Gets the CANifier fault status
        
        :param toFill:
            Container for fault statuses.
        :returns: Error Code generated by function. 0 indicates no error.
        """
        _, bits = super().getFaults()
        toFill.update(bits)
        return self.getLastError()

    def getStickyFaults(self, toFill: CANifierStickyFaults):
        """
        Gets the CANifier sticky fault status

        :param toFill:
            Container for sticky fault statuses.
        :returns: Error Code generated by function. 0 indicates no error.
        """
        _, bits = super().getStickyFaults()
        toFill.update(bits)
        return self.getLastError()
