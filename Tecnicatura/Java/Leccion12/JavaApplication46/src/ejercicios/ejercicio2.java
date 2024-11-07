//Ejercicio2: Leer por teclado dos tablas de 10 numeros enteros y mezclarlas en una tercera de la forma: el 1 de A, el 1 de B, el 2 de B, etc
package ejercicios;
import java.util.Scanner;

public class ejercicio2 {
     public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tablaA = new int[10];
        int[] tablaB = new int[10];
        int[] tablaC = new int[20];

        // Leer los 10 números de la tabla A
        System.out.println("Ingresa 10 números para la tabla A:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Número " + (i + 1) + " de la tabla A: ");
            tablaA[i] = scanner.nextInt();
        }

        // Leer los 10 números de la tabla B
        System.out.println("Ingresa 10 números para la tabla B:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Número " + (i + 1) + " de la tabla B: ");
            tablaB[i] = scanner.nextInt();
        }

        // Mezclar las tablas en la tabla C
        int j = 0;
        for (int i = 0; i < 10; i++) {
            tablaC[j++] = tablaA[i]; // Añadir elemento de tabla A
            tablaC[j++] = tablaB[i]; // Añadir elemento de tabla B
        }

        // Mostrar la tabla C
        System.out.println("Tabla C mezclada:");
        for (int i = 0; i < 20; i++) {
            System.out.print(tablaC[i] + " ");
        }
    }
}
