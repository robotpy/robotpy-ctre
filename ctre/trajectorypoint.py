# validated: 2018-01-14 DV 76dd48fe2e6a libraries/driver/include/ctre/phoenix/Motion/TrajectoryPoint.h
from collections import namedtuple

from ._impl import TrajectoryDuration


__all__ = ['TrajectoryPoint']

#: Motion Profile Trajectory Point.
#: This is simply a data transfer object.
TrajectoryPoint = namedtuple("TrajectoryPoint", ["position", "velocity", "headingDeg", "profileSlotSelect0",
                                                 "profileSlotSelect1", "isLastPoint", "zeroPos", "timeDur"])
TrajectoryPoint.TrajectoryDuration = TrajectoryDuration
TrajectoryPoint.position.__doc__ = "The position to servo to."
TrajectoryPoint.velocity.__doc__ = "The velocity to feed-forward."
#TrajectoryPoint.headingDeg.__doc__ = ""
TrajectoryPoint.profileSlotSelect0.__doc__ = """
     Which slot to get PIDF gains.
     PID is used for position servo.
     F is used as the Kv constant for velocity feed-forward.
     Typically this is hardcoded to a particular slot, but you are free to
     gain schedule if need be.
     Choose from [0,3]
"""
TrajectoryPoint.profileSlotSelect1.__doc__ = """
    Which slot to get PIDF gains for cascaded PID.
    This only has impact during MotionProfileArc Control mode.
    Choose from [0,1]
"""
TrajectoryPoint.isLastPoint.__doc__ = """
     Set to true to signal Talon that this is the final point, so do not
     attempt to pop another trajectory point from out of the Talon buffer.
     Instead continue processing this way point.  Typically the velocity
     member variable should be zero so that the motor doesn't spin indefinitely.
"""
TrajectoryPoint.zeroPos.__doc__ = """
     Set to true to signal Talon to zero the selected sensor.
     When generating MPs, one simple method is to make the first target position zero,
     and the final target position the target distance from the current position.
     Then when you fire the MP, the current position gets set to zero.
     If this is the intent, you can set zeroPos on the first trajectory point.

     Otherwise you can leave this false for all points, and offset the positions
     of all trajectory points so they are correct.
"""
TrajectoryPoint.timeDur.__doc__ = """
    Duration to apply this trajectory pt.
    This time unit is ADDED to the existing base time set by
    configMotionProfileTrajectoryPeriod().
"""

# monkey patch the docstring in - TODO make this part of autogen
TrajectoryDuration.__doc__ = TrajectoryPoint.timeDur.__doc__
