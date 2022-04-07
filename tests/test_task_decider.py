from src.task_decider import *
from src.task import *
import unittest


class TestTaskDecider(unittest.TestCase):
    def setUp(self):
        self.task1 = Task("Wash the Dishes", 15)
        self.task2 = Task("Cook Dinner", 60)

    def test_first_comparison(self):
        self.assertEqual("Wash the Dishes", task_decider_function(self.task1, self.task2))