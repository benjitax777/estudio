def repuesta_de_opcion():
    print("***MENU PRINCIPAL ***")
    print("1.-Registrar Socio\n 2.-Buscar socio\n 3.- Abonar a Deuda\n 4.-Expulsar Socio\n 5.- Mostar reporte de socios\n 6.- Salir ")
    
    try:

        eleccion=int(input("Elija una opcion: "))
        if  1 <= eleccion  <= 6:
            return eleccion
        else:
            print("Error: elija una opcion valida.")
    except ValueError:
        print("Error: Solo se permiten numeros")

def validacion_rut(rut):
    if rut.strip() != "":
        return True
    return False
def validacion_edad(edad):
    if edad > 0:
        return True
    return False
def validacion_plan(plan, dicci_plan):
    for i in dicci_plan:
        if i.lower().strip() == plan.lower().strip():
            return i
    return None

def registar_socio(lista):
    rut= input("Ingrese el rut: ")
    if not validacion_rut(rut):
        print("Erro: El rut no puede estar vacio ni contenter espacios")
        return
    nombre=input("Ingrese el nombre: ")
    if not validacion_rut(nombre):
        print("Error; El nombre no  puede estar vacio")
        return
    try:
        edad = int(input("Ingrese su edad: "))
        if not validacion_edad(edad):
            print("Error: la edad debe ser un numero entero mayor que cero")
    except ValueError:
        print("Error: debe de ser un numero entero")
        return
    plan=input("Ingrese su plan: ")
    clave_plan=validacion_plan(plan,tarifas_planes)
    if clave_plan is None:
        print("Error: No existe ese plan ")
        return 0
    precio_base, permite_menores = tarifas_planes[clave_plan]
    if not permite_menores and edad < 18:
        print(f"Error: El plan {clave_plan} exige ser mayor de edad")
        return
    nuevo_socio={
        "rut": rut.strip(),
        "nombre": nombre.strip(),
        "edad": edad,
        "plan": clave_plan,
        "pago_pendiente": precio_base

    }
    lista.append(nuevo_socio)
    print(f"Socio registrado con exito! pago pendiente: ${precio_base:,.0f}".replace(",","."))
def buscar_socio(lista, rut_buscar):
    for i in range(len(lista)):
        if lista[i]["rut"].strip() == rut_buscar.strip():
            return i
    return -1



    

    
    










while True:
    opcion=repuesta_de_opcion()
    if opcion == 6:
        print("Gracias por ocupar el progrmaa ")
        break
    if opcion == 1:
        registar_socio(lista_socios)
    elif opcion == 2:
        rut_buscar=str(input("Ingrese el rut: "))
        valor=buscar_socio(lista_socios, rut_buscar)
        if valor !=-1:
             print(f"el socicio se encontro el posicion: {valor}")
             
        else:
           
            print("Error: no existe ese socio")



