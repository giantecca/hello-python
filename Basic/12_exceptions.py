# Excepciones

numberOne, numberTwo = 5, 1

numberTwo = '1'


# try except
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error :D')
except:
    print('Se ha producido un error :(')
    
# try except else
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error :D')
except:
    print('Se ha producido un error :(')
else:
    # Opcional | Se ejecuta si no se produce una excepción
    print('La ejecución continúa correctamente')
    
# try except else finally
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error :D')
except:
    print('Se ha producido un error :(')
else:
    # Opcional | Se ejecuta si no se produce una excepción
    print('La ejecución continúa correctamente')
finally:
    # Opcional | Se ejecuta siempre
    print('La ejecución continúa')
    
# Excepciones por tipo
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error :D')
except TypeError:
    # Se ejecuta sólo si el error es de type
    print('Se ha producido un TypeError :(')
except ValueError:
    # Se ejecuta sólo si el error es de value
    print('Se ha producido un ValueError :(')
    # Dejando sólo except cubrimos cualquier tipo de error
    
# Captura de la información de la excepción
try:
    print(numberOne + numberTwo)
    print('No se ha producido un error :D')
except ValueError as error: # as {variable}
    print(error)
except Exception as my_random_error_name: # as {variable}
    print(my_random_error_name)
