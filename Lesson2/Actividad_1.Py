color = input("Escribe un color: ")

def colores(color):

    colorObj = color.lower()

    if colorObj == "azul":
        print('Tú color es azul')
    elif colorObj == "rojo":
        print('Tú color es rojo')
    elif colorObj == "verde":
        print('Tú color es verde')

colores(color)