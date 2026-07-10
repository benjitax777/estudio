
"""
inventario={
    "P001": ["Television", "20000",10],
    "P002": ["PC Gamer", "1000000",3],
    "P003": ["PLAY 5", "500000",4]
}
def actualizar_stock(codigo, cantidad_nueva):
    


    if  codigo in inventario:#El in permite verifical la existencia de la llave sin necesidad de for
        inventario[codigo][2]= inventario[codigo][2] + cantidad_nueva
        return True
    else:
        print("Error, no se encontro el codigo")
        return False
            
resultado=actualizar_stock("P001",3)
print(resultado)
"""




"""

inventario={
    "RUT 2248548-7": [4.5,4.5,7.0],
    "RUT 5541541-5": [7.0,5.5,4.4]
}

def calcular_promedios():
    promedios={}
    for rut, notas in inventario.items():
        
        sum(notas)
        len(notas)
        promedio=round(sum(notas)/len(notas),1)
        promedios[rut]=promedio
    return promedios

resultado=calcular_promedios()
print(resultado)
"""






biblioteca = {
    "978-01": ["El Hobbit", "J.R.R. Tolkien", "Fantasía"],
    "978-02": ["It", "Stephen King", "Terror"],
    "978-03": ["Dune", "Frank Herbert", "Ciencia Ficción"],
    "978-04": ["El Resplandor", "Stephen King", "Terror"],
    "978-05": ["Fundación", "Isaac Asimov", "Ciencia Ficción"]
}


def buscar_por_genero(genero_buscado):
    
    encontrado=False
    for titulos in biblioteca:
        if biblioteca[titulos][2].lower() == genero_buscado.lower():
            titulo=biblioteca[titulos][0]#Se agrego titulo una variable para guardar el titulo del dicionnario para asi imprimirlo de manera mas sencilla
            autor=biblioteca[titulos][1]#Se agrego la variable autor para guardar el autor y imprimirlo, ya que se selecciono el lugar donde va el autor 
            print(f"Título: {titulo}, Autor: {autor}")
            encontrado=True
    if not encontrado:

        print("No hay libros disponibles en este genero")
            
   

buscar_por_genero("TERROR")