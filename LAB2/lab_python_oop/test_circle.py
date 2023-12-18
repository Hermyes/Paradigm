import unittest
from lab_python_oop.circle import Circle


class TestCircle(unittest.TestCase):
    def test_square(self):
        c = Circle(8, "зеленого")
        self.assertAlmostEqual(c.square(), 201.06192982974676, places=5)

    def test_repr(self):
        c = Circle(8, "зеленого")
        expected_repr = 'Супер красивый Круг зеленого цвета с радиусом 8. А плошадь его равна 201.06192982974676'
        self.assertEqual(repr(c), expected_repr)


if __name__ == '__main__':
    unittest.main()