import unittest
import task5



class TaskTest(unittest.TestCase):
    def test_check_notes(self):
        self.assertEqual(task5.check_notes(532), [2, 1, 3, 2])

