// formas de declarar un arreglo
let arreglo1 = new Array(1, 2, 3, 4, 5); // ya no se usa tanto
const arreglo2 = [1, 2, 3, 4, 5]; // forma más común
console.log("Arreglo 1 (forma antigua):\n" + arreglo1);
console.log("Arreglo 2 (actualidad):\n" + arreglo2);

// acceder a los elementos del arreglo
console.log("Elemento 0 del arreglo 2: " + arreglo2[0]);

// recorrer un arreglo con el ciclo for-i
console.log("Recorrer arreglo 2 con ciclo for-i:");
for (let i = 0; i < arreglo2.length; i++) {
  console.log("índice " + i + ": " + arreglo2[i]);
}

// modificar los elementos de un arreglo
console.log("Elemento 0 del arreglo 2: " + arreglo2[0]);
arreglo2[0] = 10;
console.log("Elemento 0 del arreglo 2: " + arreglo2[0]);

// agregar elementos a un arreglo
console.log("Arreglo 2 antes de agregar un elemento: " + arreglo2);
arreglo2.push(6); // agrega un elemento al final del arreglo
console.log("Arreglo 2 después de agregar un elemento: " + arreglo2);

// otras formas de agregar elementos a un arreglo
console.log("Arreglo 2 antes de agregar un elemento: " + arreglo2);
arreglo2[arreglo2.length] = 7; // agrega un elemento al final del arreglo
console.log("Arreglo 2 después de agregar un elemento: " + arreglo2);

// saber qué tipo de dato es un arreglo
console.log("Tipo de dato de arreglo2: " + typeof arreglo2); // object
// otras formas de saber qué tipo de dato es un arreglo
console.log("Es arreglo2 un arreglo: " + Array.isArray(arreglo2)); // true
let resutl = arreglo2 instanceof Array; // true
console.log("Es arreglo2 instancia de un arreglo: " + resutl);
