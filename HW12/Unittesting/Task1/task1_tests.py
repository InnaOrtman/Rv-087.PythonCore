import unittest
import task1


class Task1Test(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(task1.calc_perimeter(5,5), 20)
    def test_area(self):
        self.assertEqual(task1.calc_area(5,5), 25)