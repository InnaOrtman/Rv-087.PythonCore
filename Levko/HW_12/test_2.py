#task_4

import unittest
import task_3


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(task_3.M, 4)


if __name__ == '__main__':
    unittest.main()
