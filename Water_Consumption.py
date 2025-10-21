# Sistema de Seguimiento de Consumo de Agua en el Hogar
# Función para registrar el consumo diario
def register_consumption():
    consumptions = []  # Lista para guardar los litros diarios

    print("=== SISTEMA DE SEGUIMIENTO DE CONSUMO DE AGUA ===")
    print("Ingrese el consumo diario en litros. Escriba -1 para finalizar.\n")

    day = 1
    while True:
        try:
            value = float(input(f"Ingrese el consumo del día {day}: "))
        except ValueError:
            print("Debe ingresar un número válido.\n")
            continue

        # Finalizar registro
        if value == -1:
            break

        # Validar que sea positivo
        if value <= 0:
            print("El valor debe ser mayor que cero.\n")
            continue

        # Agregar consumo a la lista
        consumptions.append(value)
        day += 1

    return consumptions


# Función para mostrar el informe estadístico
def show_report(consumptions):
    print("\n=== INFORME DE CONSUMO DE AGUA ===")

    if not consumptions:
        print("No se registraron consumos.")
        return

    total_days = len(consumptions)
    total_consumption = sum(consumptions)
    average = total_consumption / total_days
    max_value = max(consumptions)
    min_value = min(consumptions)
    max_day = consumptions.index(max_value) + 1
    min_day = consumptions.index(min_value) + 1
    sorted_list = sorted(consumptions)

    print(f"Total de días registrados: {total_days}")
    print(f"Promedio de consumo: {average:.2f} litros")
    print(f"Día con mayor consumo: Día {max_day} ({max_value} litros)")
    print(f"Día con menor consumo: Día {min_day} ({min_value} litros)")

    print("\nListado completo en orden ascendente:")
    for i, value in enumerate(sorted_list, start=1):
        print(f"{i}. {value} litros")


# Función principal del sistema
def main():
    consumptions = register_consumption()
    show_report(consumptions)


# Ejecutar el sistema
if __name__ == "__main__":
    main()
