#Azar Ibrahimli

import unittest
from features import TeamCapacity, TeamMember
class TestTeamCapacity(unittest.TestCase):
    def test_calculate_individual_capacity_no_days_off_no_ceremony_hours(self):
        team_member = TeamMember(days_off=0, ceremony_hours=0, hours_per_day=(8, 8), sprint_days=5)
        team_capacity = TeamCapacity()

        capacity = team_capacity.calculate_individual_capacity(team_member)

        self.assertEqual(capacity, 40)

    def test_calculate_individual_capacity_with_days_off(self):
        team_member = TeamMember(days_off=2, ceremony_hours=0, hours_per_day=(8, 8), sprint_days=5)
        team_capacity = TeamCapacity()

        capacity = team_capacity.calculate_individual_capacity(team_member)

        self.assertEqual(capacity, 24)

    def test_calculate_individual_capacity_with_ceremony_hours(self):
        team_member = TeamMember(days_off=0, ceremony_hours=4, hours_per_day=(8, 8), sprint_days=5)
        team_capacity = TeamCapacity()

        capacity = team_capacity.calculate_individual_capacity(team_member)

        self.assertEqual(capacity, 36.0)


