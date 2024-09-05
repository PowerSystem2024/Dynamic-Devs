import javax.swing.*;

/*
 * Ejercicio 2 (uso JOptionPane):
 * pedir números hasta que se ingrese uno negativo y calcular la media
 * */
public class Ejercicio2JOptionPane {
    public static void main(String[] args) {
        int num, sum = 0, count = 0;
        float avr = 0;
        num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un valor entero. Para salir ingrese uno negativo."));
        while (num >= 0) {
            sum += num;
            count++;
            avr = (float) sum / count;
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro valor o un valor negativo para salir."));
        }
        JOptionPane.showMessageDialog(null, "Se ha ingresado un valor negativo.\nFin del programa." +
                "\nNúmeros positivos ingresados: " + count + "\nSumatoria: " + sum + "\nMedia aritmética: " + avr);
    }
}
