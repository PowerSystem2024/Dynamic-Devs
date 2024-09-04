miFuncion(8,2) //Esto se lo conoce como hosting

function miFuncion(a, b){
    //console.log("Sumamos: "+ (a + b));
    return a + b;
}
//Llamando la funcion
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);

//Declaramos una funcion de tipo expresión o anonima
let x = function(a, b){return a + b}; //Nceesita cierre con punto y coma
resultado = x(5, 6); // Al llamarla se pone la variable y parentesis
console.log(resultado);

//Funciones de tipo self e invoking esta funcion no se reutiliza es decir no la podemos volver a llamar. Solo
//Se hace una sola vez.
(function(a,b){
    console.log("Ejecutando la funcion: "+ (a + b));
})(9, 6);

console.log(typeof miFuncion);
function miFuncionDos(a, b){ //(a,b) = parametros de la funcion
    console.log(arguments.length); // Length: Cuantos argumentos tiene la funcion?
}

miFuncionDos(5, 7, 3 , 4, ); // 5,7,3,4 Argumentos de mi funcion

//toString Lo que hacemos es asignar nuestra funcion pero como si fuera texto, agrega codigo
//de forma automatica.
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

//Funciones de flecha
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7); // Asignamos el valor a una variable
console.log(resultado);


//Resumen: Los parametros son la lsita de variables que definimos en una funcion
//Los argumentos: son los valores que pasamos cuando llamamos una funcion.
//Las funciones pueden ser definidas como objetos ya que tienen una propiedad arguments y toString
//Arguments es para poder acceder a lso diferentes valores de los parametros

//Funcion de tipo expresión
let sumar = function(a = 4 , b = 8){
    console.log(arguments[0]) // Muestra el parametro de a
    console.log(arguments[1]); // Muestra el parametro de b

    return a + b + arguments[2];
}
resultado = sumar(3, 2, 9);
console.log(resultado);

//Sumar todos los argumentos HOISTING
let respuesta = sumarTodo(5, 4, 13, 10, 8);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i]; //arguments es para arreglos
    }
    return suma;
}

//Tipos primitivos
let k = 10;
function cambiarValor(a){ //Paso por valor la variable no sufre ningun cambio.
    a = 20;
}

cambiarValor(k);
console.log(k);

//Paso por referencia esto es un objeto

const persona = {
    nombre: "Juan",
    apellido: "Lepez"
}
console.log(persona);
function cambiarValorObjeto(p1){
    p1.nombre = "Ignacio";
    p1.apellido = "Perez";
}

cambiarValorObjeto(persona);
console.log(persona);