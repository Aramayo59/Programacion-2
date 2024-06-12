# Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y devuelva un diccionario con la frecuencia de cada palabra.

def diccionario_frecuencias(lista):
    frecuencia = {}
    for palabra in lista:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia


lista_palabras = ['hola', 'mundo', 'hola', 'python', 'hola']
print("Frecuencia de palabras:", diccionario_frecuencias(lista_palabras))
