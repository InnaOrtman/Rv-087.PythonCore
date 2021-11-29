import unittest
import task5_tests

taskTestSuite = unittest.TestSuite()
taskTestSuite.addTest(unittest.makeSuite(task5_tests.TaskTest))


runner = unittest.TextTestRunner(verbosity = 2)
print("count of tests: " +str(taskTestSuite.countTestCases()) + "\n")
runner.run(taskTestSuite)