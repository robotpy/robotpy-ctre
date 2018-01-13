robotpy-ctre wrapper generators
===============================

The files in this directory are used to generate the needed python wrappers
for the CTRE libraries from the CCI headers distributed with their
binaries.

Note that at this time we do not support the entire Phoenix framework, but only
the motor controllers.

Requirements
------------

    pip install header2whatever

Generation
----------

The wrapper generation automatically happens as part of the setup.py build
process when building on a RoboRIO.
