//let persona3 = new Persona('Carla', 'Ponce');

//Siempre se hereda automaticamente de la clase Object ( es la clase padre de todos los objetos en javascript)
class Persona extends Object{  //Clase padre

    static contadorPersonas = 0; // Atributo estático
    // email = 'Valor default email'; // Atributo no estático

    static get MAX_OBJ() { // Este método simula una constante
        return 5;
    }

    constructor(nombre, apellido){
        super(nombre)
        this._nombre = nombre;
        this._apellido = apellido;
        if (Persona.contadorPersonas < Persona.MAX_OBJ) {
            this.idPersona = ++Persona.contadorPersonas; 
        }
        else {
            console.log('Se ha superado el máximo de objetos permitidos');
            
        }

        // console.log('Se incrementa el contador": ' +Persona.contadorObjetosPersona);
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
        return this.idPersona +' '+this._nombre+' '+this._apellido;
    }

    //SObreescribiendo el metodo de la clase Object(padre)
    toString(){
        //Se aplica polimorfismo
        return this.nombreCompleto();
    }

    static saludar() {
        console.log('Saludos desde este método static');
    }
    
    static saludar2(persona) {
        console.log(persona.nombre +' '+ persona.apellido);
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
persona1.apellido = 'Perez';
console.log(persona1.apellido);
console.log(persona1.nombre+" "+persona1.apellido);
//console.log(persona1);

let persona2 = new Persona('Martín', 'Perez');
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);

console.log(persona2.apellido);
persona2.apellido = 'Lara';
console.log(persona2.apellido);
console.log(persona2.nombre+" "+persona2.apellido);
//console.log(persona2);

let empleado1 = new Empleado('María', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombre);
console.log(empleado1.nombreCompleto());

//Polimorfismo
console.log(empleado1.toString());
console.log(persona1.toString());//Se llama dependiendo al objeto que estamos apuntando

// persona1.saludar(); No se utiliza desde el objeto
Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

// console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona);

console.log(persona1.email);
console.log(empleado1.email);
// console.log(Persona.email); No puede acceder desde la clase

console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);

let persona3 = new Persona('Carla', 'Pertosi')
console.log(persona3.toString());
console.log(Persona.contadorPersonas);

console.log(Persona.MAX_OBJ);
// Persona.MAX_OBJ = 10; No se puede modificar, ni alterar
console.log(Persona.MAX_OBJ);

let persona4 = new Persona('Franco', 'Diaz');
console.log(persona4.toString());

let persona5 = new Persona('Liliana', 'Paz');
console.log(persona5.toString());
