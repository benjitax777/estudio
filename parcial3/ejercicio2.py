


cantidad_productos=0
suma_precio=0
total=0
while True:

    print("Menu principal:\n 1.-Agregar producto \n 2.- Ver total de la venta\n 3.-Aplicar descuento \n 4.-Salir")
    try:
        opcion=int(input("Ingrese su opcion:"))
    except ValueError:
        print("Eliga una opcion correcta por favor")
        continue
    if opcion==4:
        print("gracias por ocupar el programa")
        break
    if opcion==1:
        if cantidad_productos >=5:
            print("no se puede agregar mas productos")
        else:
             nombre_producto=input("ingrese el nombre del producto:")
             cantidad_productos+=1
             try:
                precio=float(input(f"ingrese el valor de {nombre_producto}: "))
                suma_precio+=precio
             except ValueError:
                 print("ingrese un precio valido.")
                 continue
    elif opcion ==2:
        total= suma_precio
        if total == 0:
            print("no hay productos registrados")
        else:
            print(f"Total de la venta: ${total}")
    elif opcion==3:
        if cantidad_productos ==0:
            print("no hay productos registrados")
        else:


            try:
                descuento=int(input("ingrese el descuento:"))
                porcentaje=descuento
            except ValueError:
                print("ingrese un valor correcto")
            except ZeroDivisionError:
                print("ingrese un numero superior a 0")
            if porcentaje >=1 and porcentaje <=100:

                descuento=descuento/100
                descuento_aplicado=total*descuento
                total_descuento=total-descuento_aplicado
                print(f"Total con descuento del {porcentaje}%:{total_descuento}")   
            else:
                print("elija una opcion de porcentaje entre 1 al 100")
                continue
    else:
        print("elija una opcion correcta")
        continue
        
       