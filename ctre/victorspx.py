# validated: 2018-01-05 EN d376a57d7f94 java/src/com/ctre/phoenix/motorcontrol/can/VictorSPX.java
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
from .basemotorcontroller import BaseMotorController


__all__ = ['VictorSPX']


class VictorSPX (BaseMotorController):
    """VEX Victor SPX Motor Controller when used on CAN Bus.
    
    Don't use this directly, use :class:`.WPI_VictorSPX`"""

    def __init__(self, deviceNumber: int):
        """Constructor

        :param deviceNumber:
            [0,62]
        """
        super().__init__(deviceNumber | 0x01040000)
        hal.report(hal.UsageReporting.kResourceType_CTRE_future1, deviceNumber + 1)
