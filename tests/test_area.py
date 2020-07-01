import unittest
from src.geometry import area


class TestArea(unittest.TestCase):

    def test_area_square(self):
        self.assertEqual(4, area.area_square(2))

    def test_area_rectangle(self):
        self.assertEqual(20, area.area_rectangle(5, 4))

    def test_area_circle(self):
        self.assertAlmostEqual(12.56, area.area_circle(2.0), delta=0.01)


if __name__ == '__main__':
    unittest.main()
