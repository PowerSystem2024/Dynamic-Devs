import java.util.Scanner;

/*
 * Ejercicio 1 (uso Scanner): Pedir números hasa que se teclee un cero.
 * Mostrar la suma total de los números.
 * */
public class Ejercicio1Scanner {
    public static void main(String[] args) {
        Scanner consoleInput = new Scanner(System.in);
        int number, sum = 0;
        System.out.print("Ingrese un valor entero, para finalizar ingrese cero: ");
        number = consoleInput.nextInt();
        while (number != 0) {
            sum += number;
            System.out.print("\nIngrese otro valor entero o cero para finalizar: ");
            number = consoleInput.nextInt();
        }
        System.out.println("\nSe ha ingresado el cero.\nFin del programa." +
                "\nSuma total de los números ingresados: " + sum);
    }
}
