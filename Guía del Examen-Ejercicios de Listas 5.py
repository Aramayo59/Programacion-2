# Eliminar duplicados: Crea una función que tome una lista y devuelva una nueva listasin elementos duplicados.

def eliminar_duplicados(lista):
    return list(set(lista))


numeros = [1, 2, 3, 4, 5, 1, 2]
print("Lista sin duplicados:", eliminar_duplicados(numeros))
