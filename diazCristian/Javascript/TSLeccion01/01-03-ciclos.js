// Ciclos, para programar un ciclo necesitamos una variable. Ej: While
//While: Si la condicion es verdadera entra, si es falsa sale del codigo.
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;
}
console.log("Fin de ciclo while");

// Ciclo do While, su difernecia es que el codigo que esta dentro del bloque del ciclo se va a ejecutar todo y luego va a revisar su condicion
//do while: Revisa la condicion y entra al do while
let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log("Fin del ciclo do while")

//Ciclo For: A diferencia del ciclo while, do while que nosotros debiamos incrementar  la variable contador
// Para que no terminaramos en un bucle infinito y se bloquee. EL ciclo for tendra definido los pasos. No necesitamos variable

for(let contando = 0 ;contando < 3 ; contando++){
    console.log(contando);
}
console.log("Fin del ciclo for")

//Palabra reservada Break
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando); //Muestra todos los pares
        break; // El break estaria diciendo que romperia al encontrar el primer numero par es decir el 0 
    }
}
console.log("Termina el ciclo terminara  al encontrar el primer numero par");

//Continue la palabra continue preguntamos si el numero no es par, en caso de que no sea par que siga con la siguiente iteracion.
// Si es diferente a cero !== Es decir el continue esta ignorando todos los pares, entonces salen todos los pares.
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue; // Esto va a continuar a la siguiente iteracion      
    }
    console.log(contando);
}
console.log("Termina el ciclo");

//Etiquetas Labels: Nos permite ir a una parte del programa que deseemos:
inicio: // etiqueta label inicio No esta recomendada por los algoritmos.
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        break inicio; // Etiqueta label inicio    
    }
    console.log(contando);
}
console.log("Termina el ciclo");



