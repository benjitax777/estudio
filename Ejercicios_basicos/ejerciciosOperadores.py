"""
print("hola bienvenido a este ejercicio vamos a calcular los siguientes numeros")
print("15 y 4")
a=15
b=4
division=a//b
print(f"la division es lo siguiente: {division}")
resto= a % b
print(f"el resto es {resto} ")
elevado= a ** b
print(f"Elevado el resultado es: {elevado}")
"""
"""
print("En este programa vas a ver comparacion")

x=10
y=20

print(x==y)#Si es igual
print(x!=y)#Si no es igual
print(x>y)#si es mayor
print(x<y)#si es menor
print(x>=y)#si es mayor o igual
print(x<= y)#si es menor o igual
"""
"""
print("Ahora vas a ver Logica")

llueve= True
tengo_paraguas= False
hace_frio = True

print( "debo salir si llueve y no tengo paraguas?",llueve and tengo_paraguas)
print("si llueve y hace frio eso significa que debo quedarme en casa?", llueve or hace_frio)
print("si esta lloviendo y tengo paraguas deberia salir con el paraguas??", llueve and not tengo_paraguas)#True
"""

print("este es un desafio")
precio= 1500
descuento= 15
precio_final=precio - (precio* descuento/100)
print(precio_final)

print(f"el precio final es menor a 1000? {precio_final< 1000}")
print(f"el descuento es mayor o igual a 10? {descuento >= 10}")