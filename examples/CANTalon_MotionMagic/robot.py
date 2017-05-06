"""
Example demonstrating the motion magic control mode.
Tested with Logitech F710 USB Gamepad inserted into Driver Station.

Be sure to select the correct feedback sensor using SetFeedbackDevice() below.

After deploying/debugging this to your RIO, first use the left Y-stick
to throttle the Talon manually.  This will confirm your hardware setup/sensors
and will allow you to take initial measurements.

Be sure to confirm that when the Talon is driving forward (green) the
position sensor is moving in a positive direction.  If this is not the
cause, flip the boolean input to the reverseSensor() call below.

Once you've ensured your feedback device is in-phase with the motor,
and followed the walk-through in the Talon SRX Software Reference Manual,
use button1 to motion-magic servo to target position specified by the gamepad stick.
"""
import wpilib
import ctre
from examples.CANTalon_MotionMagic.instrum import Instrum


class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.talon = ctre.CANTalon(3)
        self.joystick = wpilib.Joystick(0)

        self.talon.setFeedbackDevice(ctre.CANTalon.FeedbackDevice.CtreMagEncoder_Relative)
        # self.talon.configEncoderCodesPerRev(XXX), if using FeedbackDevice.QuadEncoder
        # self.talon.configPotentiometerTurns(XXX), if using FeedbackDevice.AnalogEncoder or AnalogPot

        # Set the peak nominal outputs. 12V means full
        self.talon.configNominalOutputVoltage(+0.0, -0.0)
        self.talon.configPeakOutputVoltage(12.0, -12.0)

        # Set closed loop gains in slot0 - see documentation
        self.talon.setProfile(0)
        self.talon.setPID(0, 0, 0, 0)  # P,I,D,F = 0

        # Set acceleration and vcruise velocity - see documentation
        self.talon.setMotionMagicCruiseVelocity(0)
        self.talon.setMotionMagicAcceleration(0)

    def teleopPeriodic(self):
        # Get gamepad axis - forward stick is positive
        leftYstick = -1 * self.joystick.getAxis(wpilib.Joystick.AxisType.kY)
        # Calculate the percent motor output
        motor_output = self.talon.getOutputVoltage() / self.talon.getBusVoltage()

        # Prepare line to print
        sb = '\tout:{}\tspd:{}'.format(motor_output, self.talon.getSpeed())

        if self.joystick.getRawButton(1):
            targetPos = leftYstick * 10  # 10 rotations in either direction
            self.talon.changeControlMode(ctre.CANTalon.ControlMode.MotionMagic)
            self.talon.set(targetPos)

            # Append more lines to print
            sb += '\terr:{}\ttrg{}'.format(self.talon.getClosedLoopError(), targetPos)
        else:
            # Percent voltage mode
            self.talon.changeControlMode(ctre.CANTalon.ControlMode.PercentVbus)
            self.talon.set(leftYstick)

        # Instrumentation
        Instrum.process(self.talon, sb)

        sb = ''

if __name__ == '__main__':
    wpilib.run(MyRobot)
