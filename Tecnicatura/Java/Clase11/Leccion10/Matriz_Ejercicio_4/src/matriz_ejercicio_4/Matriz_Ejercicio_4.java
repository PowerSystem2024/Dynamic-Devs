/*
Ejercicio 4: Crear una matriz de tamaño 7x7 y rellenarla de forma que los elementos de la
diagonal principal sean 1 y el resto 0.
 */
package matriz_ejercicio_4;

import java.util.Scanner;

public class Matriz_Ejercicio_4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][] = new int [7][7];
        
        
        //Llenando la matriz
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                if(i == j){
                    matriz[i][j] = 1;
                }
                else{
                    matriz[i][j] = 0;
                }
                
            }
            
        }
        
        System.out.println("Mostrando matriz completa: ");
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                 System.out.print(matriz[i][j]+"");
            }
            
            System.out.println("");
        }
        
        System.out.println(" ");
    }
}
