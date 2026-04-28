print("Hola bienvenidos a Cesar’s Pizza")
print("este es el menu que tenemos")
#Menu
print("opcion 1. Pizza Napolitana")
print("opcion 2. Pizza De Queso")
print("opcion 3. Pizza De Peperoni")
print("opcion 4. Pizza De Champiñon")
print("opcion 5. Pizza Hawaiana")
opcion= int(input("eliga una opcion de  pizzas "))
cantidad = int(input("Cuantas pizzas se va a llevar "))
if opcion == 1:
    precio= 6000
    print("una pizza Napolitana costaria:", precio)
elif opcion == 2:
    precio = 6000
    print("una pizza Queso costaria : ", precio)
elif opcion ==3:
    precio= 6500
    print("una pizza de Peperoni costaria: ", precio)
elif opcion ==4:
    precio = 7000
    print("Una pizza de Champiñon costaria : ", precio)
elif opcion ==5:
    precio = 7500
    print("Una pizza Hawaiana costaria : ", precio)
else:
    print("elija una opcion correcta")
neto = precio * cantidad

iva = neto * 0.19

total = neto + iva
print(f"Neto:     ${neto}")
print(f"Iva:     ${iva}")
print(f"Total:   ${total}")


