package ejercicios;

import javax.swing.*;

/*
 * Ejercicio 9 (uso JOptionPane):
 * pedir día, mes y año de una fecha e indicar si la fecha es correcta,
 * suponiendo que los meses son de 30 días
 * */
public class Ejercicio9JOptionPane {
    public static void main(String[] args) {
        int days, month, year; // variables necesarias
        JOptionPane.showMessageDialog(null, "A continuación, indique una fecha para verificar si es válida.");
        days = Integer.parseInt(JOptionPane.showInputDialog("Ingrese los días."));
        month = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes."));
        year = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año."));
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
            JOptionPane.showMessageDialog(null, "\nLa fecha " + days + '/' + month + '/' + year + " es válida.");
        } else {
            JOptionPane.showMessageDialog(null, "\nLa fecha " + days + '/' + month + '/' + year + " NO es válida.");
        }
    }
}
