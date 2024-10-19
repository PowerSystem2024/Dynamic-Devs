//let persona3 = new Persona('Carla', 'Ponce');

//Siempre se hereda automaticamente de la clase Object ( es la clase padre de todos los objetos en javascript)
class Persona extends Object{  //Clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto(){
        return this._nombre+" "+this._apellido;
    }

    //SObreescribiendo el metodo de la clase Object(padre)
    toString(){
        //Se aplica polimorfismo
        return this.nombreCompleto();
    }
}

class Empleado extends Persona{  //clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }

    //Sobreescritura
    nombreCompleto(){
        return super.nombreCompleto()+", "+this._departamento;
    }

}

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);

console.log(persona1.apellido);
persona1.apellido = 'Martinez';
console.log(persona1.apellido);
console.log(persona1.nombre+" "+persona1.apellido);
//console.log(persona1);

let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);

console.log(persona2.apellido);
persona2.apellido = 'Rodriguez';
console.log(persona2.apellido);
console.log(persona2.nombre+" "+persona2.apellido);
//console.log(persona2);

let empleado1 = new Empleado('Miqueas', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombre);
console.log(empleado1.nombreCompleto());

//Polimorfismo
console.log(empleado1.toString());
console.log(persona1.toString());//Se llama dependiendo al objeto que estamos apuntando
