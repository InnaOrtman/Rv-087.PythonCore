import unittest
import tests.testRectangle as rec
import tests.testTriangle as tri
import tests.testSquare as sq
import tests.testCircle as cir


figuresTestSuit = unittest.TestSuite()
figuresTestSuit.addTest(unittest.makeSuite(rec.TestRectangle))
figuresTestSuit.addTest(unittest.makeSuite(sq.TestSquare))
figuresTestSuit.addTest(unittest.makeSuite(cir.TestCircle))
figuresTestSuit.addTest(unittest.makeSuite(tri.TestTriangle))
print("count of tests: " + str(figuresTestSuit.countTestCases()) + "\n")

# testCases = [rec.TestRectangle, sq.TestSquare, cir.TestCircle,
#              tri.TestTriangle]
# testLoad = unittest.TestLoader()
# suites = []
# for tc in testCases:
#     if tc == "testPerimeterTriangle":
#         continue
#     suites.append(testLoad.loadTestsFromTestCase(tc))
# resSuite = unittest.TestSuite(suites)
runner = unittest.TextTestRunner(verbosity=2)

# runner.run(figuresTestSuit)
testResults = runner.run(figuresTestSuit)
# testResults = runner.run(resSuite)
print("Errors: ", len(testResults.errors))
print("Failures: ", len(testResults.failures))
print("Skipped: ", len(testResults.skipped))
print("TestsRun: ", testResults.testsRun)
