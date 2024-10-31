class MiClase:
    # variable de clase, este atributo dara a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia):  # variable de instancia, da diferentes valores
        self.variable_intancia = variable_instancia

print(MiClase.variable_clase)

miClase1 = MiClase('Esta una varibale de instancia')
print(miClase1.variable_intancia)

print(miClase1.variable_clase)
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_intancia)
print(miClase2.variable_clase)


