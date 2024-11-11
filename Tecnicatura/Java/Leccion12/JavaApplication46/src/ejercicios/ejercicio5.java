//Ejercicio5: Leer 10 enteros en una tabla. Guardar en otra tabla los elementos pares de la primera, y a continuacion los elementos imares
package ejercicios;
import java.util.Scanner;


public class ejercicio5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tablaOriginal = new int[10];
        int[] tablaSeparada = new int[10];
        int contadorPares = 0;
        int contadorImpares = 0;

        // Leer los 10 elementos de la tabla
        System.out.println("Introduce 10 números enteros:");
        for (int i = 0; i < tablaOriginal.length; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            tablaOriginal[i] = scanner.nextInt();
        }

        // Separar pares e impares
        for (int i = 0; i < tablaOriginal.length; i++) {
            if (tablaOriginal[i] % 2 == 0) {
                tablaSeparada[contadorPares++] = tablaOriginal[i];
            } else {
                tablaSeparada[9 - contadorImpares++] = tablaOriginal[i];
            }
        }

        // Mostrar la tabla separada con pares al inicio e impares al final
        System.out.println("\nTabla con pares primero y luego impares:");
        for (int i = 0; i < tablaSeparada.length; i++) {
            System.out.print(tablaSeparada[i] + " ");
        }
    }
}
