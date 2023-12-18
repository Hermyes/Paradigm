import numpy as np
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    r = Rectangle(8, 8, "синего")
    c = Circle(8, "зеленого")
    s = Square(8, "красного")
    print(r)
    print(c)
    print(s)

    print(np.zeros([2, 3]))

if __name__ == '__main__':
    main()

