#Consigna 2: Consigna diccionario
#Objetivo: Los estudiantes deberán crear una función que modifique el diccionario dicEstudiantes eliminando la clave &quot;sexo&quot; y añadiendo una nueva clave &quot;edad&quot; con valores generados aleatoriamente entre 18 y 32 años (inclusive) para cada estudiante.
#Instrucciones para los Alumnos
#1. Copia el código del diccionario dicEstudiantes proporcionado.
#2. Implementa la función según la consigna.
#3. Desarrolla la lógica para cumplir con el enunciado.
#4. Imprime el diccionario resultante para verificar que las modificaciones se han realizado correctamente (eliminación de &quot;sexo&quot; y adición de &quot;edad&quot;).

import random

diccEstudiantes = {
    'estudiante_1': {'nombre_apellido': 'Juan Pérez', 'dni': 12345678, 'sexo': 'Masculino', 'carrera': 'Turismo'},
    'estudiante_2': {'nombre_apellido': 'María López', 'dni': 23456789, 'sexo': 'Femenino', 'carrera': 'Software'},
    'estudiante_3': {'nombre_apellido': 'Carlos García', 'dni': 34567890, 'sexo': 'Masculino', 'carrera': 'Trekking'},
    'estudiante_4': {'nombre_apellido': 'Ana Fernández', 'dni': 45678901, 'sexo': 'Femenino', 'carrera': 'Espacios'},
    'estudiante_5': {'nombre_apellido': 'Luis Martínez', 'dni': 56789012, 'sexo': 'Masculino', 'carrera': 'Enfermería'},
    'estudiante_6': {'nombre_apellido': 'Sofía Gómez', 'dni': 67890123, 'sexo': 'Femenino', 'carrera': 'Turismo'},
    'estudiante_7': {'nombre_apellido': 'Pedro Rodríguez', 'dni': 78901234, 'sexo': 'Masculino', 'carrera': 'Software'},
    'estudiante_8': {'nombre_apellido': 'Elena Sánchez', 'dni': 89012345, 'sexo': 'Femenino', 'carrera': 'Trekking'},
    'estudiante_9': {'nombre_apellido': 'Miguel Torres', 'dni': 90123456, 'sexo': 'Masculino', 'carrera': 'Espacios'},
    'estudiante_10': {'nombre_apellido': 'Laura Ruiz', 'dni': 91234567, 'sexo': 'Femenino', 'carrera': 'Enfermería'}
}

def modificar_diccionario(dic_estudiantes):
    for key, value in dic_estudiantes.items():
       
        if 'sexo' in value:
            del value['sexo']
        
        value['edad'] = random.randint(18, 32)
    return dic_estudiantes


diccEstudiantes_modificado = modificar_diccionario(diccEstudiantes)


print(diccEstudiantes_modificado)