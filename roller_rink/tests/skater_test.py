import unittest
from models.skater import Skater
from models.lesson import Lesson
from models.level import Level


class TestSkater(unittest.TestCase):

    def setUp(self):

        self.skater1 = Skater("Wheels Smith", True)
        self.skater2 = Skater("Skate Beckingsale", False)
        self.skater3 = Skater("Quad Stewart", False)
        self.skater4 = Skater("Rhys Derby", True)
        self.lesson1 = Lesson("Speed Skating", "Monday", 10, False)
        self.lesson2 = Lesson("Intensive Training", "Thursday", 3, True)

    def test_skater_has_name(self):
        result = self.skater1.full_name
        self.assertEqual("Wheels Smith", result)

    def test_skater_can_change_name(self):
        self.skater1.full_name = "Ursula K LaSpin"
        result = self.skater1.full_name
        self.assertEqual("Ursula K LaSpin", result)

    def test_skater_is_premium_member__true(self):
        result = self.skater1.premium_member
        self.assertEqual(True, result)

    def test_skater_is_premium_member__false(self):
        result = self.skater2.premium_member
        self.assertEqual(False, result)

    def test_skater_has_id__none(self):
        result = self.skater1.id
        self.assertEqual(None, result)

    # def test_skater_has_id__not_none(self):
    #     self.skater1.id = 3
    #     result = self.skater1.id
    #     self.assertEqual(3, result)
    