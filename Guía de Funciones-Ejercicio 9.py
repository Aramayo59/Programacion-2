# Ordenar lista de cadenas: Escribe una función que tome una lista de cadenas y devuelva una lista ordenada alfabéticamente de esas cadenas, ignorando mayúsculas y minúsculas.
def ordenar_cadenas(lista):
    return sorted(lista, key=lambda s: s.lower())


cadenas = input("Ingresa una lista de cadenas separadas por comas: ").split(",")
cadenas_ordenadas = ordenar_cadenas(cadenas)
print("Lista ordenada alfabéticamente:", cadenas_ordenadas)
