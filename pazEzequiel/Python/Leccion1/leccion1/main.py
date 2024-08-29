nombres = ["Naty", "Osvaldo", "Lily", "Ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])#podemos recorrer mediante el uso de negativos
print(nombres[0:2])
#Ir del inicio de la lista hasta el indice (sin incluir)
print(nombres[ :3])#Da por entendido el compilador que es del cero en adelante
print(nombres[1: ])
#Modificamos un valor dentro de la lista
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
#Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

#Preguntamos cuantos elementos tiene una lista
print(len(nombres)) #Le pasamos como parametro la lista
#Agregamos un elemento a una lista
nombres.append("Marcelo")#al final de la lista
print(nombres)
#Insertamos un elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
#Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)
#Eliminar el ultimo elemento
nombres.pop()
print(nombres)
#Eliminar un indice especifico
del nombres[2]
print(nombres)
#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)
#Eliminar la lista
#del nombres

#Ejercicio1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
#Ejemplo de ejercucion: 0,3,6,9
print("Rango de 0 a 10 con numero divisibles por 3")
x = range(0,10,3)
for i in x:
    print(i)
#Ejercicio2: Crear un rango de numeros de 2 a 6 e impremelos
#Ejemplo de ejecucion: 2,3,4,5,6
print("Rango de 2 a 6")
y = range(2,7)
for i in y:
    print(i)
#Ejercicio3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
#Ejemplo de ejecucion: 3,5,7,9
print("Rango con valores de inicio=3, fin=10 y incremento=2")
z = range(3,10,2)
for i in z:
    print(i)

#Definimos una tupla
cocina = ("Cuchara", "Cuchillo", "Tenedor")
print(len(cocina))

#Acceder a un elemento, para esto utilizamos corchetos no parentesis
print(cocina[0])
#Mostrar de manera inversa
print(cocina[0:2])
#Acceder a un rango
print(cocina[0:2])

#Ejemplo
verduras = ("papa",)
#De lo contrario solo seria un tipo de str cadena

#Recorremos los elementos de una tupla
for cocinar in cocina: #Print esta usando \n pars saltos de lineas
    print(cocinar, end=" ") #Usamos end para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("\n", cocina)

# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
#Crear una lista que solo incluya los numeros menores a 5
#e imprima por consola[1, 3, 2]

lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

#tipo set
planetas = {"Martes", "Jupiter", "Venus"}
print(len(planetas))

#Revisar si el elemento existe o no dentro de un set
print("Martes" in planetas)

#Agregar un elemento(No se puede agregar elementos duplicados)
planetas.add("Tierra")
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove("Tierra")#Esta funcion ante un mal ingreso da error
planetas.discard("Tierra")#Esta funcion no nos presenta ningun error
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas

# "Maradona":10 un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
#dict(key,value)
diccionario = {
    "IDE":"integrated development eviroment",
    "POO": "Programacion orientada a objetos",
    "SABD": "Sistema de admistracion de base de datos"
}
#Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)
#Acceder a un diccionario con la key
print(diccionario["IDE"])
#Otra forma de recuperar un elemento
print(diccionario.get("POO"))
#Modificamos elementos
diccionario["IDE"] = "Entorno de desarrollo integrado"
print(diccionario)

#Como recorrer los elementos
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)
#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)
#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():#Estamos usando una funcion
    print(termino)#Muestra solo las llaves

for valor in diccionario.values():
    print(valor)

#Comprobar la existencia de algun elemento
print("IDE" in diccionario)#Devuelve un booleano

#Agregar un elemento
diccionario["PK"] = "Primary key"
print(diccionario)

#Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)
#ELiminar un diccionario
del diccionario

#Concatenamos listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7,8,9,1]) #Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) #Funcion para ubicar en que indice esta el valor ingresado

#Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) #Cuenta cuantos valores iguales hay dentro de la lista

#Para poner al reves una lista
lista3.reverse()
print(lista3)

#Para que una lista se mulitplique repetiendo sus elementos
lista3 = lista3*2
print(lista3)

#Metodos de ordenamiento, en python ees una
lista3.sort() #Ordena ascendentemente
lista3.sort(reverse=True) #Ordena descendentemente

#Repaso de tuplas
tupla = (4,"Hola", 6.78, [1,2,78], "Hola") #distintos tipos de datos
print(tupla)

print(4 in tupla) #Accion booleana, su respuesta es de tipo booleano
#Lo que podemos usar dentro de tuplas son index. count, len
#Las tuplas pueden convertirse a listas y de listas a tuplas 