import pytest


@pytest.fixture(scope='function')
def victor(ctre):
    return ctre.WPI_VictorSPX(1)

@pytest.fixture(scope='function')
def cdata(victor, hal_data):
    return hal_data['CAN'][1]


def test_victor_init(ctre, hal_data):
    assert 1 not in hal_data['CAN']
    ctre.WPI_VictorSPX(1)
    assert 1 in hal_data['CAN']
    assert hal_data['CAN'][1]['type'] == 'victorspx'

# Victor tests are covered by TalonSRX
