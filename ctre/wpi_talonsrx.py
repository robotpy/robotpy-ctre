# validated: 2018-01-05 EN 46d3d290a0b2 java/src/com/ctre/phoenix/motorcontrol/can/WPI_TalonSRX.java
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

from .talonsrx import TalonSRX
from ._impl import ControlMode


class WPI_TalonSRX(TalonSRX, SendableBase, MotorSafety):
    """WPI Compliant motor controller class.
        WPILIB's object model requires many interfaces to be implemented to use
        the various features.  This includes...

        - Software PID loops running in the robot controller
        - LiveWindow/Test mode features
        - Motor Safety (auto-turn off of motor if Set stops getting called)
        - Single Parameter set that assumes a simple motor controller.
    """

    def __init__(self, deviceNumber):
        super().__init__(deviceNumber)
        hal.report(hal.UsageReporting.kResourceType_CTRE_future2, deviceNumber + 1)

        self.description = "Talon SRX %s" % (deviceNumber,)

        MotorSafety.__init__(self)
        self.setExpiration(0.0)
        self.setSafetyEnabled(False)

        SendableBase.__init__(self)
        self.setName("Talon SRX ", deviceNumber)
        self.speed = 0.0

    def pidWrite(self, output: float):
        self.set(output)

    def get(self):
        """Common interface for getting the current set speed of a speed controller.

        :returns: The current set speed. Value is between -1.0 and 1.0.
        """
        return self.speed

    def set(self, *args, **kwargs):
        """
        Can be called either with a single unnamed parameter representing the
        percentage of output, or with up to 4 arguments:
        
        :param mode:
            The output mode to apply.
        :param demand0:
            The output value to apply. such as advanced feed forward and/or auxiliary close-looping in firmware.

            In :attr:`.ControlMode.PercentOutput`, the output is between -1.0 and 1.0, with 0.0 as
            stopped.
            
            In :attr:`.ControlMode.Voltage` mode, output value is in volts.
            
            In :attr:`.ControlMode.Current` mode, output value is in amperes.
            
            In :attr:`.ControlMode.Speed` mode, output value is in position change / 100ms.
            
            In :attr:`.ControlMode.Position` mode, output value is in encoder ticks or an analog value, depending on the sensor.
            
            In :attr:`.ControlMode.Follower` mode, the output value is the integer device ID of the talon to duplicate.
        :param demand1Type:
            The demand type for demand1.
            
            * Neutral: Ignore demand1 and apply no change to the demand0 output.
            * AuxPID: Use demand1 to set the target for the auxiliary PID 1.
            * ArbitraryFeedForward: Use demand1 as an arbitrary additive value to the
              demand0 output.  In PercentOutput the demand0 output is the motor output,
              and in closed-loop modes the demand0 output is the output of PID0.
        :param demand1:
            Supplemental value.  This will also be control mode specific for future features.
        """
        if len(args) == 1:
            self.speed = args[0]
            args = (ControlMode.PercentOutput, self.speed)
        else:
            self.speed = 0
        
        super().set(*args, **kwargs)
        self.feed()
            
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
