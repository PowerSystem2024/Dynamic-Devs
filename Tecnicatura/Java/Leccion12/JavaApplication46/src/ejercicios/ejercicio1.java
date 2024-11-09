//Ejercicio 1: Leer 10 numeros enteros, guardarlos en un arreglo. Debemos mostrarlos en el siguiente orden: El primero, el ultimo, el segundo, el penultimo, el tercero, etc
package ejercicios;
import java.util.Scanner;

public class ejercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numeros = new int[10];

        // Leer los 10 números y almacenarlos en el arreglo
        System.out.println("Ingresa 10 numeros enteros:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Numero " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();
        }

        // Mostrar los números en el orden solicitado
        System.out.println("Numeros en el orden solicitado:");
        for (int i = 0; i < 5; i++) {
            System.out.print(numeros[i] + " ");              // Imprime el elemento desde el principio
            System.out.print(numeros[9 - i] + " ");          // Imprime el elemento desde el final
        }
    }
}

