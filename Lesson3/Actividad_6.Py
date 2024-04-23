nums = [1, 2, 3, 4, 5]

def exponen():
    rest = map(lambda a: a ** 2, nums)
    lista = list(rest)
    return lista

print(exponen())