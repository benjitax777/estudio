# ==========================================
# DICCIONARIOS BASE (NO MODIFICAR ESTRUCTURA)
# ==========================================

# productos_hogar = { codigo: [nombre_aparato, marca, categoria] }
productos_hogar = {
    'REF23': ['Refrigerador No Frost', 'Samsung', 'Línea Blanca'],
    'MIC09': ['Microondas Digital', 'LG', 'Cocina'],
    'ASP15': ['Aspiradora Robot', 'Xiaomi', 'Limpieza'],
    'TV55M': ['Smart TV 55 QLED', 'Samsung', 'Entretenimiento'],
    'HOR45': ['Horno Eléctrico', 'Thomas', 'Cocina']
}

# inventario_hogar = { codigo: [precio_pesos, unidades_stock] }
inventario_hogar = {
    'REF23': [649990, 7],
    'MIC09': [119990, 12],
    'ASP15': [249900, 0],   # ¡Ojo, stock 0!
    'TV55M': [499990, 5],
    'HOR45': [89990, 15],
    'FANTASMA': [150000, 2] # Código que no existe en el primer diccionario
}

def pedir_opcion():
    while True:

        print("***MENU PRINCIPAL***")
        print("1.-Buscar y Mostrar Stock\n 2.- Registrar nuevo producto\n3.-Actualizar precio\n 4.- Dar de baja producto\n 5.- Salir")
        try:

            opcion=int(input("Ingrese una  opcion: "))
            if  1 <= opcion  <= 5:
                return opcion
            else:
                print("Ingrese una opcion correcta")
        except ValueError:
            print("Error: Debe de ser numero ")
        except ZeroDivisionError:
            print("Ingrese un valor mayor a 0")
def buscar_producto(codigo, dicc_productos):
    
    for clave in dicc_productos:
        if clave.strip().lower() == codigo.strip().lower():

            return True
    return False
def mostrar_stock_marca(marca,dicc_productos,dicc_inventario):
    stock_total=0
    for i in dicc_productos:
        if dicc_productos[i][1].strip().lower()== marca.strip().lower():
            stock_total+=dicc_inventario[i][1]
    
    print(f"El stock total es : {stock_total}")

def registrar_producto(codigo, nombre, marca, cat, precio, stock, dicc_productos, dicc_inventario):
    if buscar_producto(codigo, dicc_productos):
        print("Error: El código ya está registrado")
        return

    dicc_productos[codigo] = [nombre, marca, cat]
    dicc_inventario[codigo] = [precio, stock]
    print("Producto registrado con éxito!")
    

def modificar_precio(codigo, precio_nuevo, dicc_inventario):
    dicc_inventario[codigo][0] = [precio_nuevo]
    print("Producto modificado")










while True: 
    Opcion=pedir_opcion()    
    if Opcion == 5:
        print("Gracias por ocupar el programa ")
        break
    elif Opcion == 1:
        
        pedir_marca=input("Ingrese una marca: ")
        mostrar_stock_marca(pedir_marca,productos_hogar, inventario_hogar)
    elif Opcion == 2:
        codigo_nuevo=input("Ingrese el codigo nuevo: ").strip()
        if codigo_nuevo == "":
            print("Erro: el codigo no puede estar vacio")
            continue
        nombre_nuevo=input("Ingrese el nombre del producto: ").strip()
        marca_nueva=input("Ingresa la marca: ").strip()
        categoria_nueva= input("Ingresa la categoria ").strip()
        try:
            precio_nuevo = int(input("Ingrese el precio: "))
            stock_nuevo = int(input("Ingrese el stock: "))
        except ValueError:
            print("Error: precio y stock deben ser números")
            continue
        registrar_producto(codigo_nuevo, nombre_nuevo, marca_nueva, categoria_nueva,
                        precio_nuevo, stock_nuevo, productos_hogar, inventario_hogar)
    elif Opcion == 3:
        codigo_precio=input("Ingrese el codigo: ")
        valor=buscar_producto(codigo_precio,productos_hogar)
        if valor == True:
            
            try:

                nuevo_precio=int(input("Ingrese el precio nuevo: "))
                modificar_precio(codigo_precio,nuevo_precio,inventario_hogar)

            except ValueError:
                print("Error debe de ser numero ")
        else:
            print("Error: Codigo no encontrado")





