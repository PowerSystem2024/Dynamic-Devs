
package Operaciones;


public class PruebaAritmetica {
    public static void main(String[] args) {
        var a =91;//variable local -> memoria stack
        int b = 34;
        miMetodo();//Llamamos el otro metodo nuevo
        Aritmetica aritmetica1 =new Aritmetica();
        aritmetica1.a=3;//en el caso de los atributos el alcance es mayor que una variable local
        aritmetica1.b=7;
        aritmetica1.sumarNumero();
        
        //para almacenar un objeto o atributos se utiliza memoria heap
        int respuesta = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + respuesta);
        
        respuesta = aritmetica1.sumarConArgumento(12, 26);
        System.out.println("Resultado con argumento = " + respuesta);
        
        System.out.println("aritmetica1 b: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5,8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        //aritmetica1 = null; nunca utilizr esto
        //System.gc(); método para limpiar residuos, es pesado, no utilizar
        Persona persona = new Persona("Ariel", "Betancud");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona nombre: "+persona.apellido);
    }
    //Modularidad creamos un nuevo metodo
    public static void miMetodo(){
        //int a = 10; //una variabla esta limitada al metodo donde se crea(si no la defino aca
        //me surje un error, por que la variable definida en el main anterior no tienen influencia
        //en este metodo. 
        System.out.println("Ahqui hay otro metodo");
    }
}

//creamos una nueva clase
class Persona{ //Dentro de la misma plantilla solo puede existir una sola clase con el modificador
                //de acceso public. En cambio no se pone nada, por que automaticamente se asigna 
                    //default 
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ //Constructor
        super();//LLama al constructor de la clase Padre object
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;//usamos this para indicar que esa variable esta apuntando a los atributos de esta clase
        System.out.println("Objeto persona usando this: "+this );
    }
    
}

class Imprimir{
    public Imprimir(){
        super();//el contstructor de la clase padre para reservar memoria
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this): "+this);
    }
}