class Persona:
    def __init__(self, nombre,apellido,dni,edad, *args, **kwargs): # se lo llama metodo Init Dunder
        self.__nombre = nombre# Evita modificacion, igual no se usa tanto
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sujerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f'La clase Persona tiene los siguientes datos: {self.__nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los otros datos importantes son: {self.kwargs}')

persona1 = Persona('Ariel','Betancud',1234518, 40)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

print(f'El objeto 1 de la clase persona es: {persona1.nombre} {persona1.apellido}, su ead es: {persona1.edad}')

persona2 = Persona('Osvaldo','Giordanini',24266125, 45)
print(f'El objeto 2 de la clase persona es: {persona2.nombre} {persona2.apellido}, su ead es: {persona2.edad}')

persona1.nombre = 'liliana'
persona1.apellido = 'Buccella'
persona1.edad=40
print(f'El objeto 1 modificado de la clase persona es: {persona1.nombre} {persona1.apellido}, su ead es: {persona1.edad}')

#Los atributos son caracteristicas
#Los metodos son  el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dara error

persona1.telefono = '44334251' # Creamos un atributo de un objeto, el cual es solopara el objeto persona1
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}')

persona3 = Persona('Rogelio', 'Romero',325154, 22,'Telefono','2604264235','Calle Lopez', 823,'Manzana',77,'Casa',18, Altura=1.83, Peso= 105,CFavorito='Azul',Auto='Citroen',Modelo=2021)
persona3.mostrar_detalle()
print(persona3._dni) # se puede acceder igual por que es sujerido el encapsulamiento, por lo que se puede pero no se debe usar asi
# persona3.__nombre #Esta totalmente ecapsulado, no deja
