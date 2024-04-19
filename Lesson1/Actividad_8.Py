num = int(input("Ingrese un número: "))
res = ""
res1 = ""

if num > 0:
    res = "positivo"
elif num == 0:
    res = "cero"
else:
    res = "negativo"

if num % 2 == 0:
    res1 = "par"
else:
    res1 = "impar"

print(f'El número que usted ingreso es {res} & {res1}')

"""
Consigna:
crearemos un programa que verifica si
un número ingresado por el usuario es positivo,
negativo o cero, y también si es un número par o impar.
"""