// En un arreglo podemos agregar diferntes tipos de valores, pueden ser numericos, tipo string
//let autos = new Array("Ferrari", "Renault", "BMW"); Esta es una sintaxis vieja, ya no se usa.
const autos = ["Ferrari", "Renault", "BMW"]; // Sintaxis actual
console.log(autos);

//Forma manual de ubicar la posicion del elemento en el array
console.log(autos[0]);
console.log(autos[2]);
//Recorremos los elementos de un arreglo con un ciclo for
for(let i = 0; i < autos.length; i++){
    console.log(i+" : "+autos[i]);
}

// Modificar los elementos del array. Le pedimos que modifique la posicion 1 del array
autos[1] = "Volvo";
console.log(autos);

//Agregar  un elemento al array (push)
autos.push("Audi"); //Agregamos el elemento al FINAL del array
console.log(autos);

//Agregar un elemento al array usando el largo. Tambien se agrega al final
autos[autos.length] = "Porche";
console.log(autos);

//Agregar un elemento al array teniendo CUIDADO. Si no se tiene en cuenta creamos un espacio vacio "undefined"
autos[6] = "Renault"
console.log(autos);

//Como preguntar si es un array
console.log(Array.isArray(autos)); //Devuelve un booleano

console.log(autos instanceof Array); //Preguntamos si la variable es una instancia de la clase Array
