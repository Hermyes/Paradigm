from lab_python_oop.figure import Figure
from lab_python_oop.Сolor import Color
import math


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, radius, color):
        self.radius = radius
        self.fc = Color()
        self.fc.colorproperty = color

    def square(self):
        return self.radius * self.radius * math.pi

    def __repr__(self):
        return 'Супер красивый {} {} цвета с радиусом {}. А плошадь его равна {}'.format(
            Circle.get_figure_type(),
            self.fc.colorproperty,
            self.radius,
            self.square()
        )
