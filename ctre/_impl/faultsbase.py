# validated: 2018-01-14 DV a68a0c3ebf0b libraries/driver/include/ctre/phoenix/MotorControl/Faults.h
# -> ensure all the methods exist!


class FaultsBase:
    __slots__ = ("bits",)

    def __init__(self, bits: int = 0) -> None:
        self.bits = bits

    def toBitfield(self) -> int:
        return self.bits

    def hasAnyFault(self) -> bool:
        """True iff any of the flags are true."""
        return self.bits != 0

    def __str__(self):
        return " ".join(
            [
                "%s:%d" % (field, getattr(self, field))
                for field, method in self.__class__.__dict__.items()
                if isinstance(method, property)
            ]
        )
