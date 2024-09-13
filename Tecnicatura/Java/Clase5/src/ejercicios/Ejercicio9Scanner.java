package ejercicios;

import java.util.Scanner;

/*
 * Ejercicio 9 (uso Scanner):
 * pedir día, mes y año de una fecha e indicar si la fecha es correcta,
 * suponiendo que los meses son de 30 días
 * */
public class Ejercicio9Scanner {
    public static void main(String[] args) {
        Scanner consoleInput = new Scanner(System.in);
        int days, month, year; // variables necesarias
        System.out.println("Ingrese una fecha y se verificará si es correcta.\n" +
                "Indique los siguiente datos.");
        System.out.print("Días: ");
        days = consoleInput.nextInt();
        System.out.print("Mes: ");
        month = consoleInput.nextInt();
        System.out.print("Año: ");
        year = consoleInput.nextInt();
        /*
         * El año se toma como válido a partir de la creación
         * del calendatio Gregoriano (1582 d.C.)
         * La cantidad de días es válida si contiene de 1 a 30 días máximo.
         *
         * Ejemplos:
         * 31/06/1998 -> no es válida
         * 20/01/2003 -> es válida
         * 19/13/2043 -> no es válida
         * 27/10/3050 -> es válida
         * 12/09/1309 -> no es válida
         * */
        if ((days >= 1 && days <= 30) && (month >= 1 && month <= 12) && year >= 1582) {
            System.out.println("\nLa fecha " + days + '/' + month + '/' + year + " es válida.");
        } else {
            System.out.println("\nLa fecha " + days + '/' + month + '/' + year + " NO es válida.");
        }
    }
}
