"""
Ejercicio 4: Calculadora de impuestos
Crear una funcion para calcular el total de un pago incluyendo un impuesto
aplicado (IVA) formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
Proporcione el pago sin impuesto: 1000
Proporcione el monto del impuesto: 21%
Pago con impuesto: xxxxx
"""

#Creamos la funcion que calcula el total del pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

#Ejecutamos la funcion
pago_sin_impuesto = float(input("Digite el pago sin impuestos: "))
impuesto = float(input("Digite el monto del impuesto a aplicar: "))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f"El pago con impuesto es: {pago_con_impuesto}")