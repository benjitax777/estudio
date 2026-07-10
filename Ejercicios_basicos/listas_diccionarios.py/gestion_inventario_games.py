lista_juego=[]
def menu():
    print("***MENU***")
    print("1.-Agregar videojuego\n 2.-Buscar videojuego\n 3.-Eliminar Videojuego\n 4.-Actualizar Disponibilidad\n 5.- Mostrar inventario\n 6.-Salir")
def agregar_juego(lista):
    titulo=input("Ingrese el titulo: ")
    if validacion_titulo(titulo) == False:
        print("Error: tiene que tener texto")
        return
    
    stock=int(input("Ingrese el stock: "))
    if validacion_stock(stock) == False:
            print("Error: tiene que ser stock mayor que cero")
            return
        
    precio=int(input("Ingrese el precio: "))
    if validar_precio(precio) == False:
             print("Error: Debe de ser mayor que cero ")
             return
            
    diccionario_videojuego={
                    "titulo": titulo,
                    "stock": stock ,
                    "precio": precio,
                    "disponible": False
                }
    lista.append(diccionario_videojuego)

    

    
def validacion_titulo(titulo):
    if not titulo.strip():
        return False
    else:
        return True
def validacion_stock(stock):
    if stock < 0:
        return False
    else:
        return True
def validar_precio(precio):
    if precio <=0:
        return False
    else:
        return True


def buscar_juego(lista,titulo_buscar):
     for i in range(len(lista)):
          
          if lista[i]["titulo"] == titulo_buscar:

            return i 
     return -1
def actualizar_disponibilidad(lista):
     for juego in lista:
          if juego["stock"] > 0 :
               juego["disponible"]= True
          else:
               juego["disponible"]= False

    










while True:
    menu()
    opcion=input("ingres una opcion: ")
    if opcion== "6":
        print("Gracias por ocupar el programa")
        break
    elif opcion=="1":
         agregar_juego(lista_juego)

    elif opcion=="2":
         titulo_buscar=input("ingrese el titulo: ")
         encontrado=buscar_juego(lista_juego,titulo_buscar)
         if encontrado == -1:
              print(f"El juego {titulo_buscar} no se encuentra en el inventario.")
         else:
              print(f"El juego con el titulo :{titulo_buscar}, fue encontrado en la posiciion {encontrado}")
    elif opcion=="3":
         titulo_eliminar=input("Ingrese el videojuego que quiera eliminar: ")
         encontrado=buscar_juego(lista_juego, titulo_eliminar)
         if encontrado == -1:
              print(f"El juego {titulo_eliminar} no se encuentra en el inventario.")
         else:
              lista_juego.pop(encontrado)
              print(f"El juego '{titulo_eliminar}' fue eliminado con éxito.")
    elif opcion=="4":
         actualizar_disponibilidad(lista_juego)
         print("Disponibilidad de inventario actualizada con éxito.")
    elif opcion =="5":
         for juego in lista_juego:
              print(f"Título: {juego['titulo']} | Stock: {juego['stock']} | Precio: ${juego['precio']} | Disponible: {juego['disponible']}")
    else:
         print("Error: Elija una opcion correcta")   
         
              

        
              
         

         
         


    


