import unittest
import task4



class TaskTest(unittest.TestCase):
    def test_calc_guess_equal(self):
        self.assertEqual(task4.guess_number(5,5), 1)

    def test_calc_guess_bigger(self):
        self.assertEqual(task4.guess_number(5,10), 2)

    def test_calc_guess_smaller(self):
        self.assertEqual(task4.guess_number(10,5), 0)

