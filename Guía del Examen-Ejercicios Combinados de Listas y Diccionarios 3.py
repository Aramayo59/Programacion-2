# Diccionario de listas: Escribe una función que tome un diccionario donde los valores son listas y devuelva una lista que contenga todos los elementos de las listas del diccionario.

def diccionario_a_lista(diccionario):
    lista = []
    for clave in diccionario:
        lista.extend(diccionario[clave])
    return lista


diccionario = {'a': [1, 2], 'b': [3, 4], 'c': [5]}
print("Lista combinada de los valores del diccionario:", diccionario_a_lista(diccionario))
