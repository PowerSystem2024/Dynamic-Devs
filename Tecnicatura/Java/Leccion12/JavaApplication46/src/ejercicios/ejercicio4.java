//Ejercicio 4: Leer por teclado una tabla de 10 elementos numericos enteros y una pocision entre (0 y 9). Eliminar el elemento situado en la posicion dada sin dejar huecos.
package ejercicios;
import java.util.Scanner;

public class ejercicio4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tabla = new int[10];

        // Leer los 10 elementos de la tabla
        System.out.println("Introduce 10 números enteros:");
        for (int i = 0; i < tabla.length; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            tabla[i] = scanner.nextInt();
        }

        // Leer la posición a eliminar (validación entre 0 y 9)
        int posicion;
        do {
            System.out.print("Introduce la posición a eliminar (0 a 9): ");
            posicion = scanner.nextInt();
            if (posicion < 0 || posicion > 9) {
                System.out.println("Posición inválida. Debe estar entre 0 y 9.");
            }
        } while (posicion < 0 || posicion > 9);

        // Eliminar el elemento sin dejar huecos
        for (int i = posicion; i < tabla.length - 1; i++) {
            tabla[i] = tabla[i + 1];
        }
        
        // Establecer el último elemento como 0 para representar la eliminación
        tabla[tabla.length - 1] = 0;

        // Mostrar la tabla resultante
        System.out.println("Tabla después de eliminar el elemento en la posición " + posicion + ":");
        for (int i = 0; i < tabla.length; i++) {
            System.out.print(tabla[i] + " ");
        }
    }
}
