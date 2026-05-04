nombre= input("ingrese su nombre por favor ")
nota1 = float(input("digame su primera nota "))
nota2 = float(input("digame su segunda nota "))
nota3 = float(input("digame su tercera nota "))
promedio= (nota1 + nota2 + nota3) / 3
print(round(promedio, 1))
if promedio >= 6.0:
    print(f"Felicidades {nombre}, aprobaste con distinción")
    if nota1 < 3.0 or nota2 < 3.0 or nota3 < 3.0:
         print("Ojo: tienes al menos una nota muy baja")

elif promedio >= 4.0:

    print(f"Aprobaste {nombre}, pero puedes mejorar")
    if nota1 < 3.0 or nota2 < 3.0 or nota3 < 3.0:
         print("Ojo: tienes al menos una nota muy baja")
else:
    print(f"Lo sentimos {nombre}, reprobaste")
    if nota1 < 3.0 or nota2 < 3.0 or nota3 < 3.0:
        print("Ojo: tienes al menos una nota muy baja")