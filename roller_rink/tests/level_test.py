import unittest
from models.skater import Skater
from models.lesson import Lesson
from models.level import Level

class TestLevel(unittest.TestCase):

    def setUp(self):

        self.skater1 = Skater("Wheels Smith", True)
        self.skater2 = Skater("Skate Beckingsale", False)
        self.skater3 = Skater("Quad Stewart", False)
        self.skater4 = Skater("Rhys Derby", True)

        self.lesson1 = Lesson("Speed Skating", "Monday", 10, False)
        self.lesson2 = Lesson("Intensive Training", "Thursday", 3, True)

        self.level1 = Level(self.skater1, self.lesson1, "Beginner")
        self.level2 = Level(self.skater2, self.lesson1, "Intermediate")

    
    def test_level_has_skater(self):
        result = self.level1.skater
        self.assertEqual(self.skater1, result)

    def test_level_has_lesson(self):
        result = self.level1.lesson
        self.assertEqual(self.lesson1, result)

    def test_level_has_level_reached(self):
        result = self.level1.level_reached
        self.assertEqual("Beginner", result)

    def test_level_can_change_level_reached(self):
        self.level1.level_reached = "Advanced"
        result = self.level1.level_reached
        self.assertEqual("Advanced", result)

    def test_level_id_is_none(self):
        result = self.level1.id
        self.assertEqual(None, result)

    def test_level_id_is_not_none(self):
        self.level1.id = 12
        result = self.level1.id
        self.assertEqual(12, result)