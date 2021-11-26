#task_5
import unittest
import task_1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertListEqual(task_1.list1, task_1.list1)
        print("it`s ok")

    def test_something_1(self):
        try:
            self.assertLess(sum(task_1.list1), task_1.c)

        except AssertionError:
            print("it`s not ok")


if __name__ == '__main__':
    unittest.main()
