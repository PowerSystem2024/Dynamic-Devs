//Ejericicio 6: leer dos series de 10 enteros, que estaran ordenados crecientemente, copiar (fusionar) las dos tablas en una tercera, de forma que sigan ordenados
package ejercicios;
import java.util.Scanner;


public class ejercicio6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] serie1 = new int[10];
        int[] serie2 = new int[10];
        int[] serieFusionada = new int[20];

        // Leer la primera serie de 10 elementos ordenados crecientemente
        System.out.println("Introduce 10 números enteros en orden creciente para la primera serie:");
        for (int i = 0; i < serie1.length; i++) {
            System.out.print("Número " + (i + 1) + " de la primera serie: ");
            serie1[i] = scanner.nextInt();
        }

        // Leer la segunda serie de 10 elementos ordenados crecientemente
        System.out.println("\nIntroduce 10 números enteros en orden creciente para la segunda serie:");
        for (int i = 0; i < serie2.length; i++) {
            System.out.print("Número " + (i + 1) + " de la segunda serie: ");
            serie2[i] = scanner.nextInt();
        }

        // Fusionar ambas series en serieFusionada
        int i = 0, j = 0, k = 0;
        while (i < serie1.length && j < serie2.length) {
            if (serie1[i] < serie2[j]) {
                serieFusionada[k++] = serie1[i++];
            } else {
                serieFusionada[k++] = serie2[j++];
            }
        }

        // Agregar los elementos restantes de serie1 si los hay
        while (i < serie1.length) {
            serieFusionada[k++] = serie1[i++];
        }

        // Agregar los elementos restantes de serie2 si los hay
        while (j < serie2.length) {
            serieFusionada[k++] = serie2[j++];
        }

        // Imprimir la serie fusionada y ordenada
        System.out.println("\nSerie fusionada y ordenada:");
        for (int num : serieFusionada) {
            System.out.print(num + " ");
        }
    }
}
