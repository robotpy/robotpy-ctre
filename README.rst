robotpy-ctre
============

This is a python wrapper around the CTRE 3rd party library. Documentation can be
found at http://robotpy-ctre.readthedocs.io/

**NOTE**: The RobotPy project is not associated with or endorsed by Cross The 
Road Electronics.

Setup (simulator)
-----------------

    pip3 install robotpy-ctre

Setup (RoboRIO)
---------------

**NOTE**: These are manual instructions, we'll have support to install this via
          the RobotPy installer in a few days

You really don't want to compile this yourself, so don't download this from pypi
and install it. Use the precompiled wheel that we've published instead. 

* Download the latest robotpy-ctre whl from https://www.tortall.net/~robotpy/wheels/2017/
* Copy the whl to your RoboRIO using WinSCP/scp or equivalent
* ssh in to the RoboRIO and run ``pip3 install roborio-ctre*.whl``

Compilation
===========

Currently, compilation is only supported on the RoboRIO or the RoboRIO VM. Use
opkg to install g++ et al, install libstdc++-dev, and then run::

    pip3 install pybind11 wheel
    pip3 wheel .

Be warned that it takes a very long time to compile, and that if you're using
a real RoboRIO that you will need a swap device installed.

License
=======

RobotPy specific bits are available under the Apache 2.0 license. The CTRE
binaries are available under their custom license which basically says "you may
only use this software with our hardware". See LICENSE for details.

Author
======

Dustin Spicuzza (dustin@virtualroadside.com)
