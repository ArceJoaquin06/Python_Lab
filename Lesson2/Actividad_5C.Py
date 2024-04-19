frutas_a = ["ciruela", "frutilla", "uva", "sandía", "naranja"]
frutas_b = ["manzana", "banana", "melón", "ananá", "durazno"]

fruta = input("Escriba una fruta cualquiera: ").lower()

if fruta in frutas_a:
    print("Ups, tu fruta ya pertenece a la lista A")
elif fruta in frutas_b:
    print("Ups, tu fruta ya pertenece a la lista B")
elif fruta not in frutas_a or fruta not in frutas_b:
    print("Vaya, tu fruta no se encontraba en ninguna de las listas")