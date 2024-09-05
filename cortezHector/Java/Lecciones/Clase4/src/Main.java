public class Main {
    public static void main(String[] args) {
        // creación de instancia por medio del constructor
        Persona persona = new Persona();
        // se establecen valores para los atributos del objeto
        persona.nombre = "Héctor";
        persona.apellido = "Cortez";
        // llamado a método propio de la clase
        persona.obtenerInformacion();
    }
}