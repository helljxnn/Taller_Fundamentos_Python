patients = []

def genetate_patient_turn():
    if not patients:
        return 1
    else:
        return patients[-1]['turn'] + 1

def menu():
    while True:
        print("""
            === Serivios de EPS ===
                   
              1.Medicina General
              2.Exámenes de Laboratorio
              3.Odontología
              """)
        option = int(input("Seleccione el servicio que desea: "))
        if option == 1:
            print("Ha seleccionado Medicina General.")
        elif option == 2:
            print("Ha seleccionado Exámenes de Laboratorio.")
        elif option == 3:
            print("Ha seleccionado Odontología.")   
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
            break

def show_patient_info(patient):
    print(f"Turno N°: {patient['turn']}")
    print(f"Nombre del paciente: {patient['name'].title()}")
    print(f"Motivo de consulta: {patient['reason_consult']}")
    print("-" * 30)


def register_patient():
    name = input("Ingresa el nombre del paciente: ").strip().lower()
    #Manejo de errores para evitar campos vacios
    if not name:
        print("El nombre del paciente debe ser ingresado!")
        return
    elif name == "fin":
        print("Saliendo del programa...")
        return
    reason_consult = input("Ingrese el motivo de su consulta: ").strip()
    #Manejo de errores para evitar campos vacios
    if not reason_consult:
        print("Debe ingresar el motivo de su consulta!")
        return
    menu()
    turn = genetate_patient_turn()
    patient = {
        'turn': turn,
        'name': name,
        'reason_consult': reason_consult
    }
    patients.append(patient)
    print(f"Paciente registrado con éxito. Su turno es el N°: {turn}")

