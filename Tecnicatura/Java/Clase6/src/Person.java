public class Person {
    String firstName;
    String lastName;

    /*
     * Constructores y sobrecarga de constructores:
     * el constructor cumple con 3 objetivos:
     * 1. crea un objeto
     * 2. reserva espacio en memoria
     * 3. inicializa los atributos de una clase
     * */

    public Person() {
        System.out.println("Uso del constructor sin argumentos/vacío");
    }

    public Person(String firstName, String lastName) {
        System.out.println("Uso del constructor con argumentos");
        this.firstName = firstName;
        this.lastName = lastName;
    }

    /*
     * Sobrecarga de métodos:
     * se definen n métodos que se llaman de igual forma, pero se diferencian
     * debido a la cantidad de parámetros
     * */
    public void fullName() {
        System.out.println(firstName + ' ' + lastName);
    }

    public void fullName(String firstName, String lastName) {
        System.out.println(firstName + ' ' + lastName);
    }
}
