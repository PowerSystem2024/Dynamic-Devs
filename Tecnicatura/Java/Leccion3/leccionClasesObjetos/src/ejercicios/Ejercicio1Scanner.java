package ejercicios;

import java.util.Scanner;

/*
 * Ejercicio 1 (uso Scanner):
 * pedir números hasta que se introduzca un cero.
 * Para cada uno indicar si es par o impar
 * */
public class Ejercicio1Scanner {
    public static void main(String[] args) {
        Scanner consoleInput = new Scanner(System.in);
        int num;
        do {
            System.out.print("Ingrese un valor entero: ");
            num = consoleInput.nextInt();
            if (num != 0) { // solo mostramos mensaje cuando el valor no es cero
                if (num % 2 == 0) {
                    System.out.println("El valor " + num + " es PAR.\n");
                } else {
                    System.out.println("El valor " + num + " es IMPAR.\n");
                }
            }
        } while (num != 0);
        System.out.println("\nSe ha ingresdo en valor 0.\nFin del programa");
    }
}
