




inventario = {
    "P001": ["Laptop Gamer", "Computación", 1200000, 5],
    "P002": ["Mouse Inalámbrico", "Accesorios", 15000, 20],
    "P003": ["Monitor 24\"", "Computación", 150000, 8],
    "P004": ["Teclado Mecánico", "Accesorios", 45000, 0]
}
def productos_sin_stock():
    lista_stock=[]
    for i in inventario:
        if inventario [i][3]==0:
            lista_stock.append(inventario[i][0])
    return lista_stock
def aplicar_descuento(categoria,porcentaje):
    encontrado=False

    
    for i in inventario:
    
        if inventario[i][1].lower() == categoria.lower():
         
         
         precio_actual=inventario[i][2]
         nuevo_precio = precio_actual * (1 - porcentaje/100)#Aca calcula el precio del producto dado por el porcentaje de descuento
         inventario[i][2]=nuevo_precio#Aqui se guarda el cambio
         encontrado=True
    return encontrado#Devuelve True si se encontro la categoria si no la encontro devuelve false y se evalua en el menu
         
def valor_total_inventario():
    total=0#Se agrega un acumulador
    for i in inventario:
        total+=inventario[i][2]* inventario[i][3]#Se multiplica el valor de cada producto por el stock que existe  y luego se le suma al cumalador 
    return total#Para luego retornar el total de la ecuacion

while True:
    print("***MENU***")
    print("1.-Ver productos sin stock\n2.-Aplicar descuento a una categoria\n3.-Ver valor total del inventario\n 4.Salir")
    opcion=input("Ingrese una opcion: ")
    if opcion == "4":
        print("Gracias por ocupar el programa")
        break
    elif opcion =="1":
        print(productos_sin_stock())
    elif opcion =="2":
        categoria_producto=input("Ingrese la categoria del producto: ").lower()
        descuento=int(input("Ingrese el descuento: "))
        
        exito=aplicar_descuento(categoria_producto, descuento) #Se guarda en una variable para que se evalue porque la funcion es un codigo y no se puede evaluar si es verdadera o false
        if exito == True:#Se evalua en el menu si se encontro la categoria del producto
            print("Descuento aplicado correctamente")#imprime si fue True
        else:
            print(f"Error: CATEGORIA NO ENCONTRADA")#Imprime si fue False
    elif opcion =="3":
        print(valor_total_inventario())