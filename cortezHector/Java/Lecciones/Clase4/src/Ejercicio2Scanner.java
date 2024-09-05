import java.util.Scanner;

/*
 * Ejercicio 2 (uso Scanner):
 * pedir números hasta que se ingrese uno negativo y calcular la media
 * */
public class Ejercicio2Scanner {
    public static void main(String[] args) {
        Scanner consoleInput = new Scanner(System.in);
        int num, count = 0, sum = 0;
        float avr = 0;
        System.out.print("Ingrese un valor entero. Para finalizar ingrese un valor negativo: ");
        num = consoleInput.nextInt();
        while (num >= 0) {
            sum += num;
            count++;
            avr = (float) sum / count;
            System.out.print("Ingrese otro valor. Para salir ingrese un valor negativo: ");
            num = consoleInput.nextInt();
        }
        System.out.println("\nSe ha ingresado un valor negativo.\nFin del programa." +
                "\nNúmeros positivos ingresados: " + count + "\nSumatoria: " + sum + "\nMedia aritmética: " + avr);
    }
}
