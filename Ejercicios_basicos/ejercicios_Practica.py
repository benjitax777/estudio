"""
monto=float(input("Ingrese el monto de la cuenta "))
porcentaje=float(input("ingrese la propina que desea dejar "))
propina=monto*(porcentaje/100)
print(f"Propina:{propina}")
total=monto+propina
print(f"el total a pagar es: {total}")
if porcentaje>= 15:
    print("gracias por su propina generosa")
elif porcentaje < 15:
    print("Gracias por su propina normal")
else:
    print("gracias por comprar")
    """
"""
nombre=input("ingrese su nombre ")
contraseña=input("ingrese una contraseña ")
if len(contraseña)< 6:
    print("ingrese una contraseña con mas de 6 caracteres")
elif not contraseña[0].isupper():
    print("Error: La contraseña debe empezar con una mayuscula")
else:
    print(f"Contraseña válida, bienvenido/a {nombre.upper()}")
"""
"""
nombre=input("ingrese su nombre ")
peso=float(input("ingrese su peso (KG) "))
estatura=float(input("ingrese su estatura (metros) "))
imc= peso/(estatura**2)
if imc < 18.5:
    categoria="Bajo peso"
elif 18.5<= imc < 25:
    categoria="normal"
elif 25<= imc < 30:
    categoria="sobrepeso"
else:
    categoria="obesidad"
print(f"{nombre}, tu IMC es {round(imc, 2)} → Categoría: {categoria}")
"""
from ast import compare


nombre=input("ingrese su nombre ")
tipo=input("ingrese su tipo (vip o regular) ").lower()
monto=int(input("ingrese el monto de compra "))
if  tipo =="vip" and monto >= 50000:
    descuento= monto * 0.20
    
elif tipo == "vip" and monto <50000:
    descuento= monto*0.10
    
elif tipo == "regular" and monto >= 100000:
    descuento= monto *0.10
   
else:
    descuento= 0

total=monto - descuento

print(f"Tipo de cliente: {tipo.upper()}")
print(f"Monto original: ${monto}")
print(f"Descuento aplicado: {int(descuento / monto * 100)}%  → ${descuento:.0f}")
print(f"Total a pagar: ${total:.0f}")