import java.util.Scanner;

public class QuadraticEquationSolver {

    public static void main(String[] args) {
        QuadraticEquationSolver solver = new QuadraticEquationSolver();
        double[] coefficients = solver.getCoefficients();
        solver.solve(coefficients[0], coefficients[1], coefficients[2]);
    }

    private double[] getCoefficients() {
        Scanner scanner = new Scanner(System.in);
        double[] coefficients = new double[3];
        System.out.println("Введите коэффициенты для квадратного уравнения (a, b, c):");

        for (int i = 0; i < 3; i++) {
            while (true) {
                try {
                    System.out.printf("Введите коэффициент %c: ", (char)('A' + i));
                    coefficients[i] = Double.parseDouble(scanner.nextLine());
                    break;
                } catch (NumberFormatException e) {
                    System.out.println("Это не цифра! Введи цифру");
                }
            }
        }

        return coefficients;
    }

    private void solve(double a, double b, double c) {
        double discriminant = b * b - 4 * a * c;

        if (discriminant > 0) {
            double x1 = (-b + Math.sqrt(discriminant)) / (2 * a);
            double x2 = (-b - Math.sqrt(discriminant)) / (2 * a);
            System.out.println("x1 = " + x1);
            System.out.println("x2 = " + x2);
        } else if (discriminant == 0) {
            double x = -b / (2 * a);
            System.out.println("x = " + x);
        } else {
            System.out.println("Нет действительных решений");
        }
    }
}