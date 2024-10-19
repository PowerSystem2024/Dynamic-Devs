package operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        Aritmetica aritmetica = new Aritmetica();
        aritmetica.a = 3;
        aritmetica.b = 7;
        aritmetica.sumarNumeros();
        int resultado = aritmetica.sumarConRetorno();
        System.out.println("resultado = " + resultado); // 10
        resultado = aritmetica.sumarConArgumentos(10, 7);
        System.out.println("resultado = " + resultado); // 17
    }
}
