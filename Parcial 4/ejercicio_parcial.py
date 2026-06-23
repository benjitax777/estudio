
"""
def saludar(nombre):
    return (f"Hola,{nombre}")
print(saludar("Benjamin"))
"""

"""
#Calculadora
def multiplicar(a,b):
    return a*b
resultado=multiplicar(6,6)
print(resultado)
"""




"""
def es_par(numero):
        return numero% 2 ==0
resultado=es_par(10)
print(resultado)
   """

"""
def obtener_mayor(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>= a and b >=c :
        return b
    else:
        return c
    

    
resultado=obtener_mayor(10,9,8)
print(resultado)
"""

"""
#contar vocales
def contar_vocales(vocal):
    contador=0
    for i in vocal:
        if i in"aeiouAEIOU":
            contador+=1    
    return contador
resultado=input("Ingrese vocales:")
cantidad=contar_vocales(resultado)
print(cantidad)
"""
"""
def filtrar_mayores_a_10(lista_numeros):
   
    nueva_lista=[]
    for i in lista_numeros:
        if i>10:
            nueva_lista.append(i)
    return nueva_lista
mi_lista=[5,10,20,19,2,7]
resultado=filtrar_mayores_a_10(mi_lista)
print(resultado)
"""



def buscar_por_categoria(categoria):
    titulos=[]
    for i in biblioteca:
        
        if biblioteca[i][2]==categoria:
            titulos.append(biblioteca[i][0])
    return titulos
def calcular_disponibilidad():
    libros_disponibles=0
    total_libros=0
    for i in biblioteca:
        if biblioteca[i][3] == "Disponible":
            libros_disponibles+=1
        total_libros+=1
    resultado=libros_disponibles/total_libros * 100  
    return round(resultado,1)
def actualizar_estado():
    titulo=input("Ingrese el titulo")
    encontrado=False

    for i in biblioteca:
        if biblioteca[i][0].lower() == titulo.lower():
            if biblioteca[i][3] == "Disponible":
                biblioteca[i][3]="Prestado"
                encontrado=True
                print("Estado actualizado a Prestado")
                break
            else:
                biblioteca[i][3] = "Disponible"
                
                print("Estado actualizado a Disponible")
                encontrado=True
                break
    if encontrado == False:
        print("No fue encontrado el libro")
          





biblioteca = {
    "L001": ["Cien años de soledad", "Gabriel García Márquez", "Novela", "Disponible"],
    "L002": ["El código Da Vinci", "Dan Brown", "Suspenso", "Prestado"],
    "L003": ["La ciudad y los perros", "Mario Vargas Llosa", "Novela", "Disponible"]
}


while True:
        print("***Menu principal***")
        print("1.- Buscar libros por categoria \n 2.- Calcular disponibilidad \n 3.- Calcular estado de libro\n 4-. Salir")
        opcion=input("Ingrese la opcion: ")
        if opcion =="4":
            print("Gracias por usar el programa")
            break
        elif opcion == "1":
            categoria_usuario=input("Ingrese la categoria que quiera buscar")
            print(buscar_por_categoria(categoria_usuario))
        elif opcion == "2":
            print(f"Disponibilidad: {calcular_disponibilidad()}%")
        elif opcion == "3":
            actualizar_estado()
        else:
            print("Opcion no valida.Por favor , intente de nuevo")
