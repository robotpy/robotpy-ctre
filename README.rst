robotpy-ctre
============

This is a python wrapper around the CTRE 3rd party library. Documentation can be
found at http://robotpy-ctre.readthedocs.io/

**NOTE**: The RobotPy project is not associated with or endorsed by Cross The
Road Electronics.

Setup (tests/simulator)
-----------------------

If you intend to use robotpy-ctre in your robot tests or via the pyfrc
simulator, you must install this package locally::

    pip3 install -U robotpy-ctre

Or on Windows::
    
    py -3 -m pip install -U robotpy-ctre

Setup (RoboRIO)
---------------

Even if you have robotpy-ctre installed locally, you need to install it on your
robot separately.

Python package
~~~~~~~~~~~~~~

You really don't want to compile this yourself, so don't download this from pypi
and install it. Instead, you can download a pre-packaged version from our opkg repository. Use the RobotPy installation script (comes with the RobotPy download), and run the following on your computer while connected to the internet::

  py -3 installer.py download-opkg python36-robotpy-ctre

Then, when connected to the roborio's network, run::

  py -3 installer.py install-opkg python36-robotpy-ctre

For more information about installing packages, see https://github.com/robotpy/roborio-packages

NI Web Dashboard (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

CTRE Phoenix can integrate with the NI Web Dashboard on the RoboRIO. This is not required to
run robotpy-ctre on the RoboRIO, but it can be a useful diagnostic tool. To install this, you
will need to use the CTRE Lifeboat tool to install it separately.

Refer to `the CTRE documentation <https://github.com/CrossTheRoadElec/Phoenix-Documentation#installing-phoenix-framework-onto-your-frc-robot>`_
for more details.

Developers Notes
================

Notes for advanced users and developers can be found in develop.md in the git
repository.

License
=======

RobotPy specific bits are available under the Apache 2.0 license. The CTRE
binaries are available under their custom license which basically says "you may
only use this software with our hardware". See LICENSE for details.

Author
======

Dustin Spicuzza (dustin@virtualroadside.com)
