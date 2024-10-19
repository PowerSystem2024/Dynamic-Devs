package ejercicios;

import java.util.Scanner;

/*
 * Ejercicio 8 (uso Scanner):
 * pedir un número N y mostrar los valos de 1 a N
 * */
public class Ejercicio8Scanner {
    public static void main(String[] args) {
        Scanner consoleInput = new Scanner(System.in);
        System.out.print("Ingrese un número positivo y se mostrará una sucesión: ");
        int num = consoleInput.nextInt();
        while (num < 1) {
            System.out.print("El valor a ingresar debe ser positivo y mayor a cero: ");
            num = consoleInput.nextInt();
        }
        int count = 0;
        System.out.println("\nMostrando valores:");
        do {
            count++;
            System.out.print(count + " ");
        } while (count < num);
    }
}
