package operaciones;

public class Aritmetica {
    int a;
    int b;

    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("Resultado = " + resultado);
    }

    public int sumarConRetorno() {
        /*
        int resultado = a + b;
        return resultado;
        */
        return this.a + this.b;
    }

    public int sumarConArgumentos(int a, int b) {
        this.a = a;
        this.b = b;
        // return a + b;
        return this.sumarConRetorno();
    }
}