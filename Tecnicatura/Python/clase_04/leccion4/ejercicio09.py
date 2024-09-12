 # Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer una frase donde el usuario ingrese una frase, se le devolverá la misma frase pero sin espacios en blanco.
# Asimismo, se realizará un conteo del número de caracteres que posee la frase (sin contar los espacios en blanco)
# Ejemplo: frase = vivir por siempre en paz | frase final = vivirporsiempreenpaz | N° de caracteres = 21.

frase1 = input('Digite una frase: ')
frase2 = ''

for i in frase1:
    if i != ' ':
        frase2 += i
frase1 = frase2
print(f'\nLa frase sin espacios en blanco es: {frase1}')
print(f'La cantidad de caracteres que posee la frase sin espacios en blanco es: {len(frase1)}')