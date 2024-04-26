# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {'Gian', 'Tecca', 36}
print(type(my_other_set))
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add('MoureDev')
print(my_other_set)

my_other_set.add('MoureDev')
print(my_other_set) # Un set no admite repetidos

print('Tecca' in my_other_set) # Sintaxis para comprobar que un elemento existe dentro de un set
print('Tecce' in my_other_set)

my_other_set.remove('Tecca')
print(my_other_set)

my_other_set.clear() # Vacía todos los elementos del set
print(my_other_set)

del my_other_set
#print(my_other_set) # NameError: name 'my_other_set' is not defined

my_set = {'Gian', 'Tecca', 36}

my_other_set = {'Kotlin', 'Swift', 'Python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union({'JavaScript', 'C#'}))

print(my_new_set.difference(my_set))
print(my_new_set)