name = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
año = int(input("Ingrese el año de su ingreso: "))

nacimiento = año - edad

print(f'Buen día {name}, gracias por ingresar. Tu edad es de {edad} y tu fecha de nacimiento es {nacimiento}')

if edad >= 18:
    print("Tu edad corresponde a la de un adulto")
else:
    print("Tu edad corresponde a la de un menor")

if edad % 5 == 0:
    print("Tu edad es un múltiplo de 5")
else:
    print("Tu edad no es múltiplo de 5")

"""
Consigna:
crear un programa que le pida al usuario
nombre, edad y ciudad de residencia, realizar
cálculos basados en la edad, y luego mostrará
la información en pantalla 
(# Pedir al usuario que ingrese su nombre
# Pedir al usuario que ingrese su edad
# Pedir al usuario que ingrese su ciudad de residencia
# Calcular el año de nacimiento
# Saludar al usuario y mostrar la información
# Comprobar si la edad es mayor de 18 años
# Comprobar si la edad es un múltiplo de 5).
"""