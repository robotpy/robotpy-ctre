# validated: 2018-01-14 DV f0e94123427a java/src/com/ctre/phoenix/motorcontrol/can/BaseMotorController.java
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
import typing
from .sensorcollection import SensorCollection
from .trajectorypoint import TrajectoryPoint
from ._impl import (
    MotController,
    ControlMode,
    NeutralMode,
    FeedbackDevice,
    StatusFrame,
    StatusFrameEnhanced,
    VelocityMeasPeriod,
    RemoteLimitSwitchSource,
    LimitSwitchNormal,
    LimitSwitchSource,
    MotionProfileStatus,
    Faults,
    StickyFaults,
    ParamEnum,
)


__all__ = ["BaseMotorController"]


class BaseMotorController(MotController):
    """Base motor controller features for all CTRE CAN motor controllers."""
    
    ControlMode = ControlMode
    FeedbackDevice = FeedbackDevice
    LimitSwitchNormal = LimitSwitchNormal
    LimitSwitchSource = LimitSwitchSource
    NeutralMode = NeutralMode
    ParamEnum = ParamEnum
    RemoteLimitSwitchSource = RemoteLimitSwitchSource
    StatusFrame = StatusFrame
    StatusFrameEnhanced = StatusFrameEnhanced
    VelocityMeasPeriod = VelocityMeasPeriod

    def __init__(self, arbId: int):
        """
        Constructor for motor controllers.
        
        :param arbId:
        """
        super().__init__()

        self._create1(arbId)
        self.arbId = arbId
        self.sensorColl = SensorCollection(self)
        self.motionProfStats = [0] * 9
        self.controlMode = ControlMode.PercentOutput
        self.sendMode = ControlMode.PercentOutput

    def getDeviceID(self):
        """
        Returns the Device ID
        
        :returns: Device number.
        """
        return self.getDeviceNumber()

    def set(self, mode: ControlMode, demand0: float, demand1: float = 0.0):
        """
        Sets the appropriate output on the talon, depending on the mode.

        :param mode:
            The output mode to apply.
        :param demand0:
            The output value to apply. such as advanced feed forward and/or cascaded close-looping in firmware.

            In :attr:`.ControlMode.PercentOutput`, the output is between -1.0 and 1.0, with 0.0 as
            stopped.
            
            In :attr:`.ControlMode.Voltage` mode, output value is in volts.
            
            In :attr:`.ControlMode.Current` mode, output value is in amperes.
            
            In :attr:`.ControlMode.Speed` mode, output value is in position change / 100ms.
            
            In :attr:`.ControlMode.Position` mode, output value is in encoder ticks or an analog value, depending on the sensor.
            
            In :attr:`.ControlMode.Follower` mode, the output value is the integer device ID of the talon to duplicate.
        :type demand0: float
        :param demand1:
            Supplemental value.  This will also be control mode specific for future features.
        :type demand1: float

        see :meth:`.selectProfileSlot` to choose between the two sets of gains.
        """
        self.controlMode = mode
        self.sendMode = mode

        if self.controlMode == ControlMode.PercentOutput:
            self.setDemand(self.sendMode, int(1023 * demand0), 0)
        elif self.controlMode == ControlMode.Follower:
            # did caller specify device ID
            if 0 <= demand0 <= 62:
                work = self.getBaseID()
                work >>= 16
                work <<= 8
                work |= int(demand0) & 0xFF
            else:
                work = int(demand0)
            self.setDemand(self.sendMode, work, 0)
        elif self.controlMode in [ControlMode.Velocity, ControlMode.Position, ControlMode.MotionMagic, ControlMode.MotionMagicArc, ControlMode.MotionProfile]:
            self.setDemand(self.sendMode, int(demand0), 0)
        elif self.controlMode == ControlMode.Current:
            self.setDemand(self.sendMode, int(1000. * demand0), 0) # milliamps
        else:
            self.setDemand(self.sendMode, 0, 0)

    def neutralOutput(self):
        """
        Neutral the motor output by setting control mode to disabled."""
        self.set(ControlMode.Disabled, 0, 0)

    def setInverted(self, invert: bool):
        """
        Inverts the hbridge output of the motor controller.

        This does not impact sensor phase and should not be used to correct sensor polarity.

        This will invert the hbridge output but NOT the LEDs.
        This ensures....

        - Green LEDs always represents positive request from robot-controller/closed-looping mode.
        - Green LEDs correlates to forward limit switch.
        - Green LEDs correlates to forward soft limit.
        
        :param invert:
            Invert state to set.
        """
        self.invert = invert
        super().setInverted(invert)

    def getInverted(self):
        """:returns: invert setting of motor output"""
        return self.invert

    def getMotorOutputVoltage(self):
        """:returns: applied voltage to motor in volts"""
        return self.getBusVoltage() * self.getMotorOutputPercent()

    def getMotionProfileStatus(self) -> MotionProfileStatus:
        """
        Retrieve all status information.
        For best performance, Caller can snapshot all status information regarding the
        motion profile executer.
        """
        fields = super()._getMotionProfileStatus_2()
        statusToFill = MotionProfileStatus(*fields)
        return statusToFill

    def pushMotionProfileTrajectory(self, trajPt: TrajectoryPoint):
        """Push another trajectory point into the top level buffer (which is emptied
        into the motor controller's bottom buffer as room allows).

        :param trajPt: to push into buffer.
            The members should be filled in with these values...

            position:  servo position in sensor units.
            velocity:  velocity to feed-forward in sensor units per 100ms.
            profileSlotSelect:  which slot to pull PIDF gains from.  Currently
            supports 0,1,2,3.

            isLastPoint:  set to nonzero to signal motor controller to keep processing this
                trajectory point, instead of jumping to the next one
                when timeDurMs expires.  Otherwise MP executer will
                eventually see an empty buffer after the last point
                expires, causing it to assert the IsUnderRun flag.
                However this may be desired if calling application
                never wants to terminate the MP.
            zeroPos:  set to nonzero to signal motor controller to "zero" the selected
                position sensor before executing this trajectory point.
                Typically the first point should have this set only thus
                allowing the remainder of the MP positions to be relative to
                zero.
        :returns: CTR_OKAY if trajectory point push ok. ErrorCode if buffer is
            full due to kMotionProfileTopBufferCapacity.
        """
        return super()._pushMotionProfileTrajectory_2(
                trajPt.position, trajPt.velocity, trajPt.headingDeg,
                trajPt.profileSlotSelect0, trajPt.profileSlotSelect1,
                trajPt.isLastPoint, trajPt.zeroPos, trajPt.timeDur
        )

    def getFaults(self) -> typing.Tuple[int, Faults]:
        '''Gets the last error generated by this object. Not all functions return an
        error code but can potentially report errors. This function can be used
        to retrieve those error codes.

        :returns: Last Error Code generated by a function, faults
        '''
        errcode, bits = super().getFaults()
        return errcode, Faults(bits)

    def getStickyFaults(self) -> typing.Tuple[int, StickyFaults]:
        """
        Polls the various sticky fault flags.
        
        :returns: Last Error Code generated by a function, sticky faults
        """
        _, bits = super().getStickyFaults()
        return self.getLastError(), StickyFaults(bits)

    def getBaseID(self) -> int:
        return self.arbId

    def follow(self, masterToFollow: 'BaseMotorController'):
        """
        Set the control mode and output value so that this motor controller will
        follow another motor controller. Currently supports following Victor SPX
        and Talon SRX.
        """
        id32 = masterToFollow.getBaseID()
        id24 = id32
        id24 >>= 16
        id24 = id24 & 0xFFFF
        id24 <<= 8
        id24 |= (id32 & 0xFF)
        self.set(ControlMode.Follower, id24)

    def valueUpdated(self):
        """
        When master makes a device, this routine is called to signal the update."""
        pass
        
    def getSensorCollection(self) -> SensorCollection:
        """
        :returns: object that can get/set individual raw sensor values."""
        return self.sensorColl
        
    def getControlMode(self) -> ControlMode:
        """
        :returns: control mode motor controller is in"""
        return self.controlMode
