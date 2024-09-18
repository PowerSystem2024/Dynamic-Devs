package positivoNegativo;

import javax.swing.*;

/*
 * Ejercicio 2: Determinar si un número ingresado es positivo o negativo.
 * Repetir hasta que se ingrese un cero (0)
 *
 * Uso de JOptionPane
 * */
public class Ejercicio2JOptionPane {
    public static void main(String[] args) {
        int num; //variables necesarias
        do {
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número entero"));
            if (num < 0) { //si es positivo...
                JOptionPane.showMessageDialog(null, "El valor ingresado es NEGATIVO.");
            } else if (num > 0) { //si es negativo...
                JOptionPane.showMessageDialog(null, "El valor ingresado es POSITIVO.");
            }
        } while (num != 0); //si es cero, fin del bucle
        JOptionPane.showMessageDialog(null, "Se ha ingresado el cero (0).\nFin del programa");
    }
}
