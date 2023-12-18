import unittest
from main import main
from io import StringIO


class TestMain(unittest.TestCase):
    def test_main(self):
        captured_output = StringIO()
        expected_output = [
            'Супер красивый Прямоугольник синего цвета с длиной 8 и шириной 8. А плошадь его равна 64\n',
            'Супер красивый Круг зеленого цвета с радиусом 8. А плошадь его равна 201.06192982974676\n',
            'Супер красивый Квадрат красного цвета с длиной сторон 8. А плошадь его равна 64\n',
            '[[0. 0. 0.]\n [0. 0. 0.]]\n'
        ]

        with captured_output as (out, err):
            main()

        output = out.getvalue()

        for i in range(len(expected_output)):
            self.assertEqual(output, expected_output[i])


if __name__ == '__main__':
    unittest.main()