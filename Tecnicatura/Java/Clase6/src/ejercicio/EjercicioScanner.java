package ejercicio;

import java.util.Scanner;

/*
 * Ejercicio (Scanner):
 * pedir 10 números y escribir la suma total
 * */
public class EjercicioScanner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number, sum = 0;
        for (int i = 1; i <= 10; i++) {
            System.out.print("Ingrese un número para el valor " + i + ": ");
            number = scanner.nextInt();
            sum += number;
        }
        System.out.println("Suma total de los números ingresados: " + sum);
    }
}
