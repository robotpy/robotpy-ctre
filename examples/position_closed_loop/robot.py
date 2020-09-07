#!/usr/bin/env python3

"""
 * Example demonstrating the Position closed-loop servo.
 * Tested with Logitech F350 USB Gamepad inserted into Driver Station]
 *
 * Be sure to select the correct feedback sensor using configSelectedFeedbackSensor() below.
 *
 * After deploying/debugging this to your RIO, first use the left Y-stick
 * to throttle the Talon manually.  This will confirm your hardware setup.
 * Be sure to confirm that when the Talon is driving forward (green) the
 * position sensor is moving in a positive direction.  If this is not the cause
 * flip the boolean input to the setSensorPhase() call below.
 *
 * Once you've ensured your feedback device is in-phase with the motor,
 * use the button shortcuts to servo to target position.
 *
 * Tweak the PID gains accordingly.
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
        self.lastButton1 = False
        self.targetPos = 0

        # choose the sensor and sensor direction
        self.talon.configSelectedFeedbackSensor(
            WPI_TalonSRX.FeedbackDevice.CTRE_MagEncoder_Relative,
            self.kPIDLoopIdx,
            self.kTimeoutMs,
        )

        # choose to ensure sensor is positive when output is positive
        self.talon.setSensorPhase(True)

        # choose based on what direction you want forward/positive to be.
        # This does not affect sensor phase.
        self.talon.setInverted(False)

        # set the peak and nominal outputs, 12V means full
        self.talon.configNominalOutputForward(0, self.kTimeoutMs)
        self.talon.configNominalOutputReverse(0, self.kTimeoutMs)
        self.talon.configPeakOutputForward(1, self.kTimeoutMs)
        self.talon.configPeakOutputReverse(-1, self.kTimeoutMs)

        # Set the allowable closed-loop error, Closed-Loop output will be
        # neutral within this range. See Table in Section 17.2.1 for native
        # units per rotation.
        self.talon.configAllowableClosedloopError(0, self.kPIDLoopIdx, self.kTimeoutMs)

        # set closed loop gains in slot0, typically kF stays zero - see documentation */
        self.talon.selectProfileSlot(self.kSlotIdx, self.kPIDLoopIdx)
        self.talon.config_kF(0, 0, self.kTimeoutMs)
        self.talon.config_kP(0, 0.1, self.kTimeoutMs)
        self.talon.config_kI(0, 0, self.kTimeoutMs)
        self.talon.config_kD(0, 0, self.kTimeoutMs)

        # zero the sensor
        self.talon.setSelectedSensorPosition(0, self.kPIDLoopIdx, self.kTimeoutMs)

    def teleopPeriodic(self):
        """
        This function is called periodically during operator control
        """
        # get gamepad axis - forward stick is positive
        leftYstick = self.joy.getY()
        # calculate the percent motor output
        motorOutput = self.talon.getMotorOutputPercent()
        button1 = self.joy.getRawButton(1)
        button2 = self.joy.getRawButton(2)

        # deadband gamepad
        if abs(leftYstick) < 0.1:
            leftYstick = 0

        # prepare line to print
        sb = []
        sb.append("\tOut%%: %.3f" % motorOutput)
        sb.append(
            "\tPos: %.3fu" % self.talon.getSelectedSensorPosition(self.kPIDLoopIdx)
        )

        if self.lastButton1 and button1:
            # Position mode - button just pressed

            # 10 Rotations * 4096 u/rev in either direction
            self.targetPos = leftYstick * 4096 * 10.0
            self.talon.set(WPI_TalonSRX.ControlMode.Position, self.targetPos)

        # on button2 just straight drive
        if button2:
            # Percent voltage mode
            self.talon.set(WPI_TalonSRX.ControlMode.PercentOutput, leftYstick)

        if self.talon.getControlMode() == WPI_TalonSRX.ControlMode.Position:
            # append more signals to print when in speed mode.
            sb.append("\terr: %s" % self.talon.getClosedLoopError(self.kPIDLoopIdx))
            sb.append("\ttrg: %.3f" % self.targetPos)

        # periodically print to console
        self.loops += 1
        if self.loops >= 10:
            self.loops = 0
            print(" ".join(sb))

        # save button state for on press detect
        self.lastButton1 = button1


if __name__ == "__main__":
    wpilib.run(Robot)
