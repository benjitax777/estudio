print("Calculadora geometrica ")
base= 0
altura=0
radio= 0
perimetro= 0
lados= 0 
area= 0
while True:
    eleccion=int(input("**********Menu**********\n1 Calcular Perimetro \n 2. Calcular area \n 3. Salir\n Elija una opcion: "))
    if eleccion == 1:
        while True:
            print("Calcular Perimetro")
            eleccion_2=int(input("1. Para circulo\n 2.Para rectangulo\n 3.Para Cuadrado\n 4.Volver menu principal\n Elija una opcion:  "))
            if eleccion_2 == 4:
                break
            elif eleccion_2== 1:
                radio=float(input("ingrese el radio "))
                perimetro= radio *2 * 3.14
                print(f"el total del perimetro es : {perimetro}")
            elif eleccion_2== 2:
                base=float(input("ingrese la base "))
                altura=float(input("ingrese la altura "))
                perimetro= 2*(base + altura)
                print(f"el  total del perimetro es: {perimetro}")
            elif eleccion_2== 3:
                lados= float(input("ingrese el lado "))
                perimetro= lados * 4
                print(f"el  total del perimetro es: {perimetro}")
            
            else:
                print("Ingrese una opcion correcta ")
    elif eleccion==2:
        while True:
            print("Calcular Area")
            eleccion_2=int(input("1. Para circulo\n 2.Para rectangulo\n 3.Para Cuadrado\n 4.Volver menu principal\n Elija una opcion:  "))
            if eleccion_2 == 4:
                break
            elif eleccion_2== 1:
                radio=float(input("ingrese el radio "))
                area= 3.14 * radio **2
                print(f"el total del area es: {area}")
            elif eleccion_2 ==2:
                base=float(input("ingrese la base "))
                altura=float(input("ingrese la altura "))
                area= base * altura
                print(f"el total del area es: {area}")
            elif eleccion_2 ==3:
                lados=float(input("ingrese el lado "))
                area= lados **2
                print(f"el total del area es: {area}")
            else:
                print("ingrese una opcion correcta")
                
    elif eleccion== 3:
        print("gracias por usar la calculadora. !Hasta luego!")
        break
        


    
