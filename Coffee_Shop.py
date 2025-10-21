# Sistema de Gestión de Pedidos en una Cafetería
# Función para mostrar el menú disponible
def show_menu():
    print("\n=== MENÚ DE LA CAFETERÍA ===")
    print("1. Papitas - $3.500")
    print("2. Helado - $1.500")
    print("3. Agua - $2.300")
    print("4. Empanada - $3.400")
    print("0. Finalizar pedido")

# Función para registrar un nuevo pedido
def register_order(orders):
    print("\n=== REGISTRAR NUEVO PEDIDO ===")
    try:
        order_number = int(input("Ingrese el número del pedido: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    # Validar que el número no esté repetido
    if order_number in orders:
        print("Ese número de pedido ya existe.")
        return

    client_name = input("Ingrese el nombre del cliente: ").strip()
    if not client_name:
        print("El nombre del cliente no puede estar vacío.")
        return

    # Menú de productos
    menu = {
        1: ("Papitas", 3500),
        2: ("Helado", 1500),
        3: ("Agua", 2300),
        4: ("Empanada", 3400)
    }

    items = []
    total = 0

    # Registro de productos del pedido
    while True:
        show_menu()
        try:
            option = int(input("Seleccione un producto (0 para finalizar): "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if option == 0:
            break
        elif option not in menu:
            print("Opción no válida.")
            continue

        try:
            quantity = int(input("Ingrese la cantidad: "))
            if quantity <= 0:
                print("La cantidad debe ser mayor que cero.")
                continue
        except ValueError:
            print("Debe ingresar una cantidad válida.")
            continue

        product_name, price = menu[option]
        subtotal = price * quantity
        total += subtotal

        # Guardar producto en la lista del pedido
        items.append({
            "producto": product_name,
            "cantidad": quantity,
            "subtotal": subtotal
        })

    # Validar que el pedido tenga al menos un ítem
    if not items:
        print("El pedido debe tener al menos un producto.")
        return

    # Guardar el pedido completo
    orders[order_number] = {
        "cliente": client_name,
        "productos": items,
        "total": total
    }

    print(f"\nPedido registrado correctamente para {client_name}. Total a pagar: ${total:,}")


# Función para consultar un pedido
def consult_order(orders):
    print("\n=== CONSULTAR PEDIDO ===")
    try:
        order_number = int(input("Ingrese el número de pedido a consultar: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    order = orders.get(order_number)
    if not order:
        print("No se encontró el pedido.")
        return

    print(f"\nPedido #{order_number}")
    print(f"Cliente: {order['cliente']}")
    print("Productos:")
    for item in order["productos"]:
        print(f"- {item['producto']} x{item['cantidad']} = ${item['subtotal']:,}")
    print(f"Total: ${order['total']:,}")


# Función para cancelar un pedido
def cancel_order(orders):
    print("\n=== CANCELAR PEDIDO ===")
    try:
        order_number = int(input("Ingrese el número de pedido a cancelar: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    if order_number in orders:
        del orders[order_number]
        print("Pedido cancelado correctamente.")
    else:
        print("No se encontró el pedido.")


# Función para ver todos los pedidos
def show_all_orders(orders):
    print("\n=== LISTA DE TODOS LOS PEDIDOS ===")
    if not orders:
        print("No hay pedidos registrados.")
        return

    for number, order in orders.items():
        print(f"\nPedido #{number} - Cliente: {order['cliente']} - Total: ${order['total']:,}")


# Función para generar reporte del día
def generate_report(orders):
    print("\n=== REPORTE DEL DÍA ===")
    if not orders:
        print("No hay pedidos registrados.")
        return

    total_orders = len(orders)
    total_income = sum(order["total"] for order in orders.values())
    average = total_income / total_orders
    highest_order = max(orders.items(), key=lambda x: x[1]["total"])

    print(f"Total de pedidos: {total_orders}")
    print(f"Total recaudado: ${total_income:,}")
    print(f"Promedio por pedido: ${average:,.2f}")
    print(f"Pedido con mayor valor: #{highest_order[0]} - ${highest_order[1]['total']:,}")


# Función principal del sistema
def main():
    orders = {}  # Diccionario para almacenar todos los pedidos

    while True:
        print("\n=== SISTEMA DE GESTIÓN DE PEDIDOS ===")
        print("1. Registrar pedido")
        print("2. Consultar pedido")
        print("3. Cancelar pedido")
        print("4. Ver todos los pedidos")
        print("5. Generar reporte del día")
        print("0. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            register_order(orders)
        elif option == "2":
            consult_order(orders)
        elif option == "3":
            cancel_order(orders)
        elif option == "4":
            show_all_orders(orders)
        elif option == "5":
            generate_report(orders)
        elif option == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar el sistema
if __name__ == "__main__":
    main()
