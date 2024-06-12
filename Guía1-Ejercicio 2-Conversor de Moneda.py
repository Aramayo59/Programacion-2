# Desarrolla un programa en Python que convierta una cantidad de dinero de dólares estadounidenses a euros. El programa debe solicitar al usuario que ingrese la cantidad en dólares y luego mostrar la cantidad equivalente en euros, utilizando un tipo de cambio fijo.

tipo_de_cambio = 0.85  


cant_usd = float(input("Ingresa la cantidad en dólares: "))


cantidad_eur = cant_usd * tipo_de_cambio


print("La cantidad equivalente en euros es:", cantidad_eur)
