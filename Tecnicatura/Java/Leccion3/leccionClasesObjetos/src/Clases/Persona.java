
package Clases;


public class Persona {
    //Atributos de la clase (Caracteristicas)
    String nombre;
    String apellido;
    
    //Métodos de la clase (Acciones)
    public void obtenerInformación(){ //en este caso nos muestra lo que tengamos guardado en los atributos
        System.out.println("Nombre = " + nombre);
        System.out.println("Apellido = " + apellido);
    }
}
