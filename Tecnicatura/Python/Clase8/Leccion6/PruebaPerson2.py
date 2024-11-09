from Persona2 import Persona2
print('Creacion de objetos'.center(50,'-'))
if __name__ == '__main__':
    persona5 = Persona2('Lionel', 'Messi',35)
    persona5.mostrar_detalles()

    print(__name__)

print('Eliminacion de Objetos'.center(30, '-'))

del persona5 # NO es muy visto por que ya lo hace automaticamente