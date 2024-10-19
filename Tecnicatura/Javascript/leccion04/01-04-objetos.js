let x = 10; //variable tipo primitiva
console.log(x.lenght);
console.log("Tipos primitivos");
//Objeto
let persona = {
    nombre: "Noelia",
    apellido: "Cruz",
    email: "ana.noe.cruz@hotmail.com",
    edad: 38,
    nombreCompleto: function(){ //metodo o funcion en Javascript
        return this.nombre + " " + this.apellido;
    }
};

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);

console.log(persona.nombreCompleto());

console.log("Ejecutando con un objeto");
let persona2 = new Object(); //deve crear un nuevo objeto en memoria
persona2.nombre = "Juan";
persona2.direccion = "SiempreViva 123";
persona2.telefono = "123657894";
console.log(persona2.telefono);

console.log("Creamos un nuevo objeto");
console.log(persona["apellido"]); //accedemos como si fuera un arreglo

console.log("Usamos el ciclo for in");
//For in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

console.log("Cambiamos y eliminamos un error");
persona.apellida = "Betancud"; //cambiamos dinamicamente un valor del objeto
delete persona.apellida; //eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto
//Num 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log("Distintas formas de imprimir un objeto: forma 1");
console.log(persona.nombre +", "+ persona.apellido);

//Num2: a traves de un ciclo for in
console.log("Distintas formas de imprimir un objeto: forma 2");
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Num 3: La funcion Object.values()
console.log("Distintas formas de imprimir un objeto: forma 3");
let personaArray = Object.values(persona);
console.log(personaArray);

//Num 4: Utilizaremos el metodo JSON.stringify
console.log("Distintas formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);



