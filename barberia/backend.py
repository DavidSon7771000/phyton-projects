# ==============================================================================
# BACKEND - BARBERÍA IMPERIAL / EL PELÓN (CORREGIDO)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. ESTRUCTURAS DE DATOS (Catálogos)
# ------------------------------------------------------------------------------
servicios = {
    1: ("Corte de Cabello Tradicional", 200.00),
    2: ("Arreglo / Delineado de Barba", 150.00),
    3: ("Combo Imperial (Corte + Barba)", 300.00),
    4: ("Tinte / Camuflaje de Canas", 400.00),
    5: ("Limpieza Facial y Mascarilla", 180.00)
}

productos = {
    "Cera de Peinado": 120.00,
    "Minoxidil Tónico": 350.00,
    "Gel Extra Firme": 80.00,
    "Espuma de Afeitar": 110.00,
    "Shampoo Anticaída": 160.00
}

barberos = ["Carlos (Master)", "Alex (Senior)", "Mateo (Junior)"]


# ------------------------------------------------------------------------------
# 2. REGLAS DE NEGOCIO Y VALIDACIONES DE SERVICIOS
# ------------------------------------------------------------------------------
def gestionarSeleccion(opcion, serviciosElegidos):
    """
    Administra la lista de servicios seleccionados garantizando las reglas de combos:
    - Si se elige Combo Imperial (3), remueve Corte (1) y Barba (2).
    - Si se elige Corte (1) o Barba (2), remueve el Combo (3).
    - Si están seleccionados Corte (1) y Barba (2), se unifican en Combo (3).
    """
    # Trabajar con una copia para evitar inconsistencias de mutabilidad
    seleccion = list(serviciosElegidos)

    if opcion in (1, 2):
        if 3 in seleccion:
            seleccion.remove(3)
        if opcion not in seleccion:
            seleccion.append(opcion)

    elif opcion == 3:
        seleccion = [s for s in seleccion if s not in (1, 2)]
        if 3 not in seleccion:
            seleccion.append(3)

    elif opcion in (4, 5):
        if opcion not in seleccion:
            seleccion.append(opcion)

    # Regla de unificación automática a Combo 3
    if 1 in seleccion and 2 in seleccion:
        seleccion.remove(1)
        seleccion.remove(2)
        seleccion.append(3)

    return seleccion


# ------------------------------------------------------------------------------
# 3. FUNCIONES DE CÁLCULO Y OPERACIONES FINANCIERAS
# ------------------------------------------------------------------------------
def calcular_total_servicios(serviciosElegidos):
    """Suma el subtotal correspondiente a los servicios acumulados."""
    return sum(servicios[s_id][1] for s_id in serviciosElegidos if s_id in servicios)


def calcular_total_productos(productosElegidos):
    """Suma el subtotal correspondiente a los productos consumidos."""
    return sum(
        precio * productosElegidos[p_nombre]
        for p_nombre, precio in productos.items()
        if p_nombre in productosElegidos
    )


def calcular_total_general(serviciosElegidos, productosElegidos):
    """Calcula la suma global (servicios + productos)."""
    return calcular_total_servicios(serviciosElegidos) + calcular_total_productos(productosElegidos)


def calcular_comision(total_servicios, porcentaje=0.40):
    """Calcula la comisión del barbero aplicada exclusivamente sobre los servicios."""
    return total_servicios * porcentaje


def calcular_cambio(pago_con, total_general):
    """Calcula la diferencia a devolver en efectivo."""
    if pago_con < total_general:
        raise ValueError("El monto entregado es inferior al total de la cuenta.")
    return pago_con - total_general


# ------------------------------------------------------------------------------
# 4. GESTIÓN DE MÉTODOS DE PAGO Y PROPINA (TERMINAL)
# ------------------------------------------------------------------------------
def seleccionar_metodo_pago(total_general):
    """Despliega el menú de cobro y valida las entradas con bucles de reintento."""
    print("\nMÉTODOS DE PAGO DISPONIBLES:")
    print("1. Efectivo")
    print("2. Tarjeta (Débito / Crédito)")
    print("3. Transferencia (SPEI)")

    while True:
        opcion_pago = input("Seleccione el método de pago (1, 2 o 3): ").strip()
        if opcion_pago in ("1", "2", "3"):
            break
        print("Opción inválida. Intente de nuevo.")

    pago_con = 0.0
    cambio = 0.0

    if opcion_pago == "1":
        metodo_nombre = "Efectivo"
        while True:
            try:
                pago_con = float(input(f"Total a pagar ${total_general:.2f}. Ingrese el pago del cliente: $"))
                cambio = calcular_cambio(pago_con, total_general)
                print(f"Cambio a entregar: ${cambio:.2f}")
                break
            except ValueError as e:
                print(f"Error: {e}. Ingrese un monto válido.")

    elif opcion_pago == "2":
        metodo_nombre = "Tarjeta (Débito / Crédito)"
        pago_con = total_general
        print("Procesando pago en la terminal bancaria... ¡PAGO APROBADO!")

    elif opcion_pago == "3":
        metodo_nombre = "Transferencia (SPEI)"
        pago_con = total_general
        print("Verificando clave de rastreo SPEI... ¡TRANSFERENCIA CONFIRMADA!")

    # Captura de propina
    propina = 0.0
    entrada_propina = input("\n¿Desea agregar propina para el barbero? (s/n o ingrese el monto directo): ").strip().lower()

    if entrada_propina == "s":
        while True:
            try:
                propina = float(input("Monto de propina: $"))
                if propina < 0:
                    raise ValueError
                break
            except ValueError:
                print("Monto inválido. Ingrese un número mayor o igual a 0.")
    elif entrada_propina != "n" and entrada_propina != "":
        try:
            val = float(entrada_propina)
            propina = val if val >= 0 else 0.0
        except ValueError:
            print("Entrada no reconocida, se registrará $0.00 de propina.")

    return metodo_nombre, pago_con, cambio, propina


# ------------------------------------------------------------------------------
# 5. EJECUCIÓN INTERACTIVA EN TERMINAL Y GENERACIÓN DE TICKET DETALLADO
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("========================================")
    print("      SISTEMA POS BARBERÍA IMPERIAL     ")
    print("========================================\n")

    servicios_elegidos = []
    productos_elegidos = {}

    # --- PASO 1: SELECCIÓN DE SERVICIOS ---
    while True:
        print("\n--- CATÁLOGO DE SERVICIOS ---")
        for s_id, (nombre, precio) in servicios.items():
            print(f"{s_id}. {nombre} - ${precio:.2f}")
        print("0. Finalizar selección de servicios")

        try:
            opc = int(input("\nSeleccione un servicio (0 para terminar): "))
            if opc == 0:
                break
            if opc in servicios:
                servicios_elegidos = gestionarSeleccion(opc, servicios_elegidos)
                print("\n-> Servicios acumulados en la cuenta:")
                for s in servicios_elegidos:
                    print(f"   • {servicios[s][0]} (${servicios[s][1]:.2f})")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor, ingrese un número entero.")

    # --- PASO 2: SELECCIÓN DE PRODUCTOS ---
    while True:
        print("\n--- CATÁLOGO DE PRODUCTOS ---")
        lista_prods = list(productos.keys())
        for idx, p_nom in enumerate(lista_prods, 1):
            print(f"{idx}. {p_nom} - ${productos[p_nom]:.2f}")
        print("0. Finalizar selección de productos")

        try:
            opc_p = int(input("\nSeleccione un producto (0 para terminar): "))
            if opc_p == 0:
                break
            if 1 <= opc_p <= len(lista_prods):
                p_elegido = lista_prods[opc_p - 1]
                productos_elegidos[p_elegido] = productos_elegidos.get(p_elegido, 0) + 1
                print(f"-> Agregado: 1x {p_elegido}")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor, ingrese un número entero.")

    # --- PASO 3: CÁLCULOS Y COBRO ---
    total_serv = calcular_total_servicios(servicios_elegidos)
    total_prod = calcular_total_productos(productos_elegidos)
    total_gen = calcular_total_general(servicios_elegidos, productos_elegidos)

    if total_gen > 0:
        metodo, pago, cambio, propina = seleccionar_metodo_pago(total_gen)

        # --- IMPRESIÓN DEL TICKET COMPLETO ---
        print("\n========================================")
        print("          TICKET DE VENTA IMPERIAL      ")
        print("========================================")

        print("\nSERVICIOS REALIZADOS:")
        if servicios_elegidos:
            for s_id in servicios_elegidos:
                nombre_s, precio_s = servicios[s_id]
                print(f" - {nombre_s:<32} ${precio_s:>6.2f}")
        else:
            print(" - Sin servicios")

        print("\nPRODUCTOS VENDIDOS:")
        if productos_elegidos:
            for p_nom, cant in productos_elegidos.items():
                p_subtotal = productos[p_nom] * cant
                print(f" - {cant}x {p_nom:<29} ${p_subtotal:>6.2f}")
        else:
            print(" - Sin productos")

        print("\n----------------------------------------")
        print(f"Subtotal Servicios:             ${total_serv:>7.2f}")
        print(f"Subtotal Productos:             ${total_prod:>7.2f}")
        print(f"TOTAL GENERAL:                  ${total_gen:>7.2f}")
        print("----------------------------------------")
        print(f"Método de Pago:                 {metodo}")
        if metodo == "Efectivo":
            print(f"Monto Entregado:                ${pago:>7.2f}")
            print(f"Cambio Entregado:               ${cambio:>7.2f}")
        print(f"Propina Barbero:                ${propina:>7.2f}")
        print(f"Comisión Barbero (40% serv):    ${calcular_comision(total_serv):>7.2f}")
        print("========================================\n")
    else:
        print("\nNo se seleccionó ningún ítem. Venta cancelada.")