import unittest
from models.skater import Skater
from models.lesson import Lesson


class TestLesson(unittest.TestCase):

    def setUp(self):

        self.lesson1 = Lesson("Speed Skating", "Monday", 10, False)
        self.lesson2 = Lesson("Intensive Training", "Thursday", 3, True)

    def test_lesson_has_name(self):
        result = self.lesson1.name
        self.assertEqual("Speed Skating", result)

    def test_lesson_can_change_name(self):
        self.lesson1.name = "Skating on Stilts"
        result = self.lesson1.name
        self.assertEqual("Skating on Stilts", result)

    def test_lesson_has_day(self):
        result = self.lesson1.day
        self.assertEqual("Monday", result)

    def test_lesson_can_change_day(self):
        self.lesson1.day = "Friday"
        result = self.lesson1.day
        self.assertEqual("Friday", result)

    def test_lesson_has_capacity(self):
        result = self.lesson1.capacity
        self.assertEqual(10, result)

    def test_lesson_can_change_capacity(self):
        self.lesson1.capacity = 50
        result = self.lesson1.capacity
        self.assertEqual(50, result)

    def test_lesson_is_premium__true(self):
        result = self.lesson2.premium
        self.assertEqual(True, result)

    def test_lesson_is_premium__false(self):
        result = self.lesson1.premium
        self.assertEqual(False, result)

    def test_lesson_id_is_none(self):
        result = self.lesson1.id
        self.assertEqual(None, result)

    def test_lesson_id_is_not_none(self):
        self.lesson1.id = 15
        result = self.lesson1.id
        self.assertEqual(15, result)