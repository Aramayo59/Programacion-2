# Contar palabras en frases: Escribe una función que reciba una lista de frases y devuelva un diccionario donde las claves son las palabras y los valores son las frecuencias de esas palabras en todas las frases.

def contar_palabras(frases):
    contador = {}
    for frase in frases:
        palabras = frase.split()
        for palabra in palabras:
            if palabra in contador:
                contador[palabra] += 1
            else:
                contador[palabra] = 1
    return contador


frases = ["hola mundo", "hola python", "Lobo Dorado"]
print("Frecuencia de palabras en frases:", contar_palabras(frases))
