from collections import namedtuple
import sys


__all__ = ["BTrajectoryPoint"]

_name = "BTrajectoryPoint"
_fields = (
    "position",
    "velocity",
    "arbFeedFwd",
    "auxiliaryPos",
    "auxiliaryVel",
    "auxiliaryArbFeedFwd",
    "profileSlotSelect0",
    "profileSlotSelect1",
    "isLastPoint",
    "zeroPos",
    "timeDur",
    "useAuxPID",
)
_defaults = (0, 0, 0, 0, 0, 0, 0, 0, False, False, 0, False)

if sys.version_info[:2] >= (3, 7):
    #: Motion Profile Trajectory Point for use with
    #: :class:`BufferedTrajectoryPointStream`.
    #:
    #: All attributes have a default value of 0 or False, so you can use
    #: keyword arguments for less typing
    BTrajectoryPoint = namedtuple(_name, _fields, defaults=_defaults)
else:
    #: Motion Profile Trajectory Point for use with
    #: :class:`BufferedTrajectoryPointStream`
    #:
    #: All attributes have a default value of 0 or False, so you can use
    #: keyword arguments for less typing
    BTrajectoryPoint = namedtuple(_name, _fields)
    BTrajectoryPoint.__new__.__defaults__ = _defaults

BTrajectoryPoint.position.__doc__ = """
    The position to servo to (in sensor units).
"""
BTrajectoryPoint.velocity.__doc__ = """
    The velocity to feed-forward (in sensor-units per 100ms)
"""
BTrajectoryPoint.arbFeedFwd.__doc__ = """
    Added to the output of PID[0], should be within [-1,+1] where 0.01 = 1%
"""
BTrajectoryPoint.auxiliaryPos.__doc__ = """
    The position for auxiliary PID[1] to target (in sensor units).
"""
BTrajectoryPoint.auxiliaryVel.__doc__ = """
    The velocity for auxiliary PID[1] to target. (in sensor-units per 100ms).
"""
BTrajectoryPoint.auxiliaryArbFeedFwd.__doc__ = """
    Added to the output of PID[1], should be within [-1,+1] where 0.01 = 1%.
"""
BTrajectoryPoint.profileSlotSelect0.__doc__ = """
     Which slot to get PIDF gains.
     PID is used for position servo.
     F is used as the Kv constant for velocity feed-forward.
     Typically this is hardcoded to a particular slot, but you are free to
     gain schedule if need be.
     Choose from [0,3]
"""
BTrajectoryPoint.profileSlotSelect1.__doc__ = """
    Which slot to get PIDF gains for auxiliary PID.
    This only has impact during MotionProfileArc Control mode.
    Choose from [0,1]
"""
BTrajectoryPoint.isLastPoint.__doc__ = """
     Set to true to signal Talon that this is the final point, so do not
     attempt to pop another trajectory point from out of the Talon buffer.
     Instead continue processing this way point.  Typically the velocity
     member variable should be zero so that the motor doesn't spin indefinitely.
"""
BTrajectoryPoint.zeroPos.__doc__ = """
     Set to true to signal Talon to zero the selected sensor.
     When generating MPs, one simple method is to make the first target position zero,
     and the final target position the target distance from the current position.
     Then when you fire the MP, the current position gets set to zero.
     If this is the intent, you can set zeroPos on the first trajectory point.

     Otherwise you can leave this false for all points, and offset the positions
     of all trajectory points so they are correct.
"""
BTrajectoryPoint.timeDur.__doc__ = """
    Duration to apply this trajectory pt.
    This time unit is ADDED to the existing base time set by
    configMotionProfileTrajectoryPeriod().
"""
BTrajectoryPoint.useAuxPID.__doc__ = """
    If using MotionProfileArc, this flag must be true on all points.
    If using MotionProfile, this flag must be false on all points.
"""
