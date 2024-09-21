// métodos get y set de un objeto
let person = {
    firstName: 'John',
    lastName: 'Doe',
    get getFirstName() {
        return this.firstName;
    },
    get getLastName() {
        return this.lastName;
    },
    fullName: function () {
        return this.firstName + ' ' + this.lastName;
    },
    set setFirstName(value) {
        this.firstName = value;
    },
    set setLastName(value) {
        this.lastName = value;
    }
}

console.log(person.getFirstName); // John Doe
person.setFirstName = 'Jane';
person.setLastName = 'Smith';
console.log(person.fullName()); // Jane Smith

// constructores de objetos
function Person(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
    // método dentro del constructor
    this.fullName = function () {
        return this.firstName + ' ' + this.lastName;
    }
}
const p1 = new Person('Héctor', 'Cortez');
const p2 = new Person('Francisco', 'Orieta');
console.log(p1.fullName()); // Héctor Cortez
console.log(p2.fullName()); // Francisco Orieta

// formas de crear objetos
// 1. mediante el uso de new Object()    
let object1 = new Object();
// 2. mediante el uso de la sintaxis de objeto
let object2 = {};

// ejemplo con String
let str1 = new String('Hola');
let str2 = 'Hola'; // string literal

// ejemplo con Number
let num1 = new Number(10);
let num2 = 10; // number literal

// ejemplo con Boolean
let bool1 = new Boolean(true);
let bool2 = true; // boolean literal

// ejemplo con Array
let arr1 = new Array();
let arr2 = []; // array literal

// ejemplo con funciones
let func1 = new function () { };
let func2 = function (x, y) {
    return x + y;
}

/* 
Uso de Prototype:
Prototype es un objeto que tiene cada función en JavaScript.

en este caso se verá cómo se puede agregar un nuevo atributo a un objeto
usando su constructor.
Pero antes se le agregará un atributo a un objeto ya creado
y se accederá a su valor.
Luego se tomará otro objeto creado con el mismo constructor
y se verá que no tiene el atributo agregado.
*/
p1.email = 'example@email.com';
console.log(p1.email); // example@email.com
console.log(p2.email); // undefined

/* 
Usando Prototype en un constructor:
esto permite que todos los objetos creados con el constructor
tengan disponible el atributo agregado.
Es importante mencionar que el atributo agregado con Prototype 
puede tener (o no) un valor por defecto.
*/
Person.prototype.email = 'default_email@example.com';
console.log(p1.email);
console.log(p2.email);

/* 
Uso de call():
esto permite llamar a un método de un objeto con otro objeto.
En este ejemplo se llama al método fullName perteneciente
al objeto p3 pasando como argumento en la función call() al objeto p4.
*/
let p3 = {
    firstName: 'Juan',
    lastName: 'Pérez',
    fullNameAndTitle: function (title) {
        return title + ' ' + this.firstName + ' ' + this.lastName;
    }
}
let p4 = {
    firstName: 'María',
    lastName: 'Gómez'
}
console.log(p3.fullNameAndTitle('Lic.')); // Lic. Juan Pérez
console.log(p3.fullNameAndTitle.call(p4, 'Ing.')); // Ing. María Gómez

/* 
Uso de apply():
Este método nos permite llamar a un método que no se encuentra 
definido en cierto objeto. 
Apply lee el arreglo y lo está asignando como argumento. 
La única diferencia entre call() y apply() es que a call() se le pasan 
directamente los argumentos y apply() va necesitar que tengamos 
a disposición un arreglo en el que estarán ingresados como 
elementos de ese arreglo los argumentos necesarios para 
el método que los está requiriendo.
*/
let p5 = {
    firstName: 'Juan',
    lastName: 'Pérez',
    showPersonalData: function (city, country) {
        return this.firstName + ' ' + this.lastName + ', ' + city + ', ' + country;
    }
}
let p6 = new Person('Lucila', 'Schuz');
// arreglo con los argumentos  para el método showPersonalData
let arr = ['Buenos Aires', 'Argentina'];
console.log(p5.showPersonalData.apply(p6, arr)); // Lucila Schuz, Buenos Aires, Argentina
