class PhysicsEngine(object):
    """
        Simulates a single motor connected to an encoder to make the
        motion magic example work correctly
    """

    def __init__(self, physics_controller):
        """
            :param physics_controller: `pyfrc.physics.core.PhysicsInterface` object
                                       to communicate simulation effects to
        """

        self.physics_controller = physics_controller
        self.position = 0

    def update_sim(self, hal_data, now, tm_diff):

        try:
            talon_data = hal_data["CAN"][3]
        except (KeyError, IndexError):
            # talon must not be initialized yet
            return

        # encoder increments speed mutiplied by the time by some constant
        # -> must be an integer
        speed = int(4096 * 4 * talon_data["value"] * tm_diff)
        talon_data["quad_position"] += speed
        talon_data["quad_velocity"] = speed
