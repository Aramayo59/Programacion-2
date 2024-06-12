# Intercambiar valores: Crea una función que tome un diccionario y dos claves, e intercambie los valores de esas dos claves en el diccionario.

def intercambiar_valores(diccionario, clave1, clave2):
    diccionario[clave1], diccionario[clave2] = diccionario[clave2], diccionario[clave1]
    return diccionario


diccionario = {'a': 1, 'b': 2}
print("Diccionario antes del intercambio:", diccionario)
diccionario = intercambiar_valores(diccionario, 'a', 'b')
print("Diccionario después del intercambio:", diccionario)
