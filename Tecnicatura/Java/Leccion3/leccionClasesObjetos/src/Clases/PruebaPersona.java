
package Clases;


public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona(); //Llamamos al constructor, creamos el objeto,y reserva memoria para este(hexadecimal)
        persona1.nombre = "Mauro";//El valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "Vignati";//Definimos tanto nombre como apellido(atributos)
        persona1.obtenerInformación();//ejecutamos el metodo, de la clase persona, 
                                      //que nos muestra, en este caso, los atributos
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);//al no darle ningun valor a sus atributos, nos va a mostrar el numero asignado de memoria
        System.out.println("persona1 = " + persona1);//junto con el nombre del paquete y la clase a la cual pertenece.
        persona2.obtenerInformación();
        persona2.nombre = "Ariel";
        persona2.apellido = "Betancud";
        persona2.obtenerInformación();
    }
}
