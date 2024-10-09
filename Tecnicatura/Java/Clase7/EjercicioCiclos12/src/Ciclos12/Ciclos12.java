/*
Ejercicio 12: Pedir un numero y calcular su factorial
*/
package Ciclos12;
import java.util.Scanner;

public class Ciclos12 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        int num = entrada.nextInt();
        int factorial = 1;
        for(int i=1;i<=num;i++){
            factorial *= i;
        }
        System.out.println("\nEl factorial del numero ingresado es: "+factorial);
    }
}
