'''
    Ejercicios de Input.
    Puedes leer documentacion de:
    cast(conversion de datos):
        - https://www.freecodecamp.org/espanol/news/como-convertir-strings-en-enteros-en-python/
        - https://www.programacionfacil.org/cursos/python_avanzado/python_avanzado_3_tipos_de_datos_y_conversiones.html
        - https://www.youtube.com/watch?v=3GcB6I7uDhA
        - https://www.youtube.com/shorts/oiAIU8bocOU
    formateo de string: 
        - https://www.freecodecamp.org/espanol/news/formato-de-cadenas-en-python-ejemplos-de-formato-s-sprint-en-python/
        - https://www.freecodecamp.org/espanol/news/tutorial-de-f-strings-en-python-formato-de-cadenas-en-python-explicado-con-ejemplos/
    input (ingreso de datos mediante la terminal):
        - https://www.programarya.com/Cursos/Python/entrada-y-lectura-de-datos
        - https://www.mclibre.org/consultar/python/lecciones/python-entrada-teclado.html
        - https://www.youtube.com/shorts/R1NqCNfEhbE
    Para probar tu codigo puedes ejecutar el programa con 'python3 tareas/input.py'
'''


'''
    Tarea 1: Desarrolla un programa que solicite al usuario que ingrese un número en forma de cadena, 
    luego conviértelo a entero (int) y flotante (float) e imprime ambas conversiones.
'''
# escribir codigo aquí 
#string = input('Escriba un número: ')
#int = int(string)
#float = float(string)
#print('Reultado:', string, 'string', int, 'int', float, 'float')


'''
    Tarea 2: Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
            Después debe mostrar por pantalla el sueldo que le corresponde.
    recordar sueldo total es: nro horas trabajadas * coste por hora
'''



# escribir codigo aquí
#horastrabajadas = input('¿cuántas horas trabajas? : ')
#horastrabajadas = int(horastrabajadas)
#costeporhora = input('¿precio por hora? : ')
#costeporhora = float(costeporhora)
#print('Sueldo Total: ', horastrabajadas * costeporhora)


'''
    Tarea 3: Crea un programa que ingrese por teclado dos valores, de como resultado la suma de estos dos valores.

'''

# escribir codigo aquí
#numero1 = input('Ingrese el primer número: ')
#numero1 = int(numero1)
#numero2 = input('ingrese el segundo número: ')
#numero2 = int(numero2)
#print('La suma de los dos números es: ', numero1+numero2)


'''
    Tarea 4: Crea un programa que calcule el área de un rectángulo. 
    El usuario debe ingresar la longitud y el ancho del rectángulo.

'''
# escribir codigo aquí
#longitud = input('Ingrese la Longitud: ')
#longitud = int(longitud)
#ancho = input('Ingrese el ancho: ')
#ancho = int(ancho)
#print('El área del rectángulo es: ', longitud*ancho)
'''
    Tarea 5: Crea un programa que convierta dolares a soles.
    Tasa de conversion es 3.80, solicite un numero y conviertalo a soles.
    formula -> 100 dolares en soles =  100 * 3.80

'''
# escribir codigo aquí
dolar = input('solicite la cantidad de dólares: ')
dolar = int(dolar)
tipodecambio = input('Tipo de cambio: 3.80')
soles = float(3.80)
print('Conversión a soles: ', dolar*soles,)
