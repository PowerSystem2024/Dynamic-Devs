/*
Ejercicio2: Leer un numero e indicar si es positivo o negativo
El proceso se repetira hasta que se introduzca un cero
Hacer este ejercicio con la clase JOptionPane
*/
package Ciclos02;   
import javax.swing.JOptionPane;
public class Ciclo02 {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            while(numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El numero " + numero + " Es POSITIVO");
            }
            else{
                JOptionPane.showMessageDialog(null, "El numero " + numero + " Es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
       JOptionPane.showMessageDialog(null, "El numero "+ numero + " Finaliza el programa");         
    }
}


