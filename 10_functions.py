# Funciones

def my_function():
    print('Esto es una función')
    
my_function() # Llamamos al print contenido en la función

def sum_two_values(first_value, second_value):
    print(first_value + second_value)
    
sum_two_values(5, 7) # Pasamos 5 a first_value y 7 a second_value
sum_two_values(54754, 71231)

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum 

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f'{name} {surname}')
    
print_name(surname = 'Tecca', name = 'Gian')

def print_name_with_default (name, surname, alias = '"Sin alias"'): # metemos un valor por defecto por si no se le asigna valor a alias
    print(f'{name} {surname} {alias}')
    
print_name_with_default('Gian', 'Tecca', 'TK')
print_name_with_default('Gian', 'Tecca')

def print_texts(*text): # Con * acepta infinitos parámetros
    print(text)
    
print_texts('Hola', 'Python', 'GianTecca')
print_texts('Hola')

def print_texts(*texts):
    for text in texts:
        print(text)
        
print_texts('Hola', 'Python', 'GianTecca')

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
        
print_upper_texts('Hola', 'Python', 'GianTecca')