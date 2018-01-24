# validated: 2018-01-05 EN 2d574139d4e2 java/src/com/ctre/phoenix/motorcontrol/SensorCollection.java
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
from ._impl import MotController


__all__ = ["SensorCollection"]


class SensorCollection:

    def __init__(self, motorController):
        """
        :type motorController: :class:`.BaseMotorController`"""
        self.motorController = motorController

    @property
    def impl(self):
        return self.motorController

    @property
    def handle(self):
        return self.motorController.handle

    def getAnalogIn(self) -> int:
        return self.impl.getAnalogIn()

    def setAnalogPosition(self, newPosition: int, timeoutMs: int):
        return self.impl.setAnalogPosition(newPosition, timeoutMs)

    def getAnalogInRaw(self) -> int:
        return self.impl.getAnalogInRaw()

    def getAnalogInVel(self) -> int:
        return self.impl.getAnalogInVel()

    def getQuadraturePosition(self) -> int:
        return self.impl.getQuadraturePosition()

    def setQuadraturePosition(self, newPosition: int, timeoutMs: int):
        return self.impl.setQuadraturePosition(newPosition, timeoutMs)

    def getQuadratureVelocity(self) -> int:
        return self.impl.getQuadratureVelocity()

    def getPulseWidthPosition(self) -> int:
        return self.impl.getPulseWidthPosition()

    def setPulseWidthPosition(self, newPosition: int, timeoutMs: int):
        return self.impl.setPulseWidthPosition(newPosition, timeoutMs)

    def getPulseWidthVelocity(self) -> int:
        return self.impl.getPulseWidthVelocity()

    def getPulseWidthRiseToFallUs(self) -> int:
        return self.impl.getPulseWidthRiseToFallUs()

    def getPulseWidthRiseToRiseUs(self) -> int:
        return self.impl.getPulseWidthRiseToRiseUs()

    def getPinStateQuadA(self) -> bool:
        """
        Gets pin state quad a.

        :returns: the pin state quad a (1 if asserted, 0 if not asserted).
        """
        return self.impl.getPinStateQuadA() != 0

    def getPinStateQuadB(self) -> bool:
        """
        Gets pin state quad b.

        :returns: Digital level of QUADB pin (1 if asserted, 0 if not asserted).
        """
        return self.impl.getPinStateQuadB() != 0

    def getPinStateQuadIdx(self) -> bool:
        """
        Gets pin state quad index.

        :returns: Digital level of QUAD Index pin (1 if asserted, 0 if not asserted).
        """
        return self.impl.getPinStateQuadIdx() != 0

    def isFwdLimitSwitchClosed(self) -> bool:
        """
        Is forward limit switch closed.

        This function works regardless if limit switch feature is
        enabled.

        :returns: True iff forward limit switch is closed, False iff switch is open.
        """
        return self.impl.isFwdLimitSwitchClosed() != 0

    def isRevLimitSwitchClosed(self) -> bool:
        """
        Is reverse limit switch closed.

        This function works regardless if limit switch feature is
        enabled.

        :returns: True iff reverse limit switch is closed, False iff switch is open.
        """
        return self.impl.isRevLimitSwitchClosed() != 0
