#!/usr/bin/env python3

"""
 * Example demonstrating the motion magic control mode.
 * Tested with Logitech F710 USB Gamepad inserted into Driver Station.
 *
 * Be sure to select the correct feedback sensor using configSelectedFeedbackSensor() below.
 *
 * After deploying/debugging this to your RIO, first use the left Y-stick
 * to throttle the Talon manually.  This will confirm your hardware setup/sensors
 * and will allow you to take initial measurements.
 *
 * Be sure to confirm that when the Talon is driving forward (green) the
 * position sensor is moving in a positive direction.  If this is not the
 * cause, flip the boolean input to the setSensorPhase() call below.
 *
 * Once you've ensured your feedback device is in-phase with the motor,
 * and followed the walk-through in the Talon SRX Software Reference Manual,
 * use button1 to motion-magic servo to target position specified by the gamepad stick.
"""

from ctre import WPI_TalonSRX
import wpilib


class Robot(wpilib.IterativeRobot):

    #: Which PID slot to pull gains from. Starting 2018, you can choose from
    #: 0,1,2 or 3. Only the first two (0,1) are visible in web-based
    #: configuration.
    kSlotIdx = 0

    #: Talon SRX/ Victor SPX will supported multiple (cascaded) PID loops. For
    #: now we just want the primary one.
    kPIDLoopIdx = 0

    #: set to zero to skip waiting for confirmation, set to nonzero to wait and
    #: report to DS if action fails.
    kTimeoutMs = 10

    def robotInit(self):
        self.talon = WPI_TalonSRX(3)
        self.joy = wpilib.Joystick(0)

        self.loops = 0
        self.timesInMotionMagic = 0

        # first choose the sensor
        self.talon.configSelectedFeedbackSensor(
            WPI_TalonSRX.FeedbackDevice.CTRE_MagEncoder_Relative,
            self.kPIDLoopIdx,
            self.kTimeoutMs,
        )
        self.talon.setSensorPhase(True)
        self.talon.setInverted(False)

        # Set relevant frame periods to be at least as fast as periodic rate
        self.talon.setStatusFramePeriod(
            WPI_TalonSRX.StatusFrameEnhanced.Status_13_Base_PIDF0, 10, self.kTimeoutMs
        )
        self.talon.setStatusFramePeriod(
            WPI_TalonSRX.StatusFrameEnhanced.Status_10_MotionMagic, 10, self.kTimeoutMs
        )

        # set the peak and nominal outputs
        self.talon.configNominalOutputForward(0, self.kTimeoutMs)
        self.talon.configNominalOutputReverse(0, self.kTimeoutMs)
        self.talon.configPeakOutputForward(1, self.kTimeoutMs)
        self.talon.configPeakOutputReverse(-1, self.kTimeoutMs)

        # set closed loop gains in slot0 - see documentation */
        self.talon.selectProfileSlot(self.kSlotIdx, self.kPIDLoopIdx)
        self.talon.config_kF(0, 0.2, self.kTimeoutMs)
        self.talon.config_kP(0, 0.2, self.kTimeoutMs)
        self.talon.config_kI(0, 0, self.kTimeoutMs)
        self.talon.config_kD(0, 0, self.kTimeoutMs)
        # set acceleration and vcruise velocity - see documentation
        self.talon.configMotionCruiseVelocity(15000, self.kTimeoutMs)
        self.talon.configMotionAcceleration(6000, self.kTimeoutMs)
        # zero the sensor
        self.talon.setSelectedSensorPosition(0, self.kPIDLoopIdx, self.kTimeoutMs)

    def teleopPeriodic(self):
        """
        This function is called periodically during operator control
        """
        # get gamepad axis - forward stick is positive
        leftYstick = -1.0 * self.joy.getY()
        # calculate the percent motor output
        motorOutput = self.talon.getMotorOutputPercent()

        # prepare line to print
        sb = []
        sb.append("\tOut%%: %.3f" % motorOutput)
        sb.append(
            "\tVel: %.3f" % self.talon.getSelectedSensorVelocity(self.kPIDLoopIdx)
        )

        if self.joy.getRawButton(1):
            # Motion Magic - 4096 ticks/rev * 10 Rotations in either direction
            targetPos = leftYstick * 4096 * 10.0
            self.talon.set(WPI_TalonSRX.ControlMode.MotionMagic, targetPos)

            # append more signals to print when in speed mode.
            sb.append("\terr: %s" % self.talon.getClosedLoopError(self.kPIDLoopIdx))
            sb.append("\ttrg: %.3f" % targetPos)
        else:
            # Percent voltage mode
            self.talon.set(WPI_TalonSRX.ControlMode.PercentOutput, leftYstick)

        # instrumentation
        self.processInstrumentation(self.talon, sb)

    def processInstrumentation(self, tal, sb):

        # smart dash plots
        wpilib.SmartDashboard.putNumber(
            "SensorVel", tal.getSelectedSensorVelocity(self.kPIDLoopIdx)
        )
        wpilib.SmartDashboard.putNumber(
            "SensorPos", tal.getSelectedSensorPosition(self.kPIDLoopIdx)
        )
        wpilib.SmartDashboard.putNumber(
            "MotorOutputPercent", tal.getMotorOutputPercent()
        )
        wpilib.SmartDashboard.putNumber(
            "ClosedLoopError", tal.getClosedLoopError(self.kPIDLoopIdx)
        )

        # check if we are motion-magic-ing
        if tal.getControlMode() == WPI_TalonSRX.ControlMode.MotionMagic:
            self.timesInMotionMagic += 1
        else:
            self.timesInMotionMagic = 0

        if self.timesInMotionMagic > 10:
            # print the Active Trajectory Point Motion Magic is servoing towards
            wpilib.SmartDashboard.putNumber(
                "ClosedLoopTarget", tal.getClosedLoopTarget(self.kPIDLoopIdx)
            )

            if not self.isSimulation():
                wpilib.SmartDashboard.putNumber(
                    "ActTrajVelocity", tal.getActiveTrajectoryVelocity()
                )
                wpilib.SmartDashboard.putNumber(
                    "ActTrajPosition", tal.getActiveTrajectoryPosition()
                )
                wpilib.SmartDashboard.putNumber(
                    "ActTrajHeading", tal.getActiveTrajectoryHeading()
                )

        # periodically print to console
        self.loops += 1
        if self.loops >= 10:
            self.loops = 0
            print(" ".join(sb))

        # clear line cache
        sb.clear()


if __name__ == "__main__":
    wpilib.run(Robot)
