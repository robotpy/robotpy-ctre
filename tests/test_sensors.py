import pytest

import phoenix5.sensors


def test_cancoder():
    enc = phoenix5.sensors.CANCoder(0)
    enc.getPosition()


def test_deprecated_import():
    with pytest.warns(FutureWarning, match="moved"):
        from phoenix5 import CANCoder

    assert CANCoder is phoenix5.sensors.CANCoder
