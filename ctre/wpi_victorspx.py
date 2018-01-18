# validated: 2018-01-05 EN 46d3d290a0b2 java/src/com/ctre/phoenix/motorcontrol/can/WPI_VictorSPX.java
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
import hal
from wpilib import MotorSafety, LiveWindow, SendableBase
from wpilib._impl.utils import match_arglist
from .victorspx import VictorSPX
from ._impl import ControlMode


__all__ = ['WPI_VictorSPX']


class WPI_VictorSPX (VictorSPX, SendableBase, MotorSafety):
    """WPI Compliant motor controller class.
    WPILIB's object model requires many interfaces to be implemented to use
    the various features.
    This includes...

    - Software PID loops running in the robot controller
    - LiveWindow/Test mode features
    - Motor Safety (auto-turn off of motor if Set stops getting called)
    - Single Parameter set that assumes a simple motor controller.
    """

    def __init__(self, deviceNumber: int):
        super().__init__(deviceNumber)
        hal.report(hal.UsageReporting.kResourceType_CTRE_future3, deviceNumber + 1)
        self.description = "Victor SPX %s" % (deviceNumber,)

        MotorSafety.__init__(self)
        self.setExpiration(0.0)
        self.setSafetyEnabled(False)

        SendableBase.__init__(self)
        LiveWindow.add(self)
        self.setName("Victor SPX ", deviceNumber)
        self.speed = 0.0

    def set(self, *args, **kwargs):
        """
        See :meth:`.BaseMotorController.set`

        Can be called three ways:

        - speed
        - mode, value
        - mode, demand0, demand1

        largely a wrapper around :meth:`.VictorSPX.set`

        :param value:
        :type value: float
        :param mode: ControlMode.PercentOutput if not provided
        :type mode: ControlMode
        :param speed:
        :type speed: float
        :param demand0:
        :type demand0: float
        :param demand1:
        :type demand1: float
        """
        speed_arg = ("speed", [float, int])
        value_arg = ("value", [float, int])
        mode_arg = ("mode", [ControlMode])
        demand0_arg = ("demand0", [float, int])
        demand1_arg = ("demand1", [float, int])

        templates = [
            [speed_arg],
            [mode_arg, value_arg],
            [mode_arg, demand0_arg, demand1_arg]]

        index, results = match_arglist('WPI_VictorSPX.set',
                                   args, kwargs, templates)

        if index == 2:
            super().set(results['mode'], results['demand0'], results['demand1'])
        else:
            if index == 0:
                self.speed = value = results['speed']
                mode = ControlMode.PercentOutput
            elif index == 1:
                value = results['value']
                mode = results['mode']
            super().set(mode, value)

        self.feed()

    def pidWrite(self, output: float):
        self.set(output)

    def get(self) -> float:
        """Common interface for getting the current set speed of a speed controller.
        
        :returns: The current set speed. Value is between -1.0 and 1.0.
        """
        return self.speed

    #def setInverted(self, isInverted: bool):
    #    super().setInverted(isInverted)

    #def getInverted(self):
    #    return super().getInverted()

    def disable(self):
        self.neutralOutput()

    def stopMotor(self):
        """Common interface to stop the motor until :meth:`.set` is called again."""
        self.neutralOutput()

    def initSendable(self, builder):
        builder.setSmartDashboardType("Speed Controller")
        builder.setSafeState(self.stopMotor)
        builder.addDoubleProperty("Value", self.get, self.set)

    def getDescription(self):
        return self.description
