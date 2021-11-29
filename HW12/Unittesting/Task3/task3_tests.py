import unittest
import task3



class TaskTest(unittest.TestCase):
    def test_calc_pos(self):
        self.assertEqual(task3.calc_pos([-5,-4,-3,-2,-1,0,1,2,3,4]), 5)
