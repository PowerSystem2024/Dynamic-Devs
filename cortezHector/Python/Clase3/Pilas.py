# Pilas o Stacks (simulación con listas)
# este tipo de estructura es de tipo LIFO (Last In - First Out)
myStack = [1, 2, 3]
print(myStack)
myStack.append(4)
myStack.append(5)
print(myStack)
removedElement = myStack.pop()
print()
print(f"Elemento removido: {removedElement}")
print(f"Elementos restantes: {myStack}")
print()
removedElement = myStack.pop()
print()
print(f"Elemento removido: {removedElement}")
print(f"Elementos restantes: {myStack}")