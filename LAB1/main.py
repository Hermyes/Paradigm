import math

class QuadraticEquationSolver:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def get_coefficient(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Это не цифра! Введи цифру")

    def get_inputs(self):
        print("Quadratic equation solver: ax^2 + bx + c = 0")
        self.a = self.get_coefficient("Введите коэффициент A: ")
        self.b = self.get_coefficient("Введите коэффициент B: ")
        self.c = self.get_coefficient("Введите коэффициент C: ")

    def solve_quadratic(self):
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if discriminant > 0:
            x1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
        elif discriminant == 0:
            x = -self.b / (2 * self.a)
            print(f"x = {x}")
        else:
            print("Нет действительных корней.")

    def execute(self):
        self.get_inputs()
        if self.a == 0:
            print("Это не квадратное уравнение (коэффициент A равен нулю).")
        else:
            self.solve_quadratic()

if __name__ == "__main__":
    solver = QuadraticEquationSolver()
    solver.execute()
