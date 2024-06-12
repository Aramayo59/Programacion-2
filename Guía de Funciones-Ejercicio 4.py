# Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
# Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido
# hacer login incremente este valor, validar con otra función la cantidad de intentos posibles en3 oportunidades.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se
# intente hacer login, recuerden solamente tenemos tres oportunidades para intentarlo.

def login(usuario, contraseña, intentos):
    if usuario == "usuario1" and contraseña == "asdasd":
        return True
    else:
        intentos += 1
        return False, intentos


intentos = 0
while intentos < 3:
    usuario = input("Ingresa el nombre de usuario: ")
    contraseña = input("Ingresa la contraseña: ")
    valido, intentos = login(usuario, contraseña, intentos)
    if valido:
        print("Login exitoso")
        break
    else:
        print(f"Login fallido. Intentos restantes: {3 - intentos}")

if intentos == 3:
    print("Has excedido el número de intentos permitidos.")
