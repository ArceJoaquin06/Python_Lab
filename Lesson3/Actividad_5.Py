def sum():
    x = lambda a, b: a + b
    return x(int(input("Escribe un número: ")), int(input("Escribe otro número: ")))

print(sum())

def exponen():
    y = lambda a, b: a ** b
    return y(int(input("Escribe un número: ")), int(input("Escribe otro número: ")))

print(exponen())