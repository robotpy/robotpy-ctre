from ._impl import BuffTrajPointStream, ErrorCode

from .btrajectorypoint import BTrajectoryPoint

__all__ = ["BufferedTrajectoryPointStream"]


class BufferedTrajectoryPointStream(BuffTrajPointStream):
    """
        Stream of trajectory points for Talon/Victor motion profiling.
    """

    def __init__(self):
        super().__init__()
        self._create1()

    def write(self, trajPt: BTrajectoryPoint) -> ErrorCode:
        """Write a single trajectory point into the buffer.

        :param trajPt: Trajectory point to write.

        :returns: nonzero error code if operation fails.

        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.
        """
        return self._write(*trajPt)
