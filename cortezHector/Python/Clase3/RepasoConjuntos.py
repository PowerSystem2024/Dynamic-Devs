# Características de los conjuntos (sets):
# - grupo de elementos desordenados
# - no pueden haber valores duplicados
# - puede albergar diferentes tipos de datos

# inicializaciones de un conjunto
setOne = set()  # crea un conjunto mutable vacío
setTwo = frozenset()  # crea un conjunto vacío inmutable
setThree = {"Hello"}  # inicializa con N valores

# agregar elementos al set
setOne.add(42)
setOne.add("World")
print(setOne)

# igualdad en sets
print("setOne igual a setTwo:", setOne == setTwo)  # false

# comprobar si un elemento está en el set
print("El valor 3 está dentro de setOne:", 3 in setOne)  # false

# operaciones en conjuntos/sets
setFour = setOne | setThree  # el símbolo | une ambos sets
print(setFour)

# Intersección entre N conjuntos:
# el operador & se utiliza para encontrar la intersección de N conjuntos,
# es decir, devuelve un nuevo conjunto que contiene solo los
# elementos que son comunes a los conjuntos evaluados.
setOne.add("Hello")
# antes de este punto, setOne y setThree tienen en común el valor "Hello"
setTwo = setOne & setThree
print(setTwo)  # output -> {'Hello'}

# Diferencia simétrica entre N conjuntos:
# al usar el operador ^ se pueden obtener los N elementos
# que esten en los conjuntos evaluados pero que no están en ambos
setA = {"hello", "world", 42, False}
setB = {3.14, True, False, "hello"}
setC = setA ^ setB
print(setC)  # output -> {True, 3.14, 42, 'world'}

# Nota: si se captura el resultado de estas operaciones en un conjunto que
# contiene otros elementos dentro, estos se eliminarán y el conjunto resultante
# tendrá solamente los resultados propios de cada operación de los conjuntos evaluados

print()

# Los métodos issubset() y issuperset() en Python son métodos que pertenecen a la clase set
# y se utilizan para verificar relaciones de inclusión entre conjuntos.
# issubset() -> ¿Está A dentro de B?
# se usa para comprobar si un conjunto (A) es un subconjunto de otro (B).
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 6}
print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)
print("¿Están los elementos de A en B? issubset()", A.issubset(B))  # True, porque todos los elementos de A están en B
print("¿Están los elementos de C en B? issubset()", C.issubset(B))  # False, porque el 6 no está en B

# issuperset() -> ¿Contiene A a B?
# se usa para comprobar si un conjunto (A) es un superconjunto de otro (B)
print("¿Contiene A a B? issuperset()", A.issuperset(B))  # False, porque el conjunto A no contiene al conjunto B
print("¿Contiene B a A? issuperset()", B.issuperset(A))  # True, porque el conjunto B contiene al conjunto A

# Disconexos:
# determinar si dos conjuntos NO comparten elementos en común
X = {1, 2, 3}
Y = {3.14, True, "Bye", 1}
Z = {False, "Hello"}
print(X.isdisjoint(Y))  # False, porque X e Y comparten el elemento 1 en común
print(X.isdisjoint(Z))  # True, porque no comparten elementos en común
