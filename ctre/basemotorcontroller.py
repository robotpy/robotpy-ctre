# validated: 2018-03-01 DS e8221da18ba9 java/src/com/ctre/phoenix/motorcontrol/can/BaseMotorController.java
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

from .sensorcollection import SensorCollection
from .trajectorypoint import TrajectoryPoint
from ._impl import (
    ControlMode,
    DemandType,
    ErrorCode,
    Faults,
    FeedbackDevice,
    FollowerType,
    LimitSwitchNormal,
    LimitSwitchSource,
    MotController,
    MotionProfileStatus,
    NeutralMode,
    ParamEnum,
    RemoteFeedbackDevice,
    RemoteLimitSwitchSource,
    RemoteSensorSource,
    StatusFrame,
    StatusFrameEnhanced,
    StickyFaults,
    VelocityMeasPeriod,
)


__all__ = ["BaseMotorController"]


class BaseMotorController(MotController):
    """Base motor controller features for all CTRE CAN motor controllers."""
    
    ControlMode = ControlMode
    DemandType = DemandType
    FeedbackDevice = FeedbackDevice
    LimitSwitchNormal = LimitSwitchNormal
    LimitSwitchSource = LimitSwitchSource
    NeutralMode = NeutralMode
    ParamEnum = ParamEnum
    RemoteFeedbackDevice = RemoteFeedbackDevice
    RemoteLimitSwitchSource = RemoteLimitSwitchSource
    RemoteSensorSource = RemoteSensorSource
    StatusFrame = StatusFrame
    StatusFrameEnhanced = StatusFrameEnhanced
    VelocityMeasPeriod = VelocityMeasPeriod

    def __init__(self, arbId: int) -> None:
        """
        Constructor for motor controllers.
        
        :param arbId:
        """
        super().__init__()

        self._create1(arbId)
        self.arbId = arbId
        self.sensorColl = SensorCollection(self)
        self.controlMode = ControlMode.PercentOutput
        self.sendMode = ControlMode.PercentOutput

    def getDeviceID(self) -> int:
        """
        Returns the Device ID
        
        :returns: Device number.
        """
        return self.getDeviceNumber()
        
    __set4_modes = {ControlMode.Velocity, ControlMode.Position, ControlMode.MotionMagic, ControlMode.MotionProfile, ControlMode.MotionProfileArc}

    def set(self, mode: ControlMode, demand0: float, demand1Type: DemandType = DemandType.Neutral, demand1: float = 0.0):
        """
        Sets the appropriate output on the talon, depending on the mode.

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
    
        Arcade Drive Example::
        
            _talonLeft.set(ControlMode.PercentOutput, joyForward, DemandType.ArbitraryFeedForward, +joyTurn)
            _talonRght.set(ControlMode.PercentOutput, joyForward, DemandType.ArbitraryFeedForward, -joyTurn)
                    
        Drive Straight Example::
                            
            # Note: Selected Sensor Configuration is necessary for both PID0 and PID1.
            _talonLeft.follow(_talonRght, FollowerType.AuxOutput1)
            _talonRght.set(ControlMode.PercentOutput, joyForward, DemandType.AuxPID, desiredRobotHeading)
                            
        Drive Straight to a Distance Example::
        
            # Note: Other configurations (sensor selection, PID gains, etc.) need to be set.
            _talonLeft.follow(_talonRght, FollowerType.AuxOutput1);
            _talonRght.set(ControlMode.MotionMagic, targetDistance, DemandType.AuxPID, desiredRobotHeading)
        
        """
        self.controlMode = mode
        self.sendMode = mode

        if self.controlMode == ControlMode.PercentOutput:
            self._set_4(self.sendMode, demand0, demand1, demand1Type)
        elif self.controlMode == ControlMode.Follower:
            # did caller specify device ID
            if 0 <= demand0 <= 62:
                work = self.getBaseID()
                work >>= 16
                work <<= 8
                work |= int(demand0) & 0xFF
            else:
                work = int(demand0)
            self._set_4(self.sendMode, work, demand1, demand1Type)
        elif self.controlMode in self.__set4_modes:
            self._set_4(self.sendMode, demand0, demand1, demand1Type)
        elif self.controlMode == ControlMode.Current:
            self.setDemand(self.sendMode, int(1000. * demand0), 0) # milliamps
        else:
            self.setDemand(self.sendMode, 0, 0)

    def neutralOutput(self):
        """Neutral the motor output by setting control mode to disabled."""
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

    def getInverted(self) -> bool:
        """:returns: invert setting of motor output"""
        return self.invert

    def getMotorOutputVoltage(self) -> float:
        """:returns: applied voltage to motor in volts"""
        return self.getBusVoltage() * self.getMotorOutputPercent()

    def getMotionProfileStatus(self) -> MotionProfileStatus:
        """
        Retrieve all status information.
        For best performance, Caller can snapshot all status information regarding the
        motion profile executer.
        """
        return MotionProfileStatus(*self._getMotionProfileStatus_2())

    def pushMotionProfileTrajectory(self, trajPt: TrajectoryPoint) -> ErrorCode:
        """Push another trajectory point into the top level buffer (which is emptied
        into the motor controller's bottom buffer as room allows).

        :param trajPt: to push into buffer.
            The members should be filled in with these values...

            position:  servo position in sensor units.
            velocity:  velocity to feed-forward in sensor units per 100ms.
            profileSlotSelect0:  Which slot to get PIDF gains. PID is used for position servo. F is used
                as the Kv constant for velocity feed-forward. Typically this is hardcoded
                to the a particular slot, but you are free gain schedule if need be.
                Choose from [0,3]
            profileSlotSelect1: Which slot to get PIDF gains for auxiliary PId.
                This only has impact during MotionProfileArc Control mode.
                Choose from [0,1].
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
            timeDur: Duration to apply this trajectory pt.
                This time unit is ADDED to the exising base time set by
                configMotionProfileTrajectoryPeriod().
        
        :returns: CTR_OKAY if trajectory point push ok. ErrorCode if buffer is
            full due to kMotionProfileTopBufferCapacity.
        """
        return self._pushMotionProfileTrajectory_2(*trajPt)

    def getFaults(self) -> Faults:
        """Gets the last error generated by this object.

        Not all functions return an error code but can potentially report errors.
        This function can be used to retrieve those error codes.
        """
        return Faults(self._getFaults())

    def getStickyFaults(self) -> StickyFaults:
        """
        Polls the various sticky fault flags.
        """
        return StickyFaults(self._getStickyFaults())

    def getBaseID(self) -> int:
        return self.arbId

    def follow(self, masterToFollow: 'BaseMotorController', followerType: FollowerType = FollowerType.PercentOutput):
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
        
        if followerType == FollowerType.PercentOutput:
            self.set(ControlMode.Follower, id24)
        elif followerType == FollowerType.AuxOutput1:
            # follow the motor controller, but set the aux flag
            # to ensure we follow the processed output
            self.set(ControlMode.Follower, id24, DemandType.AuxPID, 0)
        else:
            self.neutralOutput()

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
    
    def configAuxPIDPolarity(self, invert: bool, timeoutMs: int) -> ErrorCode:
        """Configures the Polarity of the Auxiliary PID (PID1).
        
        Standard Polarity:
        
        * Primary Output = PID0 + PID1
        * Auxiliary Output = PID0 - PID1
        
        Inverted Polarity:
        
        * Primary Output = PID0 - PID1
        * Auxiliary Output = PID0 + PID1
        
        :param invert:    If true, use inverted PID1 output polarity.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for config
                          success and report an error if it times out. If zero, no
                          blocking or checking is performed.
        
        :returns: Error Code
        """
        return self.configSetParameter(ParamEnum.ePIDLoopPolarity, 1 if invert else 0, 0, 1, timeoutMs)
