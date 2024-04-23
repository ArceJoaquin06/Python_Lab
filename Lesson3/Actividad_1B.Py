users = [{"Nombre": 'Joaquín', "Edad": 17}, {"Nombre": 'Insua', "Edad": 63}, {"Nombre": 'Messi', "Edad": 36}]

#Opción A:

for user in users:
    x = user.keys()
    y = user.values()
    print(x, y)

#Opción B:

for user in users:
    for name, age in user.items():
        print(f'{name}: {age}')