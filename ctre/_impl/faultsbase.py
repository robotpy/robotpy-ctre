# validated: 2018-01-14 DV a68a0c3ebf0b libraries/driver/include/ctre/phoenix/MotorControl/Faults.h
# -> ensure all the methods exist!


class FaultsBase:
    # List all the flags from LSB to MSB in __slots__.
    __slots__ = ()

    def __init__(self, bits: int = 0) -> None:
        for field in self.__slots__:
            setattr(self, field, bool(bits & 1))
            bits >>= 1

    def toBitfield(self) -> int:
        retval = 0
        mask = 1
        for field in self.__slots__:
            if getattr(self, field):
                retval |= mask
                mask <<= 1
        return retval

    def hasAnyFault(self) -> bool:
        """True iff any of the flags are true."""
        return any(getattr(self, field) for field in self.__slots__)

    def __str__(self):
        return " ".join(
            ["%s:%d" % (field, getattr(self, field)) for field in self.__slots__]
        )
