# Actualizar diccionario: Escribe una función que tome un diccionario y una lista de tuplas (clave, valor) y actualice el diccionario con esas tuplas.

def actualizar_diccionario(diccionario, lista_tuplas):
    for clave, valor in lista_tuplas:
        diccionario[clave] = valor
    return diccionario


diccionario = {'a': 1, 'b': 2}
tuplas = [('a', 3), ('c', 4)]
print("Diccionario actualizado:", actualizar_diccionario(diccionario, tuplas))
