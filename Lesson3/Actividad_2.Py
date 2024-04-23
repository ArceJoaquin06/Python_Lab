num = int(input("Ingrese un número: "))

def primo(num):
    i = 2
    while i < num :
        if num % i == 0:
            return False
        i += 1
    return True

print(f'¿El número {num} es primo?:', primo(num))
    