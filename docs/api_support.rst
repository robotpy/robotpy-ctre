.. _api_support:

Supported API
=============

RoboRIO
~~~~~~~

RobotPy uses partially automatically generated bindings for the CTRE libraries,
and so almost all functionality exposed by the CTRE libraries is expected to work
when used on a RoboRIO. If you find something that doesn't work, that's most likely
a bug and/or oversight. please file an `issue on github <https://github.com/robotpy/robotpy-ctre/issues>`_
and we'll try to address the problem.

Simulation
~~~~~~~~~~

The RobotPy project tries to implement simulation functionality for commonly
used pieces of the CTRE API. Unfortunately, the API is huge and changes every
year, so there are obscure/complex pieces that just haven't been implemented
yet.

If you run into one of these functions that aren't implemented and you'd like
to see it implemented in simulation, please file an
`issue on github <https://github.com/robotpy/robotpy-ctre/issues>`_ and lets
talk about it.

.. note:: The best way to ensure that simulation functionality you require gets
          implemented is by doing it yourself and making a pull request!
          RobotPy is a community project and needs its community members to
          contribute in order to continue existing.
