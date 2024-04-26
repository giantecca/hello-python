# Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    'Nombre':'Gian',
    'Apellido':'Tecca',
    'Edad':36,
    1:'Python'
}

my_dict = {
    'Nombre':'Gian',
    'Apellido':'Tecca',
    'Edad':36,
    'Lenguajes':{'Python', 'Swift', 'Kotlin'}, #Diccionario con un Set dentro
    1: 1.88
}   # Clave:Valor

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict['Nombre'])

my_dict['Nombre'] = 'Gregory'
print(my_dict['Nombre'])

my_dict['Calle'] = 'El Mango'
print(my_dict)

del my_dict[1]
print(my_dict)

print('Tecca' in my_dict)
print('Apellido' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
