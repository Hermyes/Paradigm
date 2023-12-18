from lab_python_oop.figure import Figure
from lab_python_oop.Сolor import Color

class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.fc = Color()
        self.fc.colorproperty = color


    def square(self):
        return self.width*self.length


    def __repr__(self):
        return 'Супер красивый {} {} цвета с длиной {} и шириной {}. А плошадь его равна {}'.format(
            Rectangle.get_figure_type(),
            self.fc.colorproperty,
            self.length,
            self.width,
            self.square()
        )


