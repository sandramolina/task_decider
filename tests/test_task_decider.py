from src.task_decider import *
from src.task import *
import unittest


class TestTaskDecider(unittest.TestCase):
    def setUp(self):
        self.task1 = Task("Wash the Dishes", 15)
        self.task2 = Task("Cook Dinner", 60)
        self.task3 = Task("Do Ironing", 15)
        self.task4 = Task("Wash Clothes", 60)
        self.task5 = Task("Clean Windows", 90)

    def test_first_comparison(self):
        self.assertEqual("Wash the Dishes", task_decider_function(self.task1, self.task2))

    def test_second_comparison(self):
        self.assertEqual("Do Ironing", task_decider_function(self.task1, self.task3))

    def test_third_comparison(self):
        self.assertEqual("Cook Dinner", task_decider_function(self.task2, self.task3))

    def test_fourth_comparison(self):
        self.assertEqual("Do Ironing", task_decider_function(self.task3, self.task4))

    def test_fifth_comparison(self):
        self.assertEqual("Do Ironing", task_decider_function(self.task4, self.task3))

    def test_sixth_comparison(self):
        self.assertEqual("Wash Clothes", task_decider_function(self.task5, self.task4))
    
    def test_seventh_comparison(self):
        self.assertEqual("Clean Windows", task_decider_function(self.task5, self.task1))

    def test_eighth_comparison(self):
        self.assertEqual("Clean Windows", task_decider_function(self.task1, self.task5))
    
    def test_nineth_comparison(self):
        self.assertEqual("Clean Windows", task_decider_function(self.task3, self.task5))
    
    def test_tenth_comparison(self):
        self.assertEqual("Do Ironing", task_decider_function(self.task1, self.task3))

    def test_eleventh_comparison(self):
        self.assertEqual("Cook Dinner", task_decider_function(self.task2, self.task5))

    def test_twelveth_comparison(self):
        self.assertEqual("Cook Dinner", task_decider_function(self.task5, self.task2))