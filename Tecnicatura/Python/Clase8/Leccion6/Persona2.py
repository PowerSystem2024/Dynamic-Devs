class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property # Decorador
    def nombre(self): #Metodo getter
        print('Estamos utilizando el metodo get')
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):# metodo Setter
        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @property  # Decorador
    def apellido(self):  # Metodo getter
        print('Estamos utilizando el metodo get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # metodo Setter
        print('Estamos utilizando el metodo set')
        self._apellido = apellido

    @property  # Decorador
    def edad(self):  # Metodo getter
        print('Estamos utilizando el metodo get')
        return self._edad

    @edad.setter
    def edad(self, edad):  # metodo Setter
        print('Estamos utilizando el metodo set')
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud',41)
    print(persona1.nombre) #llamamos al metodo getter .. puede usarse persona1.nombre sin parentesis
    print(persona1.apellido)
    print(persona1.edad)

    persona1.nombre = 'Juan Pedro' #reconoce automaticamente el metodo sett
    print(persona1.nombre)
    print(persona1.mostrar_detalles())
    # Atributo read-only seria la edad por que no tiene metodo sett
    #print(persona1.edad)

    #Tarea crear tres objetos mas, utilizando los metodos getter and setter
    #para modificar, y mostrar los cambios con el metodo mostrar_detalles

    #Objeto numero 1
    persona2 = Persona2('Flor','Romero',23)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Forencia'
    persona2.apellido = 'Romery'
    persona2.edad = 22

    print(persona2.mostrar_detalles())

    #Objeto numero2
    persona3 = Persona2('caro','Felisa',21)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Carolina'
    persona3.apellido = 'Felix'
    persona3.edad = 31

    print(persona3.mostrar_detalles())

    #Objeto numero3
    persona4 = Persona2('Naty','Lucer', 35)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Natalia'
    persona4.apellido = 'Lucero'
    persona4.edad = 33

    print(persona4.mostrar_detalles())

    print(__name__)