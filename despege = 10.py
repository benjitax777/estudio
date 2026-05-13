"""
for despege in range(10,0,-1):
    
    print(despege)

print("despege")
"""
"""
while True:
    nombre = input("ingrese su nombre ")
    
    if nombre == "terminar":
        break
    elif nombre != "terminar":
        print(f"hola {nombre}")
"""



"""
total=0


for ahorrar in range(7):
    ahorro=float(input("ingrese el lo que ahorro hoy? "))
    
    total+= ahorro
print(f"el total ahorrado fue {total}")
"""
"""
for i in range(1,31):
    if i % 3 == 0:
        print(f"es multiplo de 3 es : {i}")
"""


"""
clave_real="duoc2026"
intentos=3
while True:
    password=input("ingrese la clave por favor ")
    if password == clave_real:

        print("acceso concedido")
        break
    elif password != clave_real:

        intentos-=1
        print(f"te quedan los siguientes intentos: {intentos}")
        if intentos == 0:
            break
print("sistema bloqueado")
"""


"""
#Menu


saldo= 1000
while True:
    eleccion=int(input("1. Consultar saldo \n 2. retirar dinero \n 3. Salir \n ingrese su opcion "))
    if eleccion == 1:
        print(f"su saldo es de {saldo}")
    elif eleccion == 2:
        monto=float(input("ingrese el monto a retirar "))
        if monto > saldo:
            print("fondos insuficientes")
        else:
            saldo-= monto
            print(f"le queda de saldo: {saldo}")
    elif eleccion == 3:
        break
    else:
        print("opcion no valida")
"""