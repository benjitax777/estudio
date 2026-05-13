bultos= int(input("ingrese los bultos "))
bultos_livianos= 0
bultos_normales = 0
valor= 0
for i in range(bultos):
try:
peso= int(input("ingrese el peso "))
if peso <= 5:
bultos_livianos += 1
valor += 1000
elif peso <= 10:
bultos_normales += 1
valor += 2000
except ValueError:
print("Valor no valido")
print(f"valor de los bultos livianos:{bultos_livianos * 1000}")
print(f"valor total de los bultos normales: {bultos_normales * 2000}")
print(f"Valor total a pagar: ${valor}")