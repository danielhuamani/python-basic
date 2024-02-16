'''
 **Cast en Python
Hacer un cast o 
casting significa convertir un 
tipo de dato a otro. 
Anteriormente hemos visto tipos como los int, string o float. 
Pues bien, es posible convertir de un tipo a otro.
'''

variable_letras = "hola geral"

variable_numero = "100"

# 'a' * 5 = 'aaaaa'
# '2' * 3 = '222'
# 5 * 3 = 15
# "5" * 3 = 15  -> '555' //incorrecto

texto = 'hola' # str
entero = 2 # int
flotante = 2.45 # float

'''
    Conversion de texto a entero.
    cast: int
'''
# variable_texto = 'hola geral' invalido
# entrada -> proceso -> salida
mi_variable = int('25')
print('inicio 25 tipo', type('25'))
print('variable ahora:', mi_variable, ' es tipo: ', type(mi_variable))

'''
    Conversion de decimal(flotante) a entero.
    cast: int
'''

mi_variable2 = int(5.2)
print('tipo del valor 5.2 ', type(5.2))
print('variable2 ahora es: ', mi_variable2, 'su tipo es:', type(mi_variable2))

'''
    Conversion de entero a flotante.
    cast: float
'''

mi_variable3 = float(7)
print('tipo del valor 7 ', type(7))
print('variable3 ahora es: ', mi_variable3, 'su tipo es:', type(mi_variable3))

'''
    Conversion de string(str) a flotante(float).
    cast: float
'''
'''
    "5.6" -> string
    type("5.6") -> string
    float("5.6") -> 5.6
    mi_variable4 -> 5.6
    type(5.6) -> float
    '7.8' -> string (str)
    m = '7.8'
    z = m
    x = float('7.8') 
    x vale -> 7.8
    
    y = 20
    a = y + 5
    y = a
    print(type(25)) -> int
    
    print(y + 2) -> 27
    print(type( y + 3)) -> int
    print( type(a + 2) ) -> int
    
    str -> convierta el parametro a texto
    print(str(y)) -> '25'
    print(float(y)) -> 25.0
    
    x = 2.5
    y = 3.2
    z = x + y
    print(z) -> 5.7
    print(type(z)) -> float
    print(str(z)) -> '5.7'
    print(int(z)) -> 5
    
    -------
    x = 2
    y = 22
    z = x + y
    print(z) -> 24
    print(float(z)) -> 24.0
    print(type(float(z))) -> 
    
'''
mi_variable4 = float('5.6')
print('tipo del valor 5.6 ', type('5.6'))
print('variable4 ahora es: ', mi_variable4, 
      'su tipo es:', type(mi_variable4))


'''
    Conversion de entero(int) a texto(str).
    cast: str
'''

mi_variable5 = str(5)
print('tipo del valor 5 ', type(5))
print('variable5 ahora es: ', mi_variable5, 
      'su tipo es:', type(mi_variable5))
