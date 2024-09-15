package ejercicios;

import javax.swing.*;

/*
 * Ejercicio 1 (uso JOptionPane):
 * pedir números hasta que se introduzca un cero.
 * Para cada uno indicar si es par o impar
 * */
public class Ejercicio1JOptionPane {
    public static void main(String[] args) {
        int num = 1;
        while (num != 0) {
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un valor entero"));
            if (num != 0) { // solo mostramos mensaje cuando el valor no es cero
                if (num % 2 == 0) {
                    JOptionPane.showMessageDialog(null, "El valor " + num + " es PAR.");
                } else {
                    JOptionPane.showMessageDialog(null, "El valor " + num + " es IMPAR.");
                }
            }
        }
        JOptionPane.showMessageDialog(null, "Se ha ingresado el cero.\nFin del programa");
    }
}
