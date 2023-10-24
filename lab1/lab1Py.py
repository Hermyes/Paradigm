import math

def Solve(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("x1 = ", x1)
        print("x2 = ", x2)
    elif discriminant == 0:
        x = -b / (2*a)
        print("x=", x)
    else:
        return None

def CoefGetter():
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

    return a, b, c

def main():
    a, b, c = CoefGetter()
    Solve(a, b, c)

if __name__ == "__lab1Py__":
    main()
