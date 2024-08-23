package CicloWhile;


public class EjercicioWhile01 { //Ciclo While es el mas importante en java
    public static void main(String[] args) {
        var conteo = 0;//Inferencia de tipos
        while(conteo < 3){
            System.out.println("conteo = " + conteo);
            conteo++;//Vamos aumentando en uno la variable
        }
        
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador <= 7);
        // Tambien para reemplazar el var contando ponemos usar int i que seria la i de iterador
         //Etiquetas label
        inicio: // Solo funcionan con break y continue
        for( var contando = 0; contando < 7; contando++){
            if(contando % 2 == 0){
            System.out.println("contando = " + contando);
            break inicio; //Rompe el ciclo
            }
        }
        for( var contando = 0; contando < 7; contando++){
            if(contando % 2 != 0){ //Pedimos todos los numeros pares hasta el 7
            continue; // vamos a la siguiente iteracion, continua en el ciclo.
            }
            System.out.println("contando = " + contando);
        }
    }
}
