from src.task import *
import unittest

class TestTask(unittest.TestCase):

    def setUp(self):
        self.task1 = Task("Wash the Dishes", 15)
        self.task2 = Task("Cook Dinner", 60)
        self.task3 = Task("Clean Windows", 90)
        
    def test_task_description(self):
        self.assertEqual("Wash the Dishes", self.task1.description)

    def test_task_duration(self):
        self.assertEqual(60, self.task2.duration)