class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self.nombre} {self.apellido}, Edad: {self.edad}")

    @property
    def nombre(self):  # Método getter
        print("Estamos utilizando el método get")
        return self._nombre  

    @nombre.setter
    def nombre(self, nombre):  # Método setter
        print("Estamos utilizando el método setter")
        self._nombre = nombre  

    @property
    def apellido(self):  # Getter para apellido
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Setter para apellido
        self._apellido = apellido

    @property
    def edad(self):  # Getter para edad
        return self._edad 
    
    @edad.setter
    def edad(self, edad):  # Setter para edad
        self._edad = edad

    def __del__(self):
        print(f"Persona2 : {self._nombre} {self._apellido} {self._edad}")

if __name__ == "__main__":
    persona1 = Persona2("Ariel", "Betancud", 41)
    # Llamar al método getter
    print(persona1.nombre)  
    persona1.nombre = "Juan Pedro"
    print(persona1.nombre)
    persona1.mostrar_detalles()  # Llama directamente al método, sin print

    # Atributo edad modificado por setter
    print(persona1.edad)

    # Crear tres objetos más
    persona2 = Persona2("Flor", "Romero", 23)
    persona2.nombre = "Florencia"
    persona2.apellido = "Romery"
    persona2.edad = 22
    persona2.mostrar_detalles()  # Método mostrar_detalles

    persona3 = Persona2("Caro", "Felisa", 21)
    persona3.nombre = "Carolina"
    persona3.apellido = "Felix"
    persona3.edad = 31
    persona3.mostrar_detalles()  # Método mostrar_detalles

    persona4 = Persona2("Naty", "Lucero", 35)
    persona4.nombre = "Natalia"
    persona4.apellido = "Lucero"
    persona4.edad = 35
    persona4.mostrar_detalles()  # Método mostrar_detalles

    print(__name__)
