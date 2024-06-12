#Merge de diccionarios: Crea una función que tome dos diccionarios y devuelva uno nuevo que combine ambos (en caso de conflicto, usa los valores del segundo diccionario).

def merge_diccionarios(dic1, dic2):
    resultado = dic1.copy()
    resultado.update(dic2)
    return resultado


dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
print("Diccionario combinado:", merge_diccionarios(dic1, dic2))
