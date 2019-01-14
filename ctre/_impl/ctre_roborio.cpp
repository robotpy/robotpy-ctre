
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

// Use this to release the gil
typedef py::call_guard<py::gil_scoped_release> release_gil;

// CTRE includes
#include "ctre/phoenix/cci/BuffTrajPointStream_CCI.h"
#include "ctre/phoenix/cci/CANifier_CCI.h"
#include "ctre/phoenix/cci/MotController_CCI.h"
#include "ctre/phoenix/cci/PigeonIMU_CCI.h"

#include "ctre/phoenix/ErrorCode.h"
#include "ctre/phoenix/paramEnum.h"

#include "ctre/phoenix/CANifierControlFrame.h"
#include "ctre/phoenix/CANifierStatusFrame.h"

#include "ctre/phoenix/motion/SetValueMotionProfile.h"
#include "ctre/phoenix/motion/TrajectoryPoint.h"

#include "ctre/phoenix/motorcontrol/ControlFrame.h"
#include "ctre/phoenix/motorcontrol/ControlMode.h"
#include "ctre/phoenix/motorcontrol/DemandType.h"
#include "ctre/phoenix/motorcontrol/FeedbackDevice.h"
#include "ctre/phoenix/motorcontrol/FollowerType.h"
#include "ctre/phoenix/motorcontrol/InvertType.h"
#include "ctre/phoenix/motorcontrol/LimitSwitchType.h"
#include "ctre/phoenix/motorcontrol/NeutralMode.h"
#include "ctre/phoenix/motorcontrol/RemoteSensorSource.h"
#include "ctre/phoenix/motorcontrol/SensorTerm.h"
#include "ctre/phoenix/motorcontrol/StatusFrame.h"
#include "ctre/phoenix/motorcontrol/VelocityMeasPeriod.h"

#include "ctre/phoenix/sensors/PigeonIMU_ControlFrame.h"
#include "ctre/phoenix/sensors/PigeonIMU_StatusFrame.h"


//#include "autogen/CheckCTRCode.hpp"


#include "autogen/BuffTrajPointStream.hpp"
#include "autogen/CANifier.hpp"
#include "autogen/MotController.hpp"
#include "autogen/PigeonIMU.hpp"


PYBIND11_MODULE(ctre_roborio, m) {

  #include "autogen/BuffTrajPointStream.cpp.inc"
  #include "autogen/CANifier.cpp.inc"
  #include "autogen/MotController.cpp.inc"
  #include "autogen/PigeonIMU.cpp.inc"

  #include "autogen/ctre_enums.cpp.inc"

}
