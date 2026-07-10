# Diccionarios base del examen
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1TB', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1TB', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1TB', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1TB', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1TB', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1TB', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990, 10], 
    '2175HD': [327990, 4], 
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21], 
    '123FHD': [290890, 32], 
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2], 
    'UWU131HD': [349990, 1], 
    'FS1230HD': [249990, 0]
}
def menu():
    print("***MENU PRINCIPAL***")
    print("1.-Stock marca\n 2.- Busqueda por precio \n 3.-Actualizar precio \n 4.-Salir")
def stock_marca(marca, dicc_productos, dicc_stock):
    suma_stock=0
    for modelo in dicc_productos:
        
        if dicc_productos[modelo][0].lower()==marca.lower():

            suma_stock+= dicc_stock[modelo][1]
    print(f"El stock es: {suma_stock}")
def busqueda_precio(p_min, p_max, dicc_productos, dicc_stock):
    lista_resultados=[]
    for modelo in dicc_productos:
        precio = dicc_stock[modelo][0]
        stock_actual = dicc_stock[modelo][1]
        marca = dicc_productos[modelo][0]
        if precio>= p_min and precio <= p_max and stock_actual > 0:
            text=f"{marca}--{modelo}"
            lista_resultados.append(text)
    if len(lista_resultados) > 0:
        lista_resultados.sort()
        print(f"Los notebooks entre los precios consultas son {lista_resultados}")
    else:
        print("No hay notebooks en ese rango de precios")
def actualizar_precio(modelo, precio_nuevo, dicc_stock):
    if modelo in dicc_stock:
        dicc_stock[modelo][0]= precio_nuevo
        return True
    else:
        return False
    


while True:
    menu()
    opcion=input("Ingrese una opcion: ")
    if opcion== "4":
        print("Gracias por ocupar el programa.")
        break
    elif opcion== "1":
        marca_ingresada=input("Ingrese marca a consultar: ")
        stock_marca(marca_ingresada, productos, stock)
    elif opcion == "2":
        try:
            minimo=int(input("Ingres un precio minimo: "))
            maximo=int(input("Ingres un precio maximo: "))
        except ValueError:
            print("Debe ingresar valores enteros!!")
            continue
        busqueda_precio(minimo, maximo,productos, stock)
    elif opcion == "3":
        while True:
            modelo_act= input("Ingrese el modelo a actualizar: ")
            try:
                precio_act=int(input("ingrese el precio nuevo: "))
            except ValueError:
                print("Debe ingresar un valor entero para el precio!! ")
                continue
            valor=actualizar_precio(modelo_act, precio_act, stock)
            if valor == True:
                print("Precio actualizado")
            else:
                print("El modelo no existe!!")
            respuesta=input("Desea actualizar otro precio (s/n) ").lower()
            if respuesta != "si":
                break
    else: 
        print("Opcion no valida.")


        

