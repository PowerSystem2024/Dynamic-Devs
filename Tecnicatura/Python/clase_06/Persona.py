class Persona:   # creamos una clase
    def __init__(self, nombre, apellido, edad):   # se lo llama metodo init Dunder - estos son atributos del metodo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Jose', 'Villalba', 38)

print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona("Osvaldo", "Giordanini", 45)

print(f'El objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido}, su edad es {persona2.edad}')

print(f'El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido}, su edad es {persona1.edad}')

# Modificando los atributos
print('\n# Modificando los atributos')
persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40

print(f'El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido}, su edad es {persona1.edad}')

# Los atributos son las características
# Los métodos son: el comportamiento que van a tener los objetos (acciones)

# Metodo != Funcion. Metodo esta asociado a una clase, la funcion no.
print('\n# Mostramos los objetos a traves de un metodo')
persona1.mostrar_detalle()
persona2.mostrar_detalle()

