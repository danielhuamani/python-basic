## OPERADORES ARITMETICOS
# Operador    Nombre	        Ejemplo
# +	        Suma	        x + y = 13
# -	        Resta	        x - y = 7
# *	        Multiplicación	x * y = 30
# /	        División	    x/y = 3.333
# %	        Módulo	        x%y = 1
# **	        Exponente	    x ** y = 1000
# //	        Cociente	    3

## OPERADORES LOGICOS


# Operador	Nombre	Ejemplo
# and	Devuelve True si ambos elementos son True	True and True = True
# or	Devuelve True si al menos un elemento es True	True or False = True
# not	Devuelve el contrario, True si es Falso y viceversa	not True = False

y = True and True and False
print('resultado de y :', y)

z = False and False and True or True
print('resultado de z :', z)

p = (((True and True)) and False) or True
print('resultado de p :', p)

q = not True
print('resultado de q :', q)
u = not (True or False)
print("u", u)
w = (not (True or False) and not ((False or True) or (False and False)))
print('resultado de q :', w)


## Operadores de asignacion

# Operador	Ejemplo	Equivalente
# =	        x=7	    x=7
# +=	    x+=2	x=x+2 = 7
# -=	    x-=2	x=x-2 = 5
# *=	    x*=2	x=x*2 = 14

i = 7
i += 2
print("i", i)

z = 3
z -= 2
print("z", z)

z = 5
z *= 4
print("z", z)