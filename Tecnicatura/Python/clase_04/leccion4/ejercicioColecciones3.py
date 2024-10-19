# Ejercicio 3: agregar personajes a una lista
# Escriba un programadonde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dunadan del Norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

# Creamos la lista

personajes = [] # creamos una lista vacia

# Creamos diccionarios
p = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dunadan del Norte'}
personajes.append(p) # agregamos a la lista un personaje

p = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(p)

p = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(p)

print(personajes) 

# agregando más personajes
p = {'Nombre': 'Frodo Baggins', 'Clase': 'Portador del Anillo', 'Raza': 'Hobbit'}, {'Nombre': 'Gimli', 'Clase': 'Guerrero', 'Raza': 'Enano'}, {'Nombre': 'Éowyn', 'Clase': 'Guerrera', 'Raza': 'Humana'}

personajes.append(p)
print(personajes)


