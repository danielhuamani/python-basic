# if -> ejecuta la condicion siempre y cuando sea True
# elif -> ejecuta la condicion sea True, siempre y cuando el if primero sea False
# else -> ejecuta la condicion siempre y cuando fallen los if or elif


x = 5 > 3

# los cursos del colegion son:
#    - matematica
#    - historia

# if x:
#     print("el valor de es x:", x, " porque fue mayor a 3")
# if (4 > 2 or 3 < 1 and not (3 > 1)):
#     print("esto da tsssrue")
    
# else

# if 5 > 6:
#     print("entro true")
# else:
#     print("entro false")

# if (5 > 3) and (5 > 10) and (2 < 1):
#     print("entro la condicion del if")
# else:
#     print("entro la condicion del else")

# elif

# if (5 > 3) and (5 > 10) and (2 < 1):
#     print("entro la condicion del if")
# elif 5 > 3:
#     print("entro al elif")
# else:
#     print("entro la condicion del else")

numero = input("""
            Ingrese una operacion:
            1. Transferir
            2. Retirar
            3. depositar       
        """)
numero = int(numero)

if numero == 1:
    print("La opcion elegida es transferir")
elif numero == 2:
    print("la opcion elegidra es retirar")
elif numero == 3:
    print("la opcion elegida es depositar")
else:
    print("la operacion no existe")