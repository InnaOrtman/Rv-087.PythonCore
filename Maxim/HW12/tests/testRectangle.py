import unittest

from Maxim.HW3 import task3_4_hw3


class TestRectangle(unittest.TestCase):
    """Testing class Rectangle"""

    @classmethod
    def setUpClass(cls) -> None:
        """ Set up for class"""

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down for class"""

    def setUp(self) -> None:
        """Create objects of figures"""
        print(self.shortDescription())
        self.rectangle = task3_4_hw3.Rectangle(2, 4)

    def tearDown(self) -> None:
        """Tear down for test"""

    def testAreaRectangle(self):
        """Testing calculating area of rectangle"""
        print("id: ", self.id(), "\n")
        self.assertEqual(self.rectangle.area(), 8)

    def testPerimeterRectangle(self):
        """Testing calculating perimeter of rectangle"""
        print("id: ", self.id(), "\n")
        self.assertEqual(self.rectangle.perimeter(), 12)

    @unittest.skip("Deliberately skipping a test with an error")
    def testSkipped(self):
        """Testing calculating area of rectangle"""
        print("id: ", self.id(), "\n")
        self.assertEqual(self.rectangle.area(), 9)

    # deliberately fail in the test
    def testFailed(self):
        """Testing calculating area of rectangle"""
        print("id: ", self.id(), "\n")
        self.assertEqual(self.rectangle.area(), 9)

    def testErr(self):
        """Testing calculating area of rectangle"""
        print("id: ", self.id(), "\n")
        self.assertEqual()


if __name__ == "__main__":
    unittest.main()
