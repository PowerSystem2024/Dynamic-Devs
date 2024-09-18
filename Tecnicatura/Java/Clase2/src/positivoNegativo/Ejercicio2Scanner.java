package positivoNegativo;

import java.util.Scanner;

/*
* Ejercicio 2: Determinar si un número ingresado es positivo o negativo.
* Repetir hasta que se ingrese un cero (0)
*
* Uso de Scanner
* */
public class Ejercicio2Scanner {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        //variables necesarias
        int num;

        do {
            System.out.print("Ingrese un número entero: ");
            num = input.nextInt();

            //determinamos si es positivo o negativo y se muestra mensaje correspondiente
            if (num > 0) {
                System.out.println("El valor ingresado es POSITIVO.");
            } else if (num < 0) {
                System.out.println("El valor ingresado es NEGATIVO.");
            }
        } while (num != 0);

        //mensaje de saida
        System.out.println("Se ha ingresado el valor CERO (0).\n" + "Fin del programa.");
    }
}
