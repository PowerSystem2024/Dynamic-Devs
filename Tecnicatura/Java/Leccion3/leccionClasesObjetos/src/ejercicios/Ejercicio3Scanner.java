package ejercicios;

import java.util.Random;
import java.util.Scanner;

/*
 * Ejercicio 3 (uso Scanner):
 * realizar un juego para adivinar un número,
 * para ello generar un número aleatorio entre 0 y 100,
 * luego ir pidiendo números indicando "es mayor" o "es menor"
 * según sea mayor o menor el número a adivinar.
 * El programa termina cuando el usuario acierta y mostramos
 * el número de intentos hechos.
 * */
public class Ejercicio3Scanner {
    public static void main(String[] args) {
        // instanciamos un objeto de la clase Random para generar valores aleatorios
        Random randomGenerator = new Random();
        // 101 = (entre) 0 y 100
        int guessNumber = randomGenerator.nextInt(101);
        int value, attempts = 0;
        String playAgain = "y";
        Scanner consoleInput = new Scanner(System.in);
        do {
            System.out.print("\n¡Adivine el número!\nIngrese un valor entero: ");
            value = consoleInput.nextInt();
            attempts++;
            // si gana, se muestran los intentos, el número adivinado y si quiere volver a jugar
            if (value == guessNumber) {
                System.out.print("\n¡Felicidades!\nHas adivinado el número en " +
                        attempts + " intento/s\n" +
                        "El número a adivinar era: " + guessNumber +
                        "\n¿Quieres volver a jugar? Si[y] - No[n]: ");
                playAgain = consoleInput.next(); // esperamos respuesta para continuar jugando o no...
                attempts = 0; // reiniciamos los intentos si quiere volver a jugar
                guessNumber = randomGenerator.nextInt(101); // nuevo número para el nuevo juego
            } else {
                if (value > guessNumber) {
                    System.out.println("Es menor...");
                } else {
                    System.out.println("Es mayor...");
                }
            }
        } while (playAgain.equals("y"));
    }
}
