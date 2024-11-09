//Ejercicio 9: Crear una matriz de "marco" de tamaño 5x5: todos sus elementos deben ser 0, salvo los bordes que deben ser 1. Mostrarla
package ejercicios;


public class ejercicio9 {
    public static void main(String[] args) {
        int tamaño = 5;
        int[][] matriz = new int[tamaño][tamaño];

        // Crear la matriz con el marco
        for (int i = 0; i < tamaño; i++) {
            for (int j = 0; j < tamaño; j++) {
                // Verificar si está en el borde de la matriz
                if (i == 0 || i == tamaño - 1 || j == 0 || j == tamaño - 1) {
                    matriz[i][j] = 1;
                } else {
                    matriz[i][j] = 0;
                }
            }
        }

        // Mostrar la matriz
        System.out.println("Matriz de marco 5x5:");
        for (int i = 0; i < tamaño; i++) {
            for (int j = 0; j < tamaño; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}
