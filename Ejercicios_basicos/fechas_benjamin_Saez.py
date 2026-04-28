from datetime import datetime, date

print("Vamos a ver el orden cronologico de las siguientes fechas")

fecha1_str = input("Ingrese una fecha (DD/MM/AAAA) ")
fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y").date()

fecha2_str = input("Ingrese otra fecha (DD/MM/AAAA)")
fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y").date()

hoy = date.today()

if fecha1 == hoy or fecha2 == hoy:
    fecha_actual = fecha1 if fecha1 == hoy else fecha2
    print(f"esta es la fecha actual {fecha_actual}")
elif fecha1 < fecha2:
    print(f"La fecha : {fecha1} es anterior a : {fecha2}")
elif fecha1 > fecha2:
    print (f"la fecha: {fecha2} es anterior a : {fecha1}")
else:
    print("Las fechas son iguales")