# Agrupar por longitud: Escribe una función que reciba una lista de palabras y devuelva un diccionario donde las claves son las longitudes de las palabras y los valores son listas de palabras con esa longitud.

def agrupar_por_longitud(lista_palabras):
    agrupado = {}
    for palabra in lista_palabras:
        longitud = len(palabra)
        if longitud in agrupado:
            agrupado[longitud].append(palabra)
        else:
            agrupado[longitud] = [palabra]
    return agrupado


palabras = ["hola", "mundo", "syrtis", "es", "verde"]
print("Palabras agrupadas por longitud:", agrupar_por_longitud(palabras))
