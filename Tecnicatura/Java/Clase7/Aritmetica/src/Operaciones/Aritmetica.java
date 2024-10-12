
package Operaciones;


public class Aritmetica {
    //Atributos de clase
    int a;
    int b;
    //El constructor es un metodo especial
    public Aritmetica(){//constructor1
        System.out.println("Se esta ejecutando el constructor numero 1");
    }
    //Sobrecarga de constructores
    public Aritmetica(int a, int b){//constructor2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el constructor 2");
    }
    //metodo
    public void sumarNumero(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        int resultado = a+b;
        return resultado;// o, a + b, directamente
    }
    
    public int sumarConArgumento(int arg1, int arg2){
        a = arg1;
        b = arg2;
        //return a + b;
        return sumarConRetorno();
    }
}
