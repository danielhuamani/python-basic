'''
    Tarea sobre cadena de texto (string), para realizar la tarea usar la funcion "print".
    Usar como referencia estos links:
    https://blog.soyhenry.com/metodos-no-tan-vistos-en-python/
    https://programacionfacil.org/blog/los-metodos-de-string-upper-lower-capitalize-y-title-de-python/
'''

'''
    Tarea de ejemplo:
    Eliminar los espacios de la cadena de texto:
    ejemplo:
        '   hola mundo '
    resultado:
        'hola mundo'
'''

variable_spaces = '   hola mundo  '

print(variable_spaces.strip())



'''
    convertir la cadena de texto en  capital letter.
    ejemplo:
        bienvenido a programar
    resultado esperado:
        Bienvenido a programar
'''

variable_to_capitalletter = "bienvenido a programar"

# print -> resultado
print('capital')
'''
    convertir la cadena de texto en todo mayuscula.
    ejemplo:
        primera clase
    resultado esperado:
        PRIMERA CLASE
'''

variable_lower_to_upper = "primera clase"


# print -> resultado
print('upper')
'''
    convertir la cadena de texto en todo miniscula.
    ejemplo:
        APRENDIENDO PYTHON
    resultado esperado:
        aprendiendo python
'''

variable_upper_to_lower = "APRENDIENDO PYTHON"

print('lower')

'''
    convertir la cadena de texto en tipo titulo.
    ejemplo:
        conociendo el lenguaje de programacion python
    resultado esperado:
        Conociendo El Lenguaje De Programacion Python
'''

variable_to_title = "conociendo el lenguaje de programacion python"

print('title')