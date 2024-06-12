#Consigna 3: Consigna listas
#Objetivo: Los estudiantes deberán crear una función que reciba una lista de calificaciones, calcule la sumatoria de las notas, el promedio y determine la condición del alumno basado en el promedio. Si el promedio es mayor a 8, el alumno será considerado &quot;PROMOCIONAL&quot; caso contrario “REGULAR”.
#Instrucciones para los Alumnos
#1. Utiliza lista de calificaciones, listaCalificaciones: [9,5, 8, 10, 7, 9, 7.5 , 2, 4.33].
#2. Crea la función evaluar_alumno que recibe el parámetro de la lista de calificaciones.
#3. Los resultados impresos deben ser: sumatoria de notas, promedio de notas y la condición del alumno.

def evaluar_alumno(listaCalificaciones):
    
    suma_notas = sum(listaCalificaciones)
    
   
    prom_notas = suma_notas / len(listaCalificaciones)
    
    
    if prom > 8:
        condicion = "Promocional"
    else:
        condicion = "Regular"
    

    print("La Sumatoria de las notas:,suma_notas ")
    print("Promedio de las notas:,prom_notas ")
    print("Condición del alumno:,condicion")

listaCalificaciones = [9, 5, 8, 10, 7, 9, 7.5, 2, 4.33]

evaluar_alumno(listaCalificaciones)
