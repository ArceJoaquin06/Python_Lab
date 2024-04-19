nombres = []
nombre = input("Escribe un nombre. Cuando ya no quieras ingresar más, ingresa 'fin': ").lower()
cant_a = 0
cant_e = 0

while nombre != "fin":
    nombres.append(nombre)
    nombre = input("Escribe un nombre. Cuando ya no quieras ingresar más, ingresa 'fin': ").lower()
    if nombre[0] == "a":
        cant_a += 1
    elif nombre[0] == "e":
        cant_e += 1

nombres.sort()

print(f'Lista de nombres ordenada: {nombres}')

print(f'{cant_a} nombres empiezan con la letra "A" y {cant_e} nombres empiezan con la letra "E"')

name = input("Escribe un nombre para buscar en la lista: ").lower()

if name in nombres:
    print(f'{name} pertenece a la lista')
else:
    print(f'{name} no pertenece a la lista')