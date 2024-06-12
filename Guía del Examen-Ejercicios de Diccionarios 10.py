#Valores únicos: Escribe una función que reciba un diccionario y devuelva una lista de valores únicos en el diccionario.

def valores_unicos(diccionario):
    return list(set(diccionario.values()))


diccionario = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
print("Valores únicos en el diccionario:", valores_unicos(diccionario))
