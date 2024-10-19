package ejercicio;

import javax.swing.*;

/*
 * Ejercicio (JOptionPane):
 * pedir 10 números y escribir la suma total
 * */
public class EjercicioJOptionPane {
    public static void main(String[] args) {
        int sum = 0;
        for (int i = 1; i <= 10; i++) {
            int number = Integer.parseInt(JOptionPane.showInputDialog("Valor " + i + "\nIngrese un número"));
            sum += number;
        }
        JOptionPane.showMessageDialog(null, "Suma total de los números ingresados: " + sum);
    }
}
