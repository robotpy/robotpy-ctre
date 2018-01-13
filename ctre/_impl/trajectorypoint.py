# validated: 2018-01-06 EN d090f9cdc6a1 libraries/driver/include/ctre/phoenix/Motion/TrajectoryPoint.h
from collections import namedtuple


__all__ = ['TrajectoryPoint']

#: Motion Profile Trajectory Point.
#: This is simply a data transfer object.
TrajectoryPoint = namedtuple("TrajectoryPoint", ["position", "velocity", "headingDeg", "profileSlotSelect",
                                                 "isLastPoint", "zeroPos"])
TrajectoryPoint.position.__doc__ = "The position to servo to."
TrajectoryPoint.velocity.__doc__ = "The velocity to feed-forward."
#TrajectoryPoint.headingDeg.__doc__ = ""
TrajectoryPoint.profileSlotSelect.__doc__ = """
     Which slot to get PIDF gains.
     PID is used for position servo.
     F is used as the Kv constant for velocity feed-forward.
     Typically this is hardcoded to a particular slot, but you are free to
     gain schedule if need be.
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
