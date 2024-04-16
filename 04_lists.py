# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [36 , 1.88, 'Gian', 'Tecca']

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count('Tecca'))

age, height, name, surname = my_other_list # Esto es complicarse
print(name)

print(my_list + my_other_list)

my_other_list.append('MoureDev') # Inserta un valor al final
print(my_other_list)

my_other_list.insert(1, 'Verde') # Inserta un valor en una posición que le indico y mueve hacia adelante el que estaba
print(my_other_list)

my_other_list[1] = 'Rojo' # Cambio el valor del índice 1
print(my_other_list)

my_other_list.remove('Rojo') # Elimina el valor que le indico
print(my_other_list)

print(my_list)
my_list.pop() # Elimina el último elemento
print(my_list)

print(my_list.pop(2)) # Retorna el elemento eliminado
print(my_list)

del my_list[2] # No retorna el elemento eliminado
print(my_list)

my_new_list = my_list.copy() # Copiamos la lista y la metemos en otra

my_list.clear() # Elimina o limpia la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # Le damos la vuelta a los elementos de la lista
print(my_new_list)

my_new_list.sort() # Ordena los elementos de menor a mayor
print(my_new_list)

print(my_new_list[1:3])

my_list = 'Hola Python'
print(my_list)
print(type(my_list))

