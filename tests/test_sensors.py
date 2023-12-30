import pytest

import phoenix5.sensors


def test_cancoder():
    enc = phoenix5.sensors.CANCoder(0)
    enc.getPosition()
