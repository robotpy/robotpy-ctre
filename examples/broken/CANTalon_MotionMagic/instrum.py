from wpilib import SmartDashboard
import ctre


class Instrum():
    loops = 0

    @staticmethod
    def process(tal, sb):
        # Smart dash plots
        SmartDashboard.putNumber('RPM', tal.getSpeed())
        SmartDashboard.putNumber('Pos', tal.getPosition())
        SmartDashboard.putNumber('AppliedThrottle', (tal.getOutputVoltage() / tal.getBusVoltage()) * 1023)
        SmartDashboard.putNumber('ClosedLoopError', tal.getClosedLoopError())
        if tal.getControlMode() is ctre.CANTalon.ControlMode.MotionMagic:
            #These API calls will be added in our next release.
            #SmartDashboard.putNumber("ActTrajVelocity", tal.getMotionMagicActTrajVelocity());
            # SmartDashboard.putNumber("ActTrajPosition", tal.getMotionMagicActTrajPosition());
            pass
        
        # Periodically print to console
        if Instrum.loops >= 10:
            print(sb)
            Instrum.loops = 0