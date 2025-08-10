import random
import string

# Bucle while para validar el mínimo de caracteres
while True:
    try:
        longitud = int(input("Ingrese el número de caracteres para la contraseña (mínimo 5): "))
        if longitud < 5:
            print("⚠ La contraseña debe tener al menos 5 caracteres.")
        else:
            break
    except ValueError:
        print("⚠ Ingrese un número válido.")

# Caracteres disponibles
mayusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = string.punctuation

# Unir todos los caracteres
todos = mayusculas + minusculas + numeros + simbolos

# Generar contraseña usando for e if
contrasena_lista = []
for i in range(longitud):
    if i % 4 == 0:
        contrasena_lista.append(random.choice(mayusculas))
    elif i % 4 == 1:
        contrasena_lista.append(random.choice(minusculas))
    elif i % 4 == 2:
        contrasena_lista.append(random.choice(numeros))
    else:
        contrasena_lista.append(random.choice(simbolos))

# Mezclar los caracteres para evitar patrón
random.shuffle(contrasena_lista)

# Convertir lista en string
contrasena = "".join(contrasena_lista)

print(f"🔐 Su contraseña generada es: {contrasena}")
