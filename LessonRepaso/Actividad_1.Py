weigth = float(input("Ingrese su peso en Kg: "))
height = float(input("Ingrese su altura en metros: "))

imc = weigth / (height * height)
size = ""

if imc < 18.5:
    size += "S"
elif imc >= 18.5 and imc < 24.9:
    size += "M"
elif imc > 25 and imc < 29.9:
    size += "L"
else:
    size += "XL"

print(f'Su IMC es de {imc}Kg/m2 y su talla es {size}')