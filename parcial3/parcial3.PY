"""
nombre=input("Ingrese su nombre:").upper().strip()
sigla=input("ingrese su carrera ")
if not nombre:
    print("Por favor escriba bien su nombre")
elif len(sigla) !=7:
    print("error debe tener 7 siglas su carrera")
else:
    print(f"hola {nombre} la sigla de su carrera son: {sigla[-4:]} ")
    """
"""
try:
    # 1. Solicitamos los datos y los convertimos a entero
    puntaje = int(input("Ingrese la suma total de los puntajes: "))
    preguntas = int(input("Ingrese la cantidad de preguntas: "))
    
    # Intentamos hacer el cálculo matemático
    promedio = puntaje / preguntas

except ValueError:
    # Captura si el usuario ingresa letras o decimales con punto en vez de enteros
    print("Error: Debes ingresar estrictamente un número entero válido.")

except ZeroDivisionError:
    # Captura si el usuario ingresa 0 en la cantidad de preguntas
    print("Error: No se puede dividir por cero. La cantidad de preguntas debe ser mayor a 0.")

else:
    # Este bloque solo se ejecuta si NO hubo ninguna excepción en el try
    print(f"El puntaje promedio por pregunta es: {promedio:.2f}")
    """



#menu
"""
while True:
    print("--- MENÚ PRINCIPAL ---\n1. Ejecutar diagnóstico\n2. Ver pauta de evaluación\n3. Salir")
    try:
        opcion=int(input("Ingrese una opcion "))
    except ValueError:
        print("Error: debes ingresar un numero entero. Las letras no son validas.\n")
        continue  
    if opcion == 3:
        print("adios gracias por usar el programa ")
        break
    elif opcion==1:
        print("abriendo prueba  de codigo...")
    elif opcion==2:
        print("Abriendo rubrica de evaluacion...")
    else:
        print("opcion invalida, intente nuevamente")
        """



