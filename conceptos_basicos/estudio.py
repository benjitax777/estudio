#variables


my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables
print(my_string_variable, str( my_int_variable), my_bool_variable)
print("esta es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_int_to_str_variable))

#Variables en una sola linea. !Cuidado con abusar de esta sintaxis!

name, surname, alias, age = "benjamin", "Saez", "Pipo", 35
print ("Me llamo:",name, surname, ". Mi edad es: ", age, ". Y mi alias es :", alias)

#inputs

#name = input("Cual es tu nombre? ")
#age = input("Cuantos años tienes? ")

#print(name)
#print(age)

# Cambiamos su tipo

name = 35
age = "Benjamin"
print(name)
print(age)

# Forzamos el el tipo
addrees: str = "Mi direccion"
addrees = 33
addrees = 5.1
print(type(addrees))