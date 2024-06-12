# Notas de estudiantes : Escribe una función que recibe un diccionario donde las claves son nombres de estudiantes y los valores son listas de sus calificaciones. La función debe devolver un nuevo diccionario con las mismas claves pero donde los valores son la calificación promedio de cada estudiante.


def promedio_calificaciones(diccionario_notas):
    promedio_diccionario = {}
    for estudiante, calificaciones in diccionario_notas.items():
        promedio = sum(calificaciones) / len(calificaciones)
        promedio_diccionario[estudiante] = promedio
    return promedio_diccionario


notas_estudiantes = {
    'Juan': [8, 9, 5],
    'Maria': [7, 2, 8],
    'Pedro': [5, 5, 8]
}
print("Promedio de calificaciones de estudiantes:", promedio_calificaciones(notas_estudiantes))
