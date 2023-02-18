import pytest

import ctre.sensors


def test_cancoder():
    enc = ctre.sensors.CANCoder(0)
    enc.getPosition()


def test_deprecated_import():
    with pytest.warns(FutureWarning, match="moved"):
        from ctre import CANCoder

    assert CANCoder is ctre.sensors.CANCoder
