#Palabras por letra inicial : Escribe una función que tome una lista de palabras y devuelva un diccionario donde las claves son las letras iniciales de las palabras y los valores son listas de palabras que comienzan con esa letra.
def palabras_por_inicial(lista_palabras):
    diccionario_iniciales = {}
    for palabra in lista_palabras:
        inicial = palabra[0].lower()
        if inicial in diccionario_iniciales:
            diccionario_iniciales[inicial].append(palabra)
        else:
            diccionario_iniciales[inicial] = [palabra]
    return diccionario_iniciales


palabras = ["hola", "mundo", "python", "Rangu", "Dorado", "Jinsei", "Barbaro"]
print("Palabras por letra inicial:", palabras_por_inicial(palabras))
