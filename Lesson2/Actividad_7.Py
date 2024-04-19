cad = input("Escriba cualquier palabra: ").lower()
sum = 0

for i in cad:
    if i == "a":
        sum += 1

print(f'En {cad} se repiten {sum} veces la letra "a"')