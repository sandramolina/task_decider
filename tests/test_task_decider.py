from src.task_decider import *
from src.task import *
import unittest


class TestTaskDecider(unittest.TestCase):
    def setUp(self):
        self.task1 = Task("Wash the Dishes", 15)
        self.task2 = Task("Cook Dinner", 60)
        self.task3 = Task("Clean Windows", 90)

    def test_first_comparison(self):
        self.assertEqual("Wash the Dishes", task_decider_function(self.task1, self.task2))

    def test_second_comparison(self):
        self.assertEqual("Clean Windows", task_decider_function(self.task1, self.task3))

    def test_third_comparison(self):
        self.assertEqual("Cook Dinner", task_decider_function(self.task2, self.task3))

    def test_fourth_comparison(self):
        self.assertEqual("Wash the Dishes", task_decider_function(self.task3, self.task1))