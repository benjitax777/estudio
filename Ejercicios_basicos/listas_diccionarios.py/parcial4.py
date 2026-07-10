# Lista general de socios (comienza con registros para pruebas)


from typing import clear_overloads


lista_socios = [
    {"rut": "111-1", "nombre": "Tomas Marin", "edad": 25, "plan": "Anual", "pago_pendiente": 0.0},
    {"rut": "222-2", "nombre": "Ana Lopez", "edad": 17, "plan": "Mensual", "pago_pendiente": 35000.0},
    {"rut": "333-3", "nombre": "Luis Silva", "edad": 40, "plan": "Vip", "pago_pendiente": 0.0}
]

# Diccionario de tarifas base fijas (¡No modificar su estructura!)
# Plan: [Precio_Base, Permite_Menores_Edad (True/False)]
tarifas_planes = {
    "Mensual": [35000.0, True],
    "Anual": [29990.0, True],
    "Vip": [55000.0, False]  # El plan VIP exige ser mayor de edad (>= 18)
}

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
        return
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
  

    

    
    










while True:
    opcion=repuesta_de_opcion()
    if opcion == 6:
        print("Gracias por ocupar el progrmaa ")
        break
    if opcion == 1:


    



