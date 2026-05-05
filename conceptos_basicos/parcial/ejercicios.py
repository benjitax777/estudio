"""
nombre=input("Ingrese su nombre ")
if not nombre:
    print("Ingrese un nombre valido")

else:
    edad=int(input("Ingrese su edad "))

    if edad < 18:
        print("Acceso restringido por edad")
    else:
        suscripcion=input("Tiene una suscripcion activa? (si/no) ")
        if suscripcion == "si":
            print("Acceso completo concedido")
        elif edad >= 60:
            print("acceso por beneificio por edad")
        else:
            print("Acceso limitado: requiere suscripcion")
"""
"""
edad= int(input("ingrese su edad "))
if edad <18:
    print("Solicitud rechazada: edad invalida")
else:
    ingreso=int(input("Ingrese su ingreso mensual "))
    if ingreso <= 0:
        print("solicitud rechazada: ingreso invalido")
    else:
        deudas= int(input("Ingrese la cantidad de deudas que posee "))
        if ingreso >= 500000 and deudas == 0:
            print("Credito aprobado (perfil excelente)")
            monto= ingreso * 5
            print(f"Monto estimado: ${monto}")
        elif ingreso >= 300000 and deudas <=2:
            print("Credito aprobado con condiciones")
            monto= ingreso * 5
            print(f"Monto estimado: ${monto}")
        else:
            print("credito rechazado")
"""

nombre=input("ingrese su nombre ")
if not nombre or not nombre.replace(" ","").isalpha():
    print("Error: nombre no valido")
else:
    edad= int(input("Ingrese su edad "))
    monto= float(input("ingesa el monto de tu compra: "))
    if monto <= 0:
        print("Error: monto invalido")
    else:
        if edad >= 60:
            print("tienes un 20%, de descuento")
            descuento= monto * 0.20
            monto_final= monto - descuento
            print(f"Monto final: ${monto_final}")
        elif monto >= 100000:
            print("descuento 15%")
            descuento= monto * 0.15
            monto_final= monto - descuento
            print(f"Monto final: ${monto_final}")
        elif edad < 18:
            print("descuento 10%")
            descuento= monto * 0.10
            monto_final= monto - descuento
            print(f"Monto final: ${monto_final}")
        else:
            print(f"no hay descuento tienes que pagar: {monto}")
                     
nombre = input("Ingrese su nombre ")
patente = input("Ingrese su patente ")

if len(patente) != 6:
    print("Ingrese una patente correcta por favor")
else:
    vehiculo = input("Ingrese su tipo de vehiculo ").lower()
    horas = int(input("Ingrese las horas en la que estuvo estacionado "))

    if vehiculo == "auto":
        costo = 1500 * horas
        if horas > 8:
            costo = costo - (costo * 0.20)
        print(f"{nombre}, la patente {patente} debe pagar: ${costo}")

    elif vehiculo == "moto":
        costo = 800 * horas
        if horas > 8:
            costo = costo - (costo * 0.20)
        print(f"{nombre}, la patente {patente} debe pagar: ${costo}")

    elif vehiculo == "camion":
        costo = 3000 * horas
        if horas > 8:
            costo = costo - (costo * 0.20)
        print(f"{nombre}, la patente {patente} debe pagar: ${costo}")

    else:
        print("Tipo de vehiculo no reconocido")

    






