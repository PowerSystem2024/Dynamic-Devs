package ejercicios;

import javax.swing.*;
import java.util.Random;

/*
 * Ejercicio 3 (uso JOptionPane):
 * realizar un juego para adivinar un número,
 * para ello generar un número aleatorio entre 0 y 100,
 * luego ir pidiendo números indicando "es mayor" o "es menor"
 * según sea mayor o menor el número a adivinar.
 * El programa termina cuando el usuario acierta y mostramos
 * el número de intentos hechos.
 * */
public class Ejercicio3JOptionPane {
    public static void main(String[] args) {
        // instanciamos un objeto de la clase Random para generar valores aleatorios
        Random randomGenerator = new Random();
        // 101 = (entre) 0 y 100
        int guessNumber = randomGenerator.nextInt(101);
        int value, attempts = 0;
        String playAgain = "y";
        do {
            value = Integer.parseInt(JOptionPane.showInputDialog("¡Adivine el número!\nIngrese un valor entero"));
            attempts++; // inicia el conteo de intentos
            // si gana, se muestran los intentos, el número adivinado y si quiere volver a jugar
            if (value == guessNumber) {
                playAgain = JOptionPane.showInputDialog("¡Felicidades!\nHas adivinado el número en " +
                        attempts + " intento/s\n" +
                        "\nEl número a adivinar era: " + guessNumber +
                        "\n¿Quieres volver a jugar? Si[y] - No[n]");
                attempts = 0; // reiniciamos los intentos si quiere volver a jugar
                guessNumber = randomGenerator.nextInt(101); // nuevo número para el nuevo juego
            } else {
                if (value > guessNumber) {
                    JOptionPane.showMessageDialog(null, "Es menor...");
                } else {
                    JOptionPane.showMessageDialog(null, "Es mayor...");
                }
            }
        } while (playAgain.equals("y"));
    }
}
