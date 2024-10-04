# Lista de tareas (formato: (nombre, descripción, estado))
tareas = [
    ("Comprar groceries", "Comprar leche, pan y frutas", "pendiente"),
    ("Estudiar para el examen", "Revisar capítulos 1 a 5", "en progreso"),
    ("Hacer ejercicio", "Ir al gimnasio por 1 hora", "completada"),
    ("Llamar al médico", "Solicitar una cita para chequeo", "pendiente"),
    ("Enviar el informe", "Enviar el informe a mi jefe por correo", "en progreso")
]
# Funciones para gestionar las tareas
def agregar_tarea():
    nombre = input("Nombre de la tarea: ")
    descripcion = input("Descripción de la tarea: ")
    estado = "pendiente"
    tareas.append((nombre, descripcion, estado))
    print("Tarea agregada exitosamente.\n")

def eliminar_tarea():
    mostrar_tareas()
    indice = int(input("Ingresa el número de la tarea a eliminar: "))
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
        print("Tarea eliminada.\n")
    else:
        print("Número de tarea inválido.\n")

def actualizar_estado():
    mostrar_tareas()
    indice = int(input("Ingresa el número de la tarea a actualizar: "))
    if 0 <= indice < len(tareas):
        nuevo_estado = input("Nuevo estado (pendiente, en progreso, completada): ")
        tarea = tareas[indice]
        tareas[indice] = (tarea[0], tarea[1], nuevo_estado)
        print("Estado actualizado.\n")
    else:
        print("Número de tarea inválido.\n")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(tareas):
            print(f"{i}. {tarea[0]} - {tarea[1]} [{tarea[2]}]")
    print()

def filtrar_tareas():
    filtro = input("Filtrar por estado (pendiente, en progreso, completada): ")
    filtradas = [t for t in tareas if t[2] == filtro]
    if filtradas:
        for i, tarea in enumerate(filtradas):
            print(f"{i}. {tarea[0]} - {tarea[1]} [{tarea[2]}]")
    else:
        print("No hay tareas con ese estado.\n")
    print()

def guardar_tareas():
    with open("tareas.txt", "w") as f:
        for tarea in tareas:
            f.write(f"{tarea[0]};{tarea[1]};{tarea[2]}\n")
    print("Tareas guardadas exitosamente.\n")

def cargar_tareas():
    global tareas
    try:
        with open("tareas.txt", "r") as f:
            tareas = [tuple(line.strip().split(";")) for line in f]
        print("Tareas cargadas exitosamente.\n")
    except FileNotFoundError:
        print("No se encontró un archivo de tareas.\n")

# Menú principal
def menu():
    while True:
        print("Bienvenido al sistema de gestión de tareas")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Actualizar estado")
        print("4. Mostrar tareas")
        print("5. Filtrar tareas")
        print("6. Guardar tareas")
        print("7. Cargar tareas")
        print("0. Salir")
        
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            eliminar_tarea()
        elif opcion == "3":
            actualizar_estado()
        elif opcion == "4":
            mostrar_tareas()
        elif opcion == "5":
            filtrar_tareas()
        elif opcion == "6":
            guardar_tareas()
        elif opcion == "7":
            cargar_tareas()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

# Iniciar el programa
menu()
