#Filtrar diccionario: Escribe una función que reciba un diccionario y una lista de claves, y devuelva un nuevo diccionario solo con las claves especificadas.

def filtrar_diccionario(diccionario, claves):
    return {k: diccionario[k] for k in claves if k in diccionario}


diccionario = {'a': 1, 'b': 2, 'c': 3}
claves = ['a', 'c']
print("Diccionario filtrado:", filtrar_diccionario(diccionario, claves))
