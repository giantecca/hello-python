# Strings

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String \ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

# Formateo
# %s - String
# %d - Integers
# %f - Floating point numbers
print("\n")

name, surname, age = "Gian", "Tecca", 36

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
print("\n")

language = "python"
a, b, c, d, e, f = language

print(a)
print(e)

# División
print("\n")

language_slice = language[1:3]
print(language_slice)

# Reverse
print("\n")

reversed_language = language[::-1]
print(reversed_language)

# Funciones
print("\n")

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))