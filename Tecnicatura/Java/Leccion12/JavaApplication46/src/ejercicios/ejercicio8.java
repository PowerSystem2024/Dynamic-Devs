//Ejercicio 8: Utilizando dos matrices de tamaaño 5x9 y 9x5, cargar la primera y trasportarla a la segunda
package ejercicios;

import java.util.Scanner;


public class ejercicio8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int filasA = 5;
        int columnasA = 9;
        int[][] matrizA = new int[filasA][columnasA];
        int[][] matrizB = new int[columnasA][filasA]; // Transpuesta de matrizA
        
        // Cargar valores en la matrizA
        System.out.println("Introduce los elementos de la matriz de tamaño 5x9:");
        for (int i = 0; i < filasA; i++) {
            for (int j = 0; j < columnasA; j++) {
                System.out.print("Elemento [" + i + "][" + j + "]: ");
                matrizA[i][j] = scanner.nextInt();
            }
        }
        
        // Realizar la transposición: matrizA -> matrizB
        for (int i = 0; i < filasA; i++) {
            for (int j = 0; j < columnasA; j++) {
                matrizB[j][i] = matrizA[i][j];
            }
        }
        
        // Mostrar la matrizA original
        System.out.println("\nMatriz Original (5x9):");
        for (int i = 0; i < filasA; i++) {
            for (int j = 0; j < columnasA; j++) {
                System.out.print(matrizA[i][j] + "\t");
            }
            System.out.println();
        }
        
        // Mostrar la matrizB transpuesta
        System.out.println("\nMatriz Transpuesta (9x5):");
        for (int i = 0; i < columnasA; i++) {
            for (int j = 0; j < filasA; j++) {
                System.out.print(matrizB[i][j] + "\t");
            }
            System.out.println();
        }
        
        scanner.close();
    }
}
