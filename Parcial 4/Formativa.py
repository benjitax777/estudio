
def turistas_por_pais(pais):
    print(f"turista de {pais}")

    for datos in turistas.values():
        if datos[1]== pais:

            print(datos[0])
def turistas_por_mes(mes):
    contador_mes=0
    for datos in turistas.values():
        fecha=datos[2]
        partes_fechas=fecha.split("-")
        mes_turista=int(partes_fechas[1])
        if mes_turista == mes:
            contador_mes +=1
    total_turistas= len(turistas)
    porcentaje=(contador_mes / total_turistas)*100
    return round(porcentaje,1)


def eliminar_turista():
    nombre_buscar=input("Ingrese el nombre del turista a eliminar: ").lower()
    encontrado=False
    for llave, datos in list(turistas.items()):
        if datos[0].lower() == nombre_buscar:
            del turistas[llave]
            encontrado=True
            break
    if encontrado:
        print("Turista eliminado con exito")
    else:
        print("Turista no encontrado. No se puede eliminar")    




turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

while True:
    print("***Menu principal***\n1.-Turista por pais\n2.-Turista por mes\n3.-Eliminar turista\n4.-Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==4:
        print("Gracias por ocupar el programa")
        break
    elif opcion == 1:
        nombre_pais=input("Ingrese el nombre del pais:").title()
        turistas_por_pais(nombre_pais)
    elif opcion ==2:
        while True:
            mes_ingresado=int(input("Ingrese el mes [1,12]"))
            if 1 <=mes_ingresado<=12:
                break
            else:
                print("Mes invalido, intente nuevamente")
        porcentaje_final=turistas_por_mes(mes_ingresado)
        print(f"El porcentaje de turista para el mes {mes_ingresado} es: {porcentaje_final}%")        
    elif opcion ==3:
        eliminar_turista()
    else:
        print("Error")