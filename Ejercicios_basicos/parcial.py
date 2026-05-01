#Ejercicio1 Entrada/salida y variables
#Pide al usuario su nombre y año de nacimiento. Calcula su edad y muestra
"""
nombre= input("ingrese su nombre ")
año = int(input("ingrese su año de naciemiento "))
edad = 2026- año
print(f"hola {nombre} tienes {edad} años")
"""
#Ejercicio 2 — Tipos de datos

"""
numero1= int(input("ingrese el primer numero "))
numero2= int(input("ingrese el segundo numero " ))

suma= numero1 + numero2
resta = numero1 - numero2
multiplicacion= numero1 * numero2
division= numero1 / numero2
print(suma)
print(resta)
print(multiplicacion)
print(division)
"""
#Ejercicio 3 — Operaciones matemáticas
"""
radio=float(input("ingrese el radio de un circulo "))
pi=3.14159
Area = pi * radio **2
circunferencia= 2 * pi * radio
print(Area)
print(circunferencia)
"""
#Ejercicio 4 — Módulo y división
"""
numero=int(input("ingrese un numero entero "))
resultado= numero % 2
if resultado == 0:
    print("numero es par")
else:
    print("numero es impar")
"""
#Ejercicio 5 — Condicionales simples
"""
nota = int(input("Ingrese una nota 0-100 "))
if nota >= 60:
    print("Aprobado")
elif nota>= 40 and nota <= 59:
    print("Recuperacion")
else:
    print("Reprobado")
    """
#ejercicio 6 — Condicionales anidados
"""
temperatura= int(input("ingrese la temperatura actual "))

if temperatura < 10:
    print("hace frio")
elif temperatura >= 10 and temperatura <= 25:
    print("Temperatura agradable")
else:
    print("hace calor")
    """
    #Ejercicio 7 — Múltiples variables y operacione
"""
precio=int(input("ingrese el precio de el chocolate "))
cantidad=int(input("ingrese la cantidad comprada "))
subtotal= precio * cantidad
Iva= subtotal * 0.19
total=subtotal + Iva
print(total)
"""
"""
#Ejercicio 8 — Todo junto
nombre=input("ingrese su nombre ")
edad=int(input("ingrese su edad "))
sueldo=int(input("ingrese su sueldo mensual "))
if sueldo >1000000:
    print(f"hola {nombre} su renta es alta")
elif sueldo >=500000 and sueldo <= 1000000:
    print(f"hola {nombre} su renta es media")
else:
    print(f"hola {nombre} su renta es baja")

print(f"Hola {nombre}, tienes {edad} años y tu sueldo es ${sueldo}")
"""