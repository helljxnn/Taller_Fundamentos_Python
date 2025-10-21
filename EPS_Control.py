# Sistema de Control de Turnos en una EPS 
# Función para registrar los turnos de los pacientes
def register_turns():
    turns = []  # Lista para almacenar los turnos (cada turno será un diccionario)
    services = ["Medicina General", "Exámenes de Laboratorio", "Odontología"]

    print("=== SISTEMA DE CONTROL DE TURNOS EPS ===")
    print("Escriba 'FIN' como nombre para finalizar el registro.\n")

    while True:
        name = input("Ingrese el nombre del paciente: ").strip()

        # Si el usuario escribe "FIN", se detiene el registro
        if name.upper() == "FIN":
            break

        # Validar que el nombre no esté vacío
        if not name:
            print("El nombre no puede estar vacío. Intente nuevamente.\n")
            continue

        print("Seleccione el servicio:")
        for i, service in enumerate(services, start=1):
            print(f"{i}. {service}")

        # Validación de servicio con manejo de errores
        try:
            option = int(input("Ingrese el número del servicio: "))
            if option < 1 or option > len(services):
                print("Opción no válida. Intente nuevamente.\n")
                continue
        except ValueError:
            print("Debe ingresar un número válido.\n")
            continue

        reason = input("Ingrese el motivo de la consulta: ").strip()
        if not reason:
            print("El motivo de consulta no puede estar vacío.\n")
            continue

        # Crear el turno como un diccionario
        turn = {
            "nombre": name,
            "servicio": services[option - 1],
            "motivo": reason
        }

        # Agregar el turno a la lista
        turns.append(turn)
        print(f"Turno registrado correctamente para {name}.\n")

    return turns


# Función para mostrar el resumen final
def show_summary(turns):
    print("\n=== RESUMEN DE TURNOS ===")

    if not turns:
        print("No se registraron turnos.")
        return

    # Número total de turnos
    total_turns = len(turns)
    print(f"Número total de turnos: {total_turns}")

    # Nombre del primer y último paciente
    first_patient = turns[0]["nombre"]
    last_patient = turns[-1]["nombre"]
    print(f"Primer paciente registrado: {first_patient}")
    print(f"Último paciente registrado: {last_patient}")

    # Listado alfabético de nombres
    names = sorted([turn["nombre"] for turn in turns])
    print("\nListado alfabético de pacientes:")
    for name in names:
        print(f"- {name}")

    # Cantidad de turnos por servicio
    service_count = {}
    for turn in turns:
        service = turn["servicio"]
        service_count[service] = service_count.get(service, 0) + 1

    print("\nCantidad de turnos por servicio:")
    for service, count in service_count.items():
        print(f"{service}: {count}")


# Función principal del sistema
def main():
    turns = register_turns()
    show_summary(turns)


# Llamar la función principal
if __name__ == "__main__":
    main()
