/*
Ejercicio 11: Diseñar un programa que muestre el producto de los 10 primeros
numeros impares. Hacerlo con JOptionPane
 */
package Ciclos11;

import javax.swing.JOptionPane;


public class Ciclos11 {
    public static void main(String[] args) {
        long producto = 1;
        for(int i = 1; i<=20;i+=2){//apunta a los numeros impares
            producto *= i;
        }
        JOptionPane.showMessageDialog(null, "El producto de los 10 primeros numeros pares es: "+producto);
    }
}
