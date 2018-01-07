
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

// Use this to release the gil
typedef py::call_guard<py::gil_scoped_release> release_gil;

// CTRE includes
#include "ctre/phoenix/CCI/CANifier_CCI.h"
#include "ctre/phoenix/CCI/MotController_CCI.h"
#include "ctre/phoenix/CCI/PigeonIMU_CCI.h"

#include "ctre/phoenix/ErrorCode.h"
#include "ctre/phoenix/paramEnum.h"

//#include "autogen/CheckCTRCode.hpp"


#include "autogen/CANifier.hpp"
#include "autogen/MotController.hpp"
#include "autogen/PigeonIMU.hpp"


PYBIND11_MODULE(ctre_roborio, m) {

  #include "autogen/CANifier.cpp.inc"
  #include "autogen/MotController.cpp.inc"
  #include "autogen/PigeonIMU.cpp.inc"

  #include "autogen/ctre_enums.cpp.inc"

}
