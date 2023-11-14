'''
    input -> ingreso de datos mediante terminal o consola
    
    ejemplo:
    nombre = input('cual es tu nombre')
'''

'''
    tarea de ejemplo:
    solicitar el nombre de la persona y responderle con un saludo.
'''
# nombre = input('cual es tu nombre? ')

# print('Un gusto saludarte')
"""
nombre = input('cual es tu nombre? ')

terminal -> cual es tu nombre? 
terminal -> daniel
nombre = daniel
print('Un gusto saludarte', nombre)
"""

# print('cual es tu nombre?')
# nombre = input()
# print('Un gusto saludarte', nombre)

"""
print('cual es tu nombre?')
terminal -> cual es tu nombre?
input()
terminal -> 'solicita algo'
nombre = daniel
print('Un gusto saludarte', nombre)
terminal -> Un gusto saludarte daniel
"""

# print("Cuanto ganas mensualmente con decimales, en soles porfavor?")
# dinero = input()
# print("tipo de dato es dinero", type(dinero))
# aumento = 400
# nuevo_sueldo = aumento + float(dinero)
# print("tu nuevo sueldo ahora es", nuevo_sueldo)

# print("cuanto pesas en kg?")
# kg = input()
# print("pesas {0} kg".format(kg))

# print("cual es tu nombre?")
# nombre = input()
# print("cual se tu apellido")
# apellido = input()
# print("Un gusto saludarte {0} {1}, me llamo daniel".format(nombre, apellido))
# print("cuantos anios tienes?")
# anios = input()
# '''
#     anios = '25'
#     if '25' > 17 -> error porque no se puede comparar un string con un numero
#     int(anios) - > 25 // en entero
#     if 25 > 17 -> es valido
# '''
# if int(anios) > 17:
#     print("eres mayor de edad")
# else:
#     print("eres menor de edad")

# print("cual es tu nombre?")
# nombre = input()
# print("Que tipo de operacion realizara?")
# print("Retirar dinero, presione 1")
# print("Transferir dinero, presione 2")
# opcion = input()
# opcion = int(opcion)
# print("la opcion elegida es ", opcion)

# if opcion == 1:
#     print("usted elegio la operacion retirar")
# elif opcion == 2:
#     print("usted elegio la operacion transferir")
# else:
#     print("error en el sistema opcion no valida")

print("digame su correo para agendarle una reunion")
correo = input()
print(f"le agendaremos una reunion al correo {correo} a las 4pm mediante zoom")