import unittest

from Maxim.HW3 import task3_4_hw3


class TestCircle(unittest.TestCase):
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
        self.circle = task3_4_hw3.Circle(5)

    def tearDown(self) -> None:
        """Tear down for test"""

    def testAreaCircule(self):
        """Testing calculating area of circle"""
        print("id: ", self.id(), "\n")
        self.assertAlmostEqual(self.circle.area()-78, 0.54, places=1)

    def testPerimeterCircule(self):
        """Testing calculating perimeter of circle"""
        print("id: ", self.id(), "\n")
        self.assertAlmostEqual(self.circle.perimeter()-31, 0.41, places=1)


if __name__ == "__main__":
    unittest.main()
