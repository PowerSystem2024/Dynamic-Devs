# Los diccionarios en Python son como objetos que contienen
# elementos en conjunto llave -> valor
# Los diccionarios no poseen índice. Para acceder a un elemento se utiliza su llave
from Colecciones import mySet

myDictionary = {
    'Value 1': 'Hello world',
    'Value 2': 42,
    'Value 3': True,
}
print(len(myDictionary))  # longitud del diccionario
print(myDictionary)  # contenido

# obtener un elemento del diccionario
print(myDictionary['Value 1'])
print(myDictionary.get('Value 2'))

# modificar el valor almacenada en una llave
myDictionary['Value 1'] = '¡Hola Mundo!'
print(myDictionary)

# recorrer un diccionario mostrando las llaves/keys
for key in myDictionary:
    print(key, end=" ")

print()

# recorrer un diccionario mostrando los valores de las llaves
for value in myDictionary.values():
    print(value, end=" ")

print()

# recorrer el diccionario con llave y valor
for item in myDictionary.items():
    print(item, end=" ")

print()

# comprobrar existencia de elemento
print('Value 2' in myDictionary) # true

# agregar un nuevo par llave/valor
myDictionary['Value 4'] = False
print(myDictionary)

# eliminar un elemento
myDictionary.pop('Value 4')
print(myDictionary)

# vaciar el diccionario
myDictionary.clear()
print(myDictionary) # output -> {}