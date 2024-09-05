import javax.swing.*;

/*
 * Ejercicio 1 (uso JOptionPane): Pedir números hasa que se teclee un cero.
 * Mostrar la suma total de los números.
 * */
public class Ejercicio1JOptionPane {
    public static void main(String[] args) {
        int num, sum = 0;
        num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un valor entero, para salir ingrese cero"));
        while (num != 0) {
            sum += num;
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro valor entero, o cero para salir"));
        }
        JOptionPane.showMessageDialog(null, "Se ha ingresado el cero.\nFin del programa\n" +
                "Suma total de los números: " + sum);
    }
}
