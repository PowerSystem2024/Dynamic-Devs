package ejercicios;

import javax.swing.*;

/*
 * Ejercicio 8 (uso JOptionPane):
 * pedir un número N y mostrar los valos de 1 a N
 * */
public class Ejercicio8JOptionPane {
    public static void main(String[] args) {
        int num;
        num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número entero y se mostrará una sucesión"));
        while (num < 1) {
            num = Integer.parseInt(JOptionPane.showInputDialog("Debe ser un entero positivo y mayor a cero"));
        }
        for (int i = 1; i <= num; i++) {
            JOptionPane.showMessageDialog(null, i);
        }
    }
}

/*
 * una forma más óptima de mostrar la sucesión final
 * es con la siguiente porción de código:
 *
 * String str = "";
 * for (int i = 1; i <= num; i++ {
 *     str = str.concat(i + ' ');
 * }
 * JOptionPane.showMessageDialog(null, str);
 *
 * lo que da como resultado una única salida de datos para mostrar
 * en un único frame del JOptionPane.
 * */
