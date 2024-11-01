class Persona:   # creamos una clase
    def __init__(self, nombre, apellido, edad, dni, *args, **kwargs):   # se lo llama metodo init Dunder - estos son atributos del metodo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._dni = dni  # clase 7: forma de encapsular atributos
        self.args = args  # clase 7: se convierte en tupla
        self.kwargs = kwargs  # clase 7: se convierte en una lista
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Jose', 'Villalba', 38, 54325433)

print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona("Osvaldo", "Giordanini", 45, 543254345)

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

"""
Continuación Clase 7:
método Innit Dunder con argumentos variables en el constructor
"""
persona3 = Persona('Héctor', 'Cortez', 32, 543215543,  # atributos del constructor
            'Brazil', 200, 'Cipolletti', 'Río Negro',  # tupla con datos del domicilio
            telefono=35414041000, hobby='estudiar a diario')  # lista con datos extras
persona3.mostrar_detalle()
persona4 = Persona('Marcela', 'Pavón', 31, 4532543,  # atributos del constructor
            'Juan XXIII', 3500, 'Córdoba Capital', 'Córdoba',  # tupla con datos del domicilio
            telefono=1223456, hobby='jugar LoL')  # lista con datos extras
persona4.mostrar_detalle()

"""
En python no existe el encapsulamiento como tal, en su defecto
en los atributos de clase se utiliza un guion bajo delante del atributo
para dar a entender que dicho atributo está encapsulado.

Aun declarando un atributo _myAttribute y dando a entender que es privado
con el uso de _ delande, esto no impide que se pueda seguir accediendo
al atributo por fuera de su definición en la clase.

Existe una segunda manera de encapsular un atributo de clase
y es con doble guión bajo al principio (__) y esto impide que se pueda acceder
al atributo, tanto para leer su contenido como para modificarlo.
Ejemplo: __atributoEncapsulado != _atributoLevementeEncapsulado

Esta regla aplica no solo a atributos, sino que también a métodos

Cuando un atributo comienza con doble guión bajo, Python cambia su nombre internamente 
para incluir el nombre de la clase como prefijo. 
Esto hace que el atributo sea más difícil de acceder desde fuera de la clase. 
Esto se conoce como name mangling.
"""
# lo siguiente es posible debido a que no restringe el acceso, pero no es correcto
print(persona1._dni)

