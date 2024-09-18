package cuadradoDeN;

import java.util.Scanner;

/*
 * Ejercicio 1: cuadrado de un número (con Scanner)
 * */
public class Ejercicio1Scanner {
    public static void main(String[] args) {
        // iniciamos un objeto scanner para el ingreso de datos por consola
        Scanner scanner = new Scanner(System.in);

        // variables necesarias para el ejercicio
        int num, result;

        do {
            System.out.print("Ingrese un número entero para calcular su cuadrado: ");
            num = scanner.nextInt(); // leemos el valor

            // rompemos el ciclo si el valor es menor a cero
            if (num < 0) {
                break;
            }

            // elevamos el número al cuadrado para obtener facilmente el resultado
            result = num * num;

            //mostramos el resultado por consola
            System.out.println("El cuadrado de " + num + " es " + result + ".");
        } while (true);

        System.out.println("Se ha finalizado el programa porque se ha ingresado el número NEGATIVO.");
    }
    /*
     * El algoritmo podría acortarse y acelerar su ejecución reemplazando el ciclo do-while por un
     * ciclo while, evitando así el uso de un condicional interno que rompe el ciclo.
     * Se ha decidido optar por este enfoque para poder hacer uso de la polabra reservada break.
     * */
}