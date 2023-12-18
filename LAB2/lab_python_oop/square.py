from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, length, color):
        self.length = length
        super().__init__(color, self.length, self.length)

    def square(self):
        return (self.length**2)

    def __repr__(self):
        return 'Супер красивый {} {} цвета с длиной сторон {}. А плошадь его равна {}'.format(
            Square.get_figure_type(),
            self.fc.colorproperty,
            self.length,
            self.square()
        )