//Ejercicio 7: Leer 10 enteros ordenados crecientemente. Leer N y buscarlo en la tabla. Se debe mostrar la posicion en que se encuentra, si no esta, indicarlo con un mensaje.
package ejercicios;

import java.util.Scanner;


public class ejercicio7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numeros = new int[10];

        // Leer los 10 números enteros en orden creciente
        System.out.println("Introduce 10 números enteros en orden creciente:");
        for (int i = 0; i < numeros.length; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();
        }

        // Leer el número N a buscar
        System.out.print("\nIntroduce el número que deseas buscar en la tabla: ");
        int n = scanner.nextInt();

        // Buscar el número N en el arreglo
        int posicion = -1;
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] == n) {
                posicion = i;
                break;
            }
        }

        // Mostrar el resultado
        if (posicion != -1) {
            System.out.println("El número " + n + " se encuentra en la posición " + posicion + ".");
        } else {
            System.out.println("El número " + n + " no se encuentra en la tabla.");
        }
    }
}
