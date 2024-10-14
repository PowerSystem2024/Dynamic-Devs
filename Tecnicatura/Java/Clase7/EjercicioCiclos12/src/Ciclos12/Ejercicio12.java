package Ciclos12;
import javax.swing.JOptionPane;

public class Ejercicio12 {
    public static void main(String[] args) {
        int num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        long factorial = 1;
        for(int i=1;i<=num;i++){
            factorial *=i;
        }
        JOptionPane.showMessageDialog(null, "\nEl factorial del numero ingresado es: "+factorial);
    }
}
