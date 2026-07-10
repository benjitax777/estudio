



vehiculos = {
    'AB-CD-12': ['Toyota', 'Yaris', 2018, 'Rojo'],
    'XY-ZW-99': ['Hyundai', 'Accent', 2020, 'Blanco'],
    'KJ-LH-44': ['Suzuki', 'Swift', 2015, 'Azul'],
    'PO-IU-11': ['Toyota', 'Hilux', 2022, 'Gris'],
    'GG-WP-77': ['Hyundai', 'Tucson', 2019, 'Negro'],
    'ZZ-AA-00': ['Suzuki', 'Baleno', 2021, 'Rojo']
}

inventario_precio = {
    'AB-CD-12': [8500000, 3],   # [Precio, Stock]
    'XY-ZW-99': [10200000, 2],
    'KJ-LH-44': [5800000, 0],   # ¡Ojo, stock 0!
    'PO-IU-11': [18500000, 1],
    'GG-WP-77': [14000000, 5],
    'ZZ-AA-00': [9200000, 4],
    'FANTASMA': [3000000, 1]    # Patente que no existe en vehículos
}
def menu():
    print("*** MENU PRINCIPAL***")
    print("1.-Stock\n2.-buscar por precio\n 3.-Actualizar precio\n 4.- Salir ")
def stock_marca(marca, dicc_vehiculos, dicc_inventario):
    stocK_disponible=0
    for auto in dicc_vehiculos:
        if dicc_vehiculos[auto][0].lower() == marca.lower():
            stocK_disponible+=dicc_inventario[auto][1]
    print(f"El total de stock es: {stocK_disponible}")
def busqueda_precio(p_min, p_max, dicc_vehiculos, dicc_inventario):
    lista_precio=[]
    for p in dicc_vehiculos:
        precio=dicc_inventario[p][0]
        marca=dicc_vehiculos[p][0]
        stock=dicc_inventario[p][1]
        if precio >= p_min and precio <= p_max and stock > 0:
            text=f"{marca}--{p}"
            lista_precio.append(text)
    if len(lista_precio) > 0:
        lista_precio.sort()
        print(f"Los autos con el precio consultado son: {lista_precio}")
    else:
        print("No hay autos en ese rango de precio")

def actualizar_precio(patente, precio_nuevo, dicc_inventario):
    if patente in dicc_inventario:
        dicc_inventario[patente][0]= precio_nuevo
        return True
    else:
        return False


while True:
    menu()
    opcion=input("Ingrese una opción: ")
    if opcion == "4":
        print("Gracias por ocupar el programa.")
        break
    elif opcion == "1":
        ingreso_marca=input("Ingrese la marca: ")
        stock_marca(ingreso_marca,vehiculos, inventario_precio)
    elif opcion == "2":
        try:
            minimo=int(input("Ingrese el precio minimo: "))
            maximo=int(input("Ingrese el precio maximo: "))
        except ValueError:
            print("Error: ingrese un numero por favor")
            continue
        busqueda_precio(minimo, maximo, vehiculos, inventario_precio)
    elif opcion== "3":
        while True:
            patente_nueva=input("ingrese la patente nueva: ")
            try:
                nuevo_precio=int(input("Ingrese el nuevo precio: "))

            except ValueError:
                print("Error: ingrese un numero")
            valor=actualizar_precio(patente_nueva,nuevo_precio, inventario_precio)
            if valor == True:
                print("Precio actualizado")
            else:
                print("La patente no existe")
            repuesta=input("Desea ingresar otro precio? (s/n): ")
            if repuesta != "si":
                break
    else:
        print("Error: Eliga una opcion correcta")
