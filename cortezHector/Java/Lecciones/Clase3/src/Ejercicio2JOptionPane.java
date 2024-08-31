import javax.swing.*;

/*
 * Ejercicio 2 (uso JOptionPane):
 * pedir números hasta que se teclee uno negativo y
 * mostrar cuántos números se han introducido.
 * */
public class Ejercicio2JOptionPane {
    public static void main(String[] args) {
        int num = 0, numCount = 0;
        while (num >= 0) {
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número entero"));
            if (num >= 0) { // evitamos contar el valor negativo que finaliza el ciclo
                numCount++;
            }
        }
        // mostramos los datos por ventana
        JOptionPane.showMessageDialog(null, "Se ha ingresado un valor negativo.\n" +
                "Fin del programa.\n\n" +
                "Valores ingresados: " + numCount);
    }
}
