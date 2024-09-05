// Funciones en JS
function sum(a, b) {
	let result = a + b;
	console.log(result);
}
sum(2, 3); // 5

// Hoisting: las funciones se pueden llamar antes de ser declaradas
rest(5, 3); // 2
function rest(a, b) {
	let result = a - b;
	console.log(result);
}

// uso de palabra reservada return
function mult(a, b) {
	return a * b;
}
let result = mult(2, 3); // 6
console.log(result);

// Funciones anónimas o de tipo expresión
let div = function (a, b) {
	return a / b;
}; // no se puede llamar antes de ser declarada
result = div(6, 2); // 3
console.log(result);

// Funciones de tipo self-invoking
(function (a, b) {
	console.log(a * b);
})(2, 3); // 6

// Tipo de dato Function
console.log(typeof sum); // function

// Funcions flecha o arrow functions
let pot = (a, b) => a ** b;
result = pot(2, 3); // 8
console.log(result);

// Uso de arguments (con hoisting incluido)
result = sumAll(1, 2, 3, 4, 5); // 15
console.log(result);
function sumAll() {
	let sum = 0;
	for (let i = 0; i < arguments.length; i++) {
		sum += arguments[i];
	}
	return sum;
}

// Paso por valor en funciones
let x = 5;
function changeValue(a) {
	a = 10;
}
changeValue(x);
console.log(x); // 5

// Paso por referencia en funciones
const obj = { name: "Juan" };
function changeObject(o) {
	o.name = "Pedro";
}
changeObject(obj);
console.log(obj.name); // Pedro
