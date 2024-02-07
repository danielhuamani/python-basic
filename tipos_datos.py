'''
    Tipos de datos:
    - **Enteros (int):** números enteros, como 1, 2, 3, -4, etc.
    - **Flotantes (float):** números con decimales, como 3.14, -0.5, etc.
    - **Cadenas (str):** una secuencia de caracteres, como “hola”, “mundo”, “Python”, etc.
    - **Booleanos (bool):** un valor que es verdadero (True) o falso (False).
    - **Listas (list):** una colección ordenada de elementos, que pueden ser de 
        cualquier tipo de datos, como [1, “hola”, True].
    - **Tuplas (tuple):** una colección ordenada e inmutable de elementos, que 
        pueden ser de cualquier tipo de datos, como (1, “hola”, True).
    - **Conjuntos (set):** una colección no ordenada de elementos únicos, como {1, 2, 3}.
    - **Diccionarios (dict):** una colección no ordenada de pares clave-valor,
        como {”nombre”: “Juan”, “edad”: 30}.
        
'''

# variables
#  nombres validos de variable
variable = 5
variable = "hola"
geral = 5
casa = 5
casa_grande = 5 # 
_casa = 5
variable10 = 5
variaBle = 5
x,y,z = 2,4,5
PI = 3.14
SEGUNDOS_EN_MINUTO = 60
# Nombers invalidos de varible
# 3variable = 5
# variable-casa=5
# var iable = "csaas"


# IMPRIMIR VALORES
# print('valor de x: ', x)
# print('valor de x:', x, 'valor de y:',  y,  'valor de z:', z)

# PALABRAS RESERVADAS
'''
    print -> imprimir mensaje o contenido
    if -> sirve como condicional
    is = identificar tipo instancia
    type -> sirve para saber que tipo de dato es
'''
#  TIPOS DE DATOS NUMERICO-> ENTERO Y FLOTANTES
'''
    Entero -> 1 , 0 , -1 (int)
'''

variable1 = 1
variable2 = 2

'''Float (float)'''
x = 2.4
y = 3.7

print('tipo de dato de variable1:', type(variable1))
print('tipo de dato de x:', type(x))


'''TIPO DE DATO STRING (CADENA DE TEXTO) -> str'''

x = 'buenos dias "geral" '
y = "buenos dias"
z = "Hola geral 'buenos dias' "

multiples_lineas = '''
    Hola Geral,
    te escribo esta carta
'''
salto_lineal = 'hola geral \nbuenos dias'
edad_geral = '25'
edad_nueva_geral = 25
nac = 1998
# FORMAS DE ANIDAR CADENAS DE TEXTO(STRING) CON MENSAJES
mensaje_geral = 'Hola geral tienes ' + edad_geral + ' años'
mensaje_format = 'Hola geral tienes {0} años y nacio en {1}'.format(edad_geral, nac)
print("mensaje_format", mensaje_format)
minuscula = 'geral'
# format(0, 1,2,3,4,5)


'''
    tipo de dato boolean -> bool
'''

x = True
y = False
string = 'dsdsds'
nostring = ' '
z = -1
o = 0
print("valores booleano", bool(o), bool(z))
'''
    tipo de dato listado -> list
'''

listado = [2, "222", True, False, 10]
listad_1 = list([2, 3, 4, 5, 10])

print(type(listado))
print(listado[4])

'''
    tipo de dato diccionario -> dict
'''
dict_prueba = {
    'nombre': 'geral',
    'edad': '25'
}
print("dict_prueba: ", dict_prueba, type(dict_prueba), dict_prueba.get('edad'))

if __name__ == "__main__":
   ...