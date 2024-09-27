package ejercicio;

public class BoxClient {
    public static void main(String[] args) {
        Box box1 = new Box(15, 11, 35);
        var result = box1.calculateVolume();
        System.out.println("Volumen de la caja 1: " + result);

        Box box2 = new Box();
        box2.height = 10;
        box2.width = 10;
        box2.depth = 25;
        result = box2.calculateVolume();
        System.out.println("Volumen de la caja 2: " + result);
    }
}
