#print("hola ingrese 3 notas por favor")
#try:
    #nota1 =float(input("ingrese la nota 1 "))
    #nota2 =float(input("ingrese la nota 2 "))
    #nota3 =float(input("ingrese la nota 3 "))

    #promedio= round((nota1 + nota2 + nota3)/3,1)
   # if promedio>=4.0:
  #      print("estas aprobado", promedio)
 #   else:
#        print("no aprobaste", promedio)

#except ValueError:
#      print("Ingrese correctamente las notas")



#print("hola bienvenido a este juego")
#print("perro")
#print("Conejo")
#print("Cocodrilo")
"""
print("Tiburon")

puntaje = 0
Repuesta= input("Cuales animales vivnen en el mar? ")
if Repuesta == "Cocodrilo":
    puntaje += 0.5
elif Repuesta == "Tiburon":
    puntaje += 1.0
else:
    print("ingrese una alternativa correcta, no consigio puntos")

print("tu puntaje es: ", puntaje)
"""
puntaje= 0
print("hola bienvenido a este quiz de minecraft")

print("cual es la manera correcta de empezar en un mundo survival?")
print("A) Esconderse")
print("B) explorar y esperar la noche")
print("C) Talar un arbol con los puños")
print("D) empezar a hacerse una casa")

repuesta1=input("ingrese la alternativa " ).upper()
if repuesta1 == "C":
    puntaje += 1.0
    print("correcto!")
else:
    print("incorrecto era la C")