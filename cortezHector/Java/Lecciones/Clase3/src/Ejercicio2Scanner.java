import java.util.Scanner;

/*
 * Ejercicio 2 (uso Scanner):
 * pedir números hasta que se teclee uno negativo y
 * mostrar cuántos números se han introducido.
 * */
public class Ejercicio2Scanner {
    public static void main(String[] args) {
        Scanner consoleInput = new Scanner(System.in);
        int num, numCount = 0;
        do {
            System.out.print("Ingrese un valor entero: ");
            num = consoleInput.nextInt();
            if (num >= 0) { // evitamos contar el valor negativo que corta el ciclo
                numCount++;
            }
        } while (num >= 0);
        System.out.println("\nSe ha ingresado un valor negativo.\nFin del programa");
        System.out.println("Valores positivos ingresados: " + numCount);
    }
}