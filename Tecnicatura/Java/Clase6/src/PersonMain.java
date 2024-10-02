public class PersonMain {
    public static void main(String[] args) {
        Person p1 = new Person();
        p1.firstName = "Person";
        p1.lastName = "One";
        Person p2 = new Person("Person", "Two");

        // uso sobrecarga de métodos
        System.out.println("Persona 1:");
        p1.fullName();
        p1.fullName(p1.firstName, p1.lastName);
        System.out.println("Persona 2:");
        p2.fullName();
        p2.fullName(p2.firstName, p2.lastName);


        // alcance de variables o scope
        String sayHi = "Hello!";
        greetings();
    }

    public static void greetings() {
        // sayHi = "Hola";
        // lo anterior no es posible ya que la variable sayHi no está
        // dentro del alcance de la función actual.
        String sayHi = "Hola!"; // esta variable no es la misma que la que está declarada en el main
        System.out.println("sayHi = " + sayHi);
    }
}