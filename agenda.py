# Programa: Agenda de Contactos Telefónicos

def mostrar_menu():
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Agregar o actualizar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar un contacto")
    print("4. Eliminar un contacto")
    print("5. Salir")

def main():
    # Diccionario para almacenar los contactos (clave: nombre, valor: teléfono)
    contactos = {}

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            # OPERACIÓN 1: Agregar o actualizar contacto
            nombre = input("Ingresa el nombre del contacto: ").strip().capitalize()
            telefono = input("Ingresa el número telefónico: ").strip()
            
            if nombre and telefono:
                contactos[nombre] = telefono
                print(f" Contacto '{nombre}' guardado correctamente.")
            else:
                print(" El nombre y el teléfono no pueden estar vacíos.")

        elif opcion == "2":
            # OPERACIÓN 2: Mostrar información almacenada en pantalla (Recorrer)
            if contactos:
                print("\n LISTA DE CONTACTOS:")
                for nombre, telefono in contactos.items():
                    print(f" • {nombre}: {telefono}")
            else:
                print(" La agenda está vacía.")

        elif opcion == "3":
            # OPERACIÓN ADICIONAL A: Buscar elementos
            nombre = input("Ingresa el nombre a buscar: ").strip().capitalize()
            if nombre in contactos:
                print(f" Contacto encontrado -> {nombre}: {contactos[nombre]}")
            else:
                print(f" El contacto '{nombre}' no existe en la agenda.")

        elif opcion == "4":
            # OPERACIÓN ADICIONAL B: Eliminar elementos
            nombre = input("Ingresa el nombre del contacto a eliminar: ").strip().capitalize()
            if nombre in contactos:
                del contactos[nombre]
                print(f" Contacto '{nombre}' eliminado con éxito.")
            else:
                print(f" El contacto '{nombre}' no fue encontrado.")

        elif opcion == "5":
            print(" ¡Gracias por usar la agenda! Hasta luego.")
            break
        else:
            print(" Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()