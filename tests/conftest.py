import sys
import pytest
from unittest.mock import patch, MagicMock


@pytest.fixture(scope="function")
def _module_patch(request):
    '''This patch forces wpilib to reload each time we do this'''
    
    assert 'halmock' not in request.fixturenames, "Cannot use mock and real fixtures in same function!"
    
    #assert 'wpilib' not in sys.modules, "Must use wpilib fixture, don't import wpilib directly"
    
    # .. this seems inefficient
    
    m = patch.dict('sys.modules', {})
    m.start()
    try:
        yield
    finally:
        m.stop()


@pytest.fixture(scope="function")
def hal(_module_patch):
    """Simulated hal module"""
    import hal
    return hal


@pytest.fixture(scope='function')
def ctre(hal, hal_data):
    import ctre
    return ctre


@pytest.fixture(scope='function')
def sendablebuilder(wpilib, networktables):
    builder = wpilib.SendableBuilder()
    table = networktables.NetworkTables.getTable("component")
    builder.setTable(table)
    return builder


@pytest.fixture(scope="function")
def hal_data(hal):
    """Simulation data for HAL"""
    import hal_impl.functions
    import hal_impl.data
    hal_impl.functions.reset_hal()
    return hal_impl.data.hal_data


@pytest.fixture(scope="function")
def wpilib(_module_patch, hal, hal_data, networktables):
    """Actual wpilib implementation"""
    import wpilib
    import wpilib.buttons
    import wpilib.command
    import wpilib.drive
    import wpilib.interfaces
    
    yield wpilib
    
    # Note: even though the wpilib module is freshly loaded each time a new
    # test is ran, we still call _reset() to finish off any finalizers
    wpilib.Resource._reset()


@pytest.fixture(scope="function")
def networktables():
    """Networktables instance"""
    import networktables
    networktables.NetworkTables.startTestMode()
    yield networktables
    networktables.NetworkTables.shutdown()
