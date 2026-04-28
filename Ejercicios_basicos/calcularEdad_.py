print("Bienvenido a este programa para ver si usted es mayor de edad")

try:
    edad = int(input("Ingrese su año de nacimiento por favor: "))
    if 1925 < edad <= 2007:
        print("Usted es mayor de edad")
    elif edad > 2007:
        print("Usted es menor de edad")
    else:
        print("Ingrese un año de nacimiento válido")
except ValueError:
    print("Error: debe ingresar solo numeros, sin letras ni simbolos")