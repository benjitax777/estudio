


lista_arriendos = []

# Diccionario de tarifas por tipo de vehículo
# Tipo: [Precio_por_dia, Requiere_licencia_avanzada (True/False)]
tarifas_vehiculos = {
    "Auto": [25000.0, False],
    "Camioneta": [40000.0, False],
    "Moto": [15000.0, True]
}

def obter_clave_auto(auto,dicc_vehiculos):
    for clave in dicc_vehiculos:
        if clave.lower().strip() == auto.lower().strip():
            return clave
    return None
def registar_arriendo(lista, dicc_tarifas):
    nombre=input("Ingrese el nombre del clinete: ")
    tipo_auto=input("Ingrese el tipo de vehiculo: ")
    try:

        dias_arrendar=int(input("Ingrese los dias que quiera arrendar:"))

    except ValueError:
        print("Ingrese un valor entero")
        return
    clave_vehiculo=obter_clave_auto(tipo_auto,tarifas_vehiculos)
    auto= tarifas_vehiculos[clave_vehiculo]