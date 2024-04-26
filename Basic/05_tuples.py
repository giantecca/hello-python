# Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (36, 1.88, 'Gian', 'Tecca', 'Gian')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])

print(my_tuple.count('Gian'))
print(my_tuple.index('Tecca'))

# La diferencia entre listas y tuplas, es que las tuplas se comportan como constantes.

my_tuple = list(my_tuple) # Convertimos la tupla en una lista
print(type(my_tuple))

my_tuple[4] = 'MoureDev' # Ahora sí podríamos modificar el elemento del índice 4
my_tuple.insert(1, 'Verde') # y agregar un nuevo elemento en el índice 1
print(my_tuple)

my_tuple = tuple(my_tuple) # Convertimos nuevamente la lista a tupla
print(my_tuple)
print(type(my_tuple))
