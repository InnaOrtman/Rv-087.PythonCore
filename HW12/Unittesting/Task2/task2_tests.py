import unittest
import task2
import math


class TaskTest(unittest.TestCase):
    def test_hypot(self):
        self.assertEqual(task2.hypot_manual(10,10), math.hypot(10,10))
