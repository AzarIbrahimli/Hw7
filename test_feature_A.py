# Azar Ibrahimli

import unittest
from features import SprintVelocity
class TestSprintVelocity(unittest.TestCase):
    def test_calculate_velocity_empty_list(self):
        sprint_velocity = SprintVelocity()

        velocity = sprint_velocity.calculate_velocity()

        self.assertEqual(velocity, 0)

    def test_calculate_velocity_with_values(self):
        sprint_velocity = SprintVelocity()
        sprint_velocity.sprint_points = [10, 15, 20]

        velocity = sprint_velocity.calculate_velocity()

        self.assertEqual(velocity, 15)
