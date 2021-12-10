import unittest

import task3_4_hw3


class TestTriangle(unittest.TestCase):
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
        self.triangle = task3_4_hw3.TriangleThreeSides(2, 3, 4)

    def tearDown(self) -> None:
        """Tear down for test"""

    def testAreaTriangle(self):
        """Testing calculating area of triangle"""
        print("id: ", self.id(), "\n")
        self.assertAlmostEqual(self.triangle.area()-2, 0.90, places=1)

    def testPerimeterTriangle(self):
        """Testing calculating perimeter of triangle"""
        print("id: ", self.id(), "\n")
        self.assertAlmostEqual(self.triangle.perimeter()-9, 0.00, places=1)


if __name__ == "__main__":
    unittest.main()
