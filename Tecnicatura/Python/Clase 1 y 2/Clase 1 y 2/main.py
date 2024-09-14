#COLECCIONES EN PYTHON

'''
#lista = Pablo, Liliana, Natalia, Osvaldo, Ariel

nombres = ['Pablo','Ariel', 'Eduardo', 'Mauro']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])

print(nombres[0:2]) #recorre 2 valores, la posicion 0 y 1
#ir del inicial de la lisla al indice (sin incluirlo)
print(nombres[ :3])
#desde el indice indicado hasta el final
print(nombres[1: ])
#modificamos un valor
nombres[3] = 'Magali'
print(nombres)
#iterar una lista
for nombre in nombres : #nombre es singular, la lista es plural
    print(nombre)
else:
    print('se acabaron los elementos de la lista')

#preguntamos la cantidad de elementos
print(len(nombres)) #kle pasamos como parametro la lista

#agregamos elementos
nombres.append('Marcelo')
print(nombres)

#insetrtar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3,'Lucio')
print(nombres)

#eliminamos elemento
nombres.remove('Alberto')
print(nombres)

#eliminar el ultimo elemento
nombres.pop()
print(nombres)

#eliminar un indice especifico
del nombres[1] #
print(nombres)

#eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#elminar la lis
del nombres
print(nombres)
'''

#EJERCICIOS
#1 iterar un rangode 0 a 10 e imprimir numeros digisibles entre 3
print("Rango de 0 a 10 con numeros divisibles entre 3")
for i in range(11):
    if i % 3 == 0:
        print(i)

#2 crear un rango de numeros de 2 a 6 e imprimelos
print("Rango con valores de inicio = 2 y fin = 6")
rango = range(2,7)
for i in rango:
    print(i)

#3 crea un rango de 3 a 10 pero con incrmento de 2 en 2
print("Rango con valores de inicio = 3 y fin = 10 con incremento 2")
for i in range(3,11,2):
    print(i)

#TUPLA
#EN LAS LISTAS SE PUEDEN MODIFICAR, EN LAS TUPLAS NO
cocina = ('cuchara','cuchillo', 'tenedor')
print(cocina)
print(len(cocina))

#Acceder a un elemento, para esto utilizamos cochetes no parentesis
print(cocina[0])
#mostrar de manera inversa
print(cocina[-1])
#acceder a un rango
print(cocina[0:2])

verduras =("papa",) #una tupla necesita aunq sea de un elemento, la coma, sino es una cadena (str)

#recorremos los elemento de la tupla
for cocinar in cocina:   #Print esta usando \n para saltos de lineas
    print(cocinar, end="/")   #usamos end= para eliminar los saltos de lineas

cocinaLista =list(cocina) #ESTO ES PARA MODIFICAR UNA TUPLA, SE PUEDE PASAR A LISTA, SE MODIFICA Y LUEGO SE VUELVE A TUPLA
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("\n", cocina)

#TIPO SET
planetas = {"Marte","Jupiter","Venus","Neptuno"}
print(planetas)
print(len(planetas))
#revisar si un elemento existe (boolean)
print("Jupiter" in planetas) #Tener en cuenta mayusculas, acentos, todo, tiene que ser igual
#agregar un elemento
planetas.add("Tierra")
print(planetas)
planetas.remove("Neptuno")
print(planetas)
planetas.discard("tierra")
print(planetas)
planetas.discard("Tierra")
print(planetas)

#DICCIONARIO EN PY
#una llave y un valor
#dict(key, value)
diccionario ={
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}
print(diccionario)
print(diccionario["IDE"])
#MODIFICAR
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario.get('IDE'))
