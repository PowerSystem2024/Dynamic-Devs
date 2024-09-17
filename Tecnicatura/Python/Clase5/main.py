"""
Comenzamos con funciones
mi_funcion() mo se puede llamar antes de definir a una funcion
Definimos una funcion
"""
def mi_funcion():
    print("Saludos a todos los alumnos de la Tecnicatura")

mi_funcion() #Estamos llamando a la funcion, puede llamarse n cantidad de veces

#Desempaquetado de listas o list unpacking
def show(name, lastName):
    print(name+" "+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) #Pasamos uno por uno los datos de la lista a la funcion
show(*person)
person2 = ("Osvaldo", "Giordanini")
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1,2,3,4,5] #Aún con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break #Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termino")

# List comprehension, lista de compresión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] #Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)
#Paso de argumentos(funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que ven a través del canal de youtube")
    print(f"Nombre:  {name}, Apellido: {lastName}",)
mi_funcion2("Jorge", "Lucero")
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analia", "Pedrosa")

#La palabra return en funciones
#Creamos una funcion para sumar
def sumar(a, b):
    return a+b
#Resultado = sumar(78,22)
#print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55, 45)}")

def sumar2(a = 0, b = 0): #Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22,66)}")

#Argumento, variables en funciones
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres("Lucas", "Jose", "Claudia", "Rosa", "María")
listarNombres("Marcos", "Daniel", "Romina", "Pepe", "Marcela", "Carlos")

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f"{llave} : {valor}")

#listarTerminos()
listarTerminos(IDE = "Integrated Development Enviroment", Pk="Primary Key")
listarTerminos(Nombre = "Lionel Messi")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombre2 = ["Tito", "Pedro", "Carlos"]
desplegarNombres(nombre2)
desplegarNombres("Carla")
#desplegarNombres(10, 11) No es un objeto iterable
desplegarNombres((10, 11))#La convertimos a una tupla, en un solo elemento no olvidarse la coma
desplegarNombres([22, 55])#Convertimos en una lista

#Funciones recursivas
def factorial(numero):
    if numero == 1:
        return 1 #Caso base
    else:
        return numero * factorial(numero-1)#Caso recursivo
resultado = factorial(5)
print(f"El factorial del numero 5: {resultado}")

numeroFactorial = int(input("Digite un numero para calcular su factorial: "))
resultado = factorial(numeroFactorial)
print(f"El factorial del numero {numeroFactorial} es: {resultado}")