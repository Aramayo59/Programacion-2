# Inventario de productos : Escribe una función que recibe un diccionario donde las claves son los nombres de los productos y los valores son listas de precios históricos de esos productos. La función debe devolver un nuevo diccionario donde las claves son los nombres de los productos y los valores son el precio promedio de cada producto.

def promedio_precios(diccionario_precios):
    promedio_diccionario = {}
    for producto, precios in diccionario_precios.items():
        promedio = sum(precios) / len(precios)
        promedio_diccionario[producto] = promedio
    return promedio_diccionario


inventario_productos = {
    'manzanas': [1.20, 0.30, 5.25],
    'naranjas': [0.90, 0.85, 2.95],
    'platanos': [1.10, 2.05, 3.15]
}
print("Promedio de precios de productos:", promedio_precios(inventario_productos))
