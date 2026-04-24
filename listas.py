### listas ###

my_list = list()
my_other_list ={}

print(len(my_list))

my_list = [18, 15, 8, 39, 18, 22, 1]

print(my_list)
print(len(my_list))

my_other_list = [18, 1.77, "benjamin", "Saez"]
print(type(my_list))
print(type(my_other_list))

print(my_other_list [0])
print(my_other_list [1])
print(my_other_list [-1])
print(my_other_list [-4])
print(my_list.count(18))#El Count se utiliza para contar elementos de la lista
#print(my_other_list [4]) IndexError
#print(my_other_list [-5]) IndexError
age, height, name, surname= my_other_list
print(name)

name, height, age, surname =my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)
#print(my_list - my_other_list)#Error



my_other_list.append("Benjitax")
print(my_other_list)

my_other_list.insert(1, "Verde")
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)

my_other_list.remove("Rojo")
print(my_other_list)

my_list.remove(18)#Remove sirve para eliminar un elemento 
print(my_list)

print(my_list.pop())




my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]#Del elimina por indice
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)
my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])


my_list = "hola Python"
print(my_list)
print(type((my_list)))