import random
import string

#definimos los caracteres de la libreria string

letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

#definimos la funcion 

def contrasena_segura(longitud):
    caracteres = letras + numeros+ simbolos
    contrasena =""
    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena

nombre = input("ingrese su nombre: ")

# Bucle while para validar el mínimo de caracteres
while True:
    try:
        #pedimos al usuario determinar la longitud de caracteres de su contraseña y generamos la contraseña 
        longitud = int(input("Ingrese el número de caracteres para la contraseña (mínimo 5 y maximo 16 ): "))
        if longitud < 5 :
            print("La contraseña debe tener al menos 5 caracteres.")
        elif longitud > 16:
            print("la contraseña debe tener un maximo 16 digitos")
        else:
            break
    except ValueError:
        print(" Ingrese un número válido.")

pasword = contrasena_segura(longitud)

print("Hola",nombre, "su contraseña es:" , pasword)






