//Ejercicio 3: Leer 5 elementos numericos que se introduciran ordenados de forma creciente. Estos los guardaremos en una tabla de tamaño 10. Leer un numero N, e insertarlo en el lugar adecuado para que la tabla continue ordenada
package ejercicios;
import java.util.Scanner;

public class ejercicio3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] tabla = new int[10];
        int numElementos = 5;

        // Leer los 5 números ordenados de forma creciente
        System.out.println("Introduce 5 números en orden creciente:");
        for (int i = 0; i < numElementos; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            tabla[i] = scanner.nextInt();
            if (i > 0 && tabla[i] < tabla[i - 1]) {
                System.out.println("Por favor, ingresa los números en orden creciente.");
                i--; // Repetir el ingreso si el orden es incorrecto
            }
        }

        // Leer el número N a insertar
        System.out.print("Introduce el número a insertar en la tabla: ");
        int numero = scanner.nextInt();

        // Insertar el número en la posición adecuada
        int posicion = numElementos;
        for (int i = 0; i < numElementos; i++) {
            if (numero < tabla[i]) {
                posicion = i;
                break;
            }
        }

        // Desplazar los elementos a la derecha para hacer espacio para el nuevo número
        for (int i = numElementos; i > posicion; i--) {
            tabla[i] = tabla[i - 1];
        }

        // Insertar el nuevo número en la posición encontrada
        tabla[posicion] = numero;
        numElementos++; // Incrementar el número de elementos en la tabla

        // Mostrar la tabla actualizada
        System.out.println("Tabla después de insertar el número:");
        for (int i = 0; i < numElementos; i++) {
            System.out.print(tabla[i] + " ");
        }
    }
}
