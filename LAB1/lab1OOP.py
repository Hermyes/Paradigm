import math

class BiqSolver:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
    def coeficentGetter(self):
        while True:
            try:
                a = float(input("Введите коэффициент А: "))
                break
            except ValueError:
                print("Это не цифра! Введи цифру")

        while True:
            try:
                b = float(input("Введите коэффициент B: "))
                break
            except ValueError:
                print("Это не цифра! Введи цифру")

        while True:
            try:
                c = float(input("Введите коэффициент C: "))
                break
            except ValueError:
                print("Это не цифра! Введи цифру")
        self.a = a
        self.b = b
        self.c = c

    def Solver(self):
        discriminant = self.b ** 2 - 4 * self.a * self.c

        if discriminant > 0:
            x1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            print("x1 = ", x1)
            print("x2 = ", x2)
        elif discriminant == 0:
            x = -self.b / (2 * self.a)
            print("x=", x)
        else:
            return None



bSol = BiqSolver()
bSol.coeficentGetter()
bSol.Solver()
