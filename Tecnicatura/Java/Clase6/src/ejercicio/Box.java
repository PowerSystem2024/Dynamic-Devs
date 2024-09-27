package ejercicio;

public class Box {
    int height;
    int width;
    int depth;

    public Box() {
    }

    public Box(int height, int width, int depth) {
        this.height = height;
        this.width = width;
        this.depth = depth;
    }

    public int calculateVolume() {
        return height * width * depth;
    }
}
