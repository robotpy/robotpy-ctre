# validated: 2018-01-06 EN d090f9cdc6a1 libraries/driver/include/ctre/phoenix/MotorControl/Faults.h


__all__ = ['FaultsBase']


class FaultsBase:
    fields = []

    def __init__(self, bits = 0):
        mask = 1
        for field in self.fields:
            setattr(self, field, bool(bits & mask))
            mask <<= 1

    def toBitfield(self):
        retval = 0
        mask = 1
        for field in self.fields:
            if getattr(self, field):
                retval |= mask
                mask <<= 1
        return retval

    def hasAnyFault(self):
        return any([getattr(self, field) for field in self.fields])

    def __str__(self):
        return " ".join(["%s:%s" % (field, int(getattr(self,field))) for field in self.fields])


