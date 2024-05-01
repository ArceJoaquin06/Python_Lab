def agregar_tarea(tareas, tarea, fecha_limite, prioridad, completada = False):
    nueva_tarea = {"Tarea": tarea, "Fecha límite": fecha_limite, "Prioridad": prioridad, "Completada": completada}
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"\nTarea {i}:")
            for clave, valor in tarea.items():
                print(f"{clave}: {valor}")

def marcar_completada(tareas):
    i = input("Ingrese el índice de la tarea completada: ")
    if 1 >= 0 and i < len(tareas):
        tareas[i - 1]["Completada"] = True
        print("¡La tarea ha sido completada exitosamente!")
    else:
        print("El indice de la tarea no se encuentra almacenado.")

if __name__ == "__main__":
    lista_tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = input("Ingrese la fecha límite (formato: dd/mm/yyyy): ")
            prioridad_nueva = input("Ingrese la prioridad: ")
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva)

        elif opcion == "2":
            mostrar_tareas(lista_tareas)

        elif opcion == "3":
            marcar_completada(lista_tareas)

        elif opcion == "4":
            break

        else:
            print("Opción no válida. Intente nuevamente.")