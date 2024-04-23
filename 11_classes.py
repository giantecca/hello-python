# Clases

class MyEmptyPerson: # Las Clases las escribimos con CamelCase
    pass # Es una instrucción que no realiza ninguna operación

# print(MyEmptyPerson)

# Ejemplo 1
class Person:
    def __init__(self, name, surname): # Constructor de Clase
        self.name = name
        self.surname = surname
    
my_person = Person('Gian', 'Tecca')
print(f"{my_person.name} {my_person.surname}")

# Ejemplo 2
class Person2:
    def __init__(self, name, surname, alias = 'Sin alias'):
        self.full_name = f"{name} {surname} ({alias})"
    
    def walk(self):
        print(f'{self.full_name} está caminando')
    
my_person = Person2('Giancarlo', 'Tecca')
print(my_person.full_name)
my_person.walk()

my_other_person = Person2('Giancarlo', 'Tecca', 'TK')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'Héctor de León (el loco de los perros)'
print(my_other_person.full_name)
