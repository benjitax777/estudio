# ==========================================
# DICCIONARIOS BASE (NO MODIFICAR ESTRUCTURA)
# ==========================================

# productos_bici = { codigo: [componente, marca, compatibilidad_velocidades] }







productos_bici = {
    'KMC9S': ['Cadena', 'KMC', '9 velocidades'],
    'SH410': ['Cambio Trasero', 'Shimano Alivio', '21 velocidades'],
    'SRM11': ['Piñón Cassette', 'Sram NX', '11 velocidades'],
    'SUN10': ['Piñón Cassette', 'Sunrace', '10 velocidades'],
    'SH310': ['Desviador Delantero', 'Shimano Tourney', '21 velocidades'],
    'KMC11': ['Cadena', 'KMC', '11 velocidades']
}

# inventario_bici = { codigo: [precio_pesos, unidades_stock] }
inventario_bici = {
    'KMC9S': [18990, 15],
    'SH410': [24990, 6],
    'SRM11': [62990, 0],   # ¡Ojo, stock 0!
    'SUN10': [34990, 8],
    'SH310': [12990, 20],
    'KMC11': [29990, 4],
    'ERROR9': [15000, 2]   # Código que no existe en el primer diccionario
}

def pedir_opcion():
    while True:
        menu()
        try:
            opcion=int(input("Ingrese una opcion  (1-4): "))
            if 1 <= opcion <=4:
                return opcion
            else:
                print("Error: Eliga una opcion correcta")
        except ValueError:
            print("Error: Debe ingresar un numero entero obligatorio. "  )

def menu():
    print("*** MENU PRINCIPAL**** ")
    print("1.-Stock marca \n 2.- Rango precio \n 3.- Actualizar precio\n 4.- Salir")
def stock_marca(marca, dicc_productos, dicc_inventario):
    stock_total=0
  
    for bici in dicc_productos:
        if dicc_productos[bici][1].lower() ==marca.lower():
            stock_total+=dicc_inventario[bici][1]
    print(f"El total de stock es: {stock_total}")

def busqueda_precio(p_min, p_max, dicc_productos, dicc_inventario):
    lista_precio=[]
    for p in dicc_productos:
        precio=dicc_inventario[p][0]
        marca=dicc_productos[p][1]
        stock=dicc_inventario[p][1]
        if precio >= p_min and precio <= p_max and stock > 0:
            texto=f"{marca}--{p}"
            lista_precio.append(texto)
    if len(lista_precio) > 0:
        lista_precio.sort()
        print(f"La lista de bicis en el rango de precio es : {lista_precio}")
    else:
        print("No hay en ese rango de precios")

def actualizar_precio(producto, precio_nuevo, dicc_inventario):
    if producto in dicc_inventario:
        dicc_inventario[producto][0]=precio_nuevo
        return True
    else:

        return False



def validacion_marca(marca):
    if not marca.strip():
        return False
    else:
        return True
    



while True:
    
    Opcion=pedir_opcion()
    if Opcion== 4:
        print("Gracias por ocupar el programa ")
        break
    elif Opcion== 1:
        ingreso_marca=input("Ingrese la marca: ")
        if validacion_marca(ingreso_marca):

         stock_marca(ingreso_marca,productos_bici,inventario_bici)
        else:
            print("Error: Debe de tener texto")
    elif Opcion== 2:
        try:
            minimo=int(input("Ingrese el precio minimo: "))
            maximo=int(input("Ingrese el precio maximo: "))

        except ValueError:
            print("Ingrese un valor correcto por favor.")
            continue
        busqueda_precio(minimo, maximo,productos_bici,inventario_bici)
    elif Opcion == 3:
        while True:
            producto_nuevo=input("Ingrese el producto nuevo: ")
            try:
                precio_nuevo=int(input("Ingrese el precio nuevo: "))
            except ValueError:
                print("Ingrese un valor correcto ")
                continue
            valor_total=actualizar_precio(producto_nuevo,precio_nuevo,inventario_bici)
            if valor_total == True:
                print("Se actualizo el precio correctamente")
            else:
                print("El producto no existe ")
            repuesta=input("Desea ingresar otro precio? (s/n)")
            if repuesta != "si":
                break
    




    
