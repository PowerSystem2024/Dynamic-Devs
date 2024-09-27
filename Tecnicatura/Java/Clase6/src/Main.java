public class Main {
    public static void main(String[] args) {
        /*
         * Paso por valor:
         * una variable declarada fuera del alcance de una función
         * que pasada como argumento a dicha función, no modifica su estado
         * inicial.
         * Estas variables están almacenadas en el stack
         * */
        double variable = 10;
        System.out.println("Variable = " + variable); // 10
        changeVariableValue(variable);
        System.out.println("Variable = " + variable); // sigue siendo 10

        System.out.println();

        /*
         * Paso por referencia:
         * variables almacenadas en el heap que contienen un valor x
         * y que pasadas como argumento a una función
         * hará que su valor inicial cambie.
         * Se puede observar este comportamiento de cambio de valor en
         * atributos pertenecientes a objetos.
         * */
        Person person = new Person("Héctor", "Cortez");
        person.fullName(); // Héctor Cortez
        changeObjectAttributeValue(person);
        person.fullName(); // Se ha cambiado y no es el mismo de un principio

        System.out.println();

        /*
        * Uso de palabra return y null
        * */
        Person nullPerson = null;
        changeNameInPerson(nullPerson);
        // nullPerson.fullName(); no es posible porque el objeto no está inicializado
        Person notNullPerson = new Person();
        changeNameInPerson(notNullPerson);
        notNullPerson.fullName(); // el objeto está inicializado y sus atributos contienen valores
    }

    public static void changeObjectAttributeValue(Person person) {
        System.out.print("Nombre completo al principio del método: ");
        person.fullName();
        System.out.print("Nombre completo al final del método: ");
        person.firstName = "Carla";
        person.lastName = "Doe";
        person.fullName();
    }

    public static void changeVariableValue(double variable) {
        System.out.println("Valor del argumento al inicio del método: " + variable);
        variable = variable * variable;
        System.out.println("Valor del argumento al final del método: " + variable);
    }

    public static Person changeNameInPerson(Person person) {
        if (person == null) {
            System.out.println("El objeto pasado como argumento es nulo.");
            return null;
        }
        person.firstName = "Teresa";
        person.lastName = "de Calcuta";
        return person;
    }
}
