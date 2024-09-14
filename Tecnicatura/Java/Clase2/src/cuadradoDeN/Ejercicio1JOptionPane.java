package cuadradoDeN;

import javax.swing.*;

/*
* Ejercicio 1: Cuadrado deun número (con JOptionPane)
* */
public class Ejercicio1JOptionPane {
    public static void main(String[] args) {
        int num, result; //declaramos las variable necesarias

        //usamos JOptionPane para pedir el ingreso de un valor
        num = Integer.parseInt(JOptionPane.showInputDialog("Digite un número para calcular su cuadrado"));

        while (num >= 0) { //repetir hasta que sea menor a cero
            result = num * num;
            JOptionPane.showMessageDialog(null, "El cuadrado de : " + num + " es " + result);

            //volvemos a pedir ingreso de valor
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número"));
        }

        JOptionPane.showMessageDialog(null, "Se ha ingresado un valor negativo. Finalizó el programa.");
    }
}
