

rut=input("ingrese su rut: ")
guiones= 0
formato_invalido=False
for i in rut:
    if i == "-":
        
        guiones+=1
    elif i =="k" or i =="K":
        pass
       
    elif not i.isdigit():
        
        formato_invalido=True
posicion_guion=rut.index("-")      
if guiones==1 and formato_invalido ==False and rut[-2] =="-" and (posicion_guion == 7 or posicion_guion==8) and (rut[-1] =="k" or rut[-1]== "K" or rut[-1].isdigit()):


    print("formato valido")
else:
    print("Formato invalido")
