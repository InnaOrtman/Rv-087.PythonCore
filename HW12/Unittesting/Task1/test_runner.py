import unittest
import task1_tests


task1TestSuite = unittest.TestSuite()
task1TestSuite.addTest(unittest.makeSuite(task1_tests.Task1Test))


runner = unittest.TextTestRunner(verbosity = 2)
print("count of tests: " +str(task1TestSuite.countTestCases()) + "\n")
runner.run(task1TestSuite)