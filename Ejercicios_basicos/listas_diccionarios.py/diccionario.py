def devuelveMayor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor
milista=[1,2,3,4,5,6,7,8,9,10,5,6,111,2324,15]
print(devuelveMayor(milista))