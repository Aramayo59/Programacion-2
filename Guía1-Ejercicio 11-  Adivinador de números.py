
# Crea un juego que le pida al usuario que piense un número entre 1 y 100. Luego, el programa debe intentar adivinar ese número utilizando la estrategia de búsqueda binaria. En cada intento, el programa debe preguntar al usuario si el número a adivinar es mayor, menor o igual al número propuesto por el programa. El juego debe terminar cuando el programa adivine el número correcto.


print("Piensa en un número entre 1 y 100. Yo intentaré adivinarlo.")
bajo = 1
alto = 100
adivinado = False

while not adivinado:
    intento = (bajo + alto) // 2
    print(f"¿Es {intento} tu número?")
    respuesta = input("Ingresa 'A' si es alto, 'B' si es bajo, o 'C' si es correcto: ").upper()
    if respuesta == 'A':
        alto = intento - 1
    elif respuesta == 'B':
        bajo = intento + 1
    elif respuesta == 'C':
        adivinado = True
        print(f"¡Genial! He adivinado tu número: {intento}")
    else:
        print("Respuesta no válida.")
