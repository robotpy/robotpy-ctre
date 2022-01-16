CTRE Libraries
==============

These are not installed on the Robot by default. For installation instructions,
see :ref:`robotpy-ctre install docs <install_ctre>`.

This documentation documents the various classes and methods that are
available to Python code, but don't discuss in detail how to actually
set up, configure, and tune your CTRE hardware. For that kind of information,
refer to the `CTRE software guide <https://phoenix-documentation.readthedocs.io/en/latest/index.html>`_.

RobotPy uses automatically generated bindings for the CTRE libraries,
and so almost all functionality exposed by the CTRE libraries is expected to work
when used on a RoboRIO. If you find something that doesn't work, that's most likely
a bug and/or oversight. please file an `issue on github <https://github.com/robotpy/robotpy-ctre/issues>`_
and we'll try to address the problem.

.. toctree::
    
    ctre
    ctre.led
