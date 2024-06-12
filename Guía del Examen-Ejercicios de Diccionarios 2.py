#Diccionario inverso: Escribe una función que tome un diccionario y devuelva uno nuevo que invierta las claves y los valores.

def diccionario_inverso(diccionario):
    return {v: k for k, v in diccionario.items()}


diccionario = {'a': 1, 'b': 2, 'c': 3}
print("Diccionario inverso:", diccionario_inverso(diccionario))
