package test;
import dominio.Persona;
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        //Modificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        
        System.out.println("persona1 con su nombre modificado = " + persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo = " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano = " + persona1.isEliminado());
        //Tarea: Crear otro objeto de tipo persona, asignar valores de manera iniciarl
        //y imprimir, luego modificar sus valores y volver a imprimir
        Persona persona2 = new Persona("Maria", 45.500, true);
        System.out.println("persona2 antes de modificar = " + persona2);
        
        // Modificar valores
        persona2.setNombre("Lucia");
        persona2.setSueldo(50.000);
        persona2.setEliminado(false);
        //Aca ya lo muestra con el tostring
        System.out.println("persona2 despues de modificar = " + persona2);


        System.out.println("persona1:  = " + persona1.toString()); //tostring
    }
    
}
