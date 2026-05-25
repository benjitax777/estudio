#ejericicio 1
"""
categoria=input("ingrese la categoria:(ropa/tecnologia/alimento) ")
precio_original=float(input(f"ingrese el valor original de {categoria} "))
if categoria == "ropa":
    descuento= precio_original * 0.2
    porcentaje= "20%"
elif categoria == "tecnologia":
    porcentaje= "10%"
    descuento= precio_original * 0.1
elif categoria == "alimento":
    porcentaje= "5%"
    descuento= precio_original * 0.05
else:
    raise ValueError("ingrese una variable correcta")
    

total= precio_original - descuento
print(f"precio originañ: {precio_original}")
print(f"Descuento aplicado:{porcentaje}")
print(f"el total es:{total:.2f}")
"""
"""
cantidad_notas = int(input("ingrese la cantidad de notas "))  # se convierte a int porque range() no acepta float
notas = []  # lista vacía donde se guardarán las notas

for i in range(cantidad_notas):  # itera exactamente "cantidad_notas" veces
    while True:  # repite hasta que el usuario ingrese un valor válido
        try:
            nota = float(input(f"ingrese la nota {i+1}: "))  # convierte el input a float

            if nota < 1.0 or nota > 7.0:  # valida que la nota esté en el rango permitido
                print("Error: La nota debe estar entre 1.0 y 7.0")
                continue  # vuelve al inicio del while si está fuera de rango
            
            notas.append(nota)  # agrega la nota válida a la lista
            break  # sale del while cuando la nota es válida

        except ValueError:  # captura el error si el usuario ingresa algo que no es número
            print("Error: ingrese un numero valido")

# --- cálculos finales ---
promedio = sum(notas) / len(notas)  # suma todas las notas y divide por la cantidad
maxima = max(notas)                 # retorna el valor más alto de la lista
minima = min(notas)                 # retorna el valor más bajo de la lista
aprobados = sum(1 for n in notas if n >= 4.0)  # cuenta cuántas notas son >= 4.0

# --- resultados ---
print(f"Promedio: {promedio:.2f}")
print(f"Nota máxima: {maxima}")
print(f"Nota mínima: {minima}")
print(f"Aprobados: {aprobados}/{cantidad_notas}")
"""



"""
numero=int(input("ingrese un numero "))
for i in range(1,11):
    
    print(f"{numero} x {i}= {numero* i}")
"""

"""
lista_frutas= []
for i in range(5):

    lista=input(f"ingrese una fruta {i+1}: ")
    lista_frutas.append(lista)
print(lista_frutas)
"""



"""
while True:
    try:
        numero=int(input("ingrese un numero"))
        dividido=int(input("ingrese un numero para dividir"))
        resultado= numero / dividido
        print(f"Resultado:{resultado}")
        break

    except ValueError:
        print("ingrese un numero valido")
        
    except ZeroDivisionError:
        print("no se puede dividir por cero")
"""


"""
intentos=0
contraseña ="python123"
while True:
        intentos+=1
        
        repuesta=input("ingrese la contraseña por favor ")
        if repuesta == contraseña:
                print("hola bienvenido!")
                break
        else:
                print(f"llevas los siguientes intentos: {intentos}")
                """





"""
lista= []
for i  in range(5):
    numeros=int(input(f"ingrese el numero {i+1}"))
    lista.append(numeros)


print(sum(lista))
print(max(lista))
print(min(lista))
promedio= sum (lista) / len(lista)
print(f"el promedio es: {promedio}")
"""

       
