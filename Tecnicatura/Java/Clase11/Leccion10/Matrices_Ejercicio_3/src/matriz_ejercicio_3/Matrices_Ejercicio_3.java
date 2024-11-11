/*
Ejercicio 3: Crear y cargar  una matriz de tamaño 3x3, transponerla y mostrarla.
 */
package matriz_ejercicio_3;

import java.util.Scanner;

   
public class Matrices_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz [][] = new int [3][3];
        
        
        System.out.println("Rellenar matriz: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println("Matriz ["+i+"]["+j+"]:");
                matriz[i][j] = entrada.nextInt();                
            }            
        }
        
        System.out.println("");
        
        System.out.println("Matriz original: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matriz[i][j]+" ");
            }
            
            System.out.println("");           
        }
        
        System.out.println("");
        
        //Matriz Transpuesta
        System.out.println("Matriz transpuesta: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matriz[j][i]+" ");
            }
            
            System.out.println(" ");
        }
        
        System.out.println(" ");
    }
}
