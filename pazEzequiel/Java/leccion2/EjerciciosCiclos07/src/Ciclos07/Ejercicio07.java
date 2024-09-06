
package Ciclos07;

import javax.swing.JOptionPane;

public class Ejercicio07 {
        public static void main(String[] args) {
        
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){
            suma += numero;
            conteo++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
        if(conteo ==0){
            JOptionPane.showMessageDialog(null, "\nError, la division entre cero no existe");
        }
        else{
            promedio = (float)suma/conteo;
            JOptionPane.showMessageDialog(null, "\nEl promedio es: "+promedio);
        }
    }
    
}
