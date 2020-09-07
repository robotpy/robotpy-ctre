#!/usr/bin/env python3

import wpilib
import ctre


class MyRobot(wpilib.IterativeRobot):
    """
    This is a short sample program demonstrating how to use the basic throttle
    mode of the TalonSRX
    """

    def robotInit(self):
        self.motor = ctre.WPI_TalonSRX(1)  # Initialize the TalonSRX on device 1.

    def disabledPeriodic(self):
        self.motor.disable()

    def teleopPeriodic(self):
        # Set the motor's output to half power.
        # This takes a number from -1 (100% speed in reverse) to +1 (100%
        # speed going forward)
        self.motor.set(0.5)


if __name__ == "__main__":
    wpilib.run(MyRobot)
