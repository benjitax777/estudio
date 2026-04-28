#nombre : benjamin saez
print("ingrese los datos del nombre del cliente")


cliente= input("ingrese su nombre ")
producto1= int(input("ingrese el precio del primer producto "))
Cantidad_producto1= int(input("ingrese la cantidad del primer producto "))
producto2= int(input("Ingrese el precio  del segundo producto "))
Cantidad_producto2 = int(input("ingrese el la cantidad del segundo producto "))
producto3= int(input("Ingrese el precio del tercer producto "))
Cantidad_producto3= int(input("Ingrese la cantidad del producto 3"))
Descuento=int(input("Ingrese la decuento: "))


#calculos
totalBruto =(producto1 * Cantidad_producto1) + (producto2 * Cantidad_producto2) + (producto3*Cantidad_producto3)
total_descuento=totalBruto - (totalBruto * Descuento / 100)
iva = total_descuento * 0.19
total= total_descuento +iva

#Resultados


print()

print(f"Cliente:    {cliente}  ")
print(f"Total bruto:   ${totalBruto}")
print(f"Total descuento ${total_descuento:.0f}")
print(f"Iva:             ${iva:.0f}")
print(f"Total:            ${total:.0f}")