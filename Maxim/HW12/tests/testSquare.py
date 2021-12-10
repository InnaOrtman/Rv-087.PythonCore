import unittest

import task3_4_hw3


class TestSquare(unittest.TestCase):
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
        self.square = task3_4_hw3.Square(3)

    def tearDown(self) -> None:
        """Tear down for test"""

    def testAreaSquare(self):
        """Testing calculating area of square"""
        print("id: ", self.id(), "\n")
        self.assertEqual(self.square.area(), 9)

    def testPerimeterSquare(self):
        """Testing calculating perimeter of square"""
        print("id: ", self.id(), "\n")
        self.assertEqual(self.square.perimeter(), 12)


if __name__ == "__main__":
    unittest.main()
