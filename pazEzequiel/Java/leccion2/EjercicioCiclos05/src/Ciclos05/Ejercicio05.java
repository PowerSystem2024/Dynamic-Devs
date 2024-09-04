
package Ciclos05;
import javax.swing.JOptionPane;

public class Ejercicio05 {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); //Esto genera un numero aleatorio
        do{
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numero mayor: ");
                
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numero menor: ");
            }
            else{
                JOptionPane.showMessageDialog(null, "FELICIDADES, has adivinado el numero");
            }
            conteo++;
        }while(numero!= aleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el numero en: "+conteo+" intentos");
        
    }
    
}
