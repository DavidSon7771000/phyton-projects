# ==============================================================================
# BACKEND - BARBERÍA EL PELÓN

# ------------------------------------------------------------------------------
# 1. CATÁLOGOS DE DATOS
# ------------------------------------------------------------------------------
import datetime
import sys


servicios = {
    1: ("Corte de Cabello Tradicional", 200.00),
    2: ("Arreglo / Delineado de Barba", 150.00),
    3: ("Combo Imperial (Corte + Barba)", 300.00),
    4: ("Tinte / Camuflaje de Canas", 400.00),
    5: ("Limpieza Facial y Mascarilla", 180.00)
}

productos = {
    "Cera": 120.00,
    "Minoxidil": 350.00,
    "Gel": 80.00,
    "Espuma de afeitar": 110.00,
    "Shampoo": 160.00
}

barberos = [
    {"nombre": "Josué", "experiencia": ""},
    {"nombre": "John", "experiencia": ""},
    {"nombre": "Alfredo", "experiencia": ""}
]


# ------------------------------------------------------------------------------
# 2. REGLAS
# ------------------------------------------------------------------------------
def gestionarSeleccion(opcion, serviciosElegidos):
    """Garantiza las reglas de unificación y sustitución de combos."""
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

    # Regla de unificación automática
    if 1 in seleccion and 2 in seleccion:
        seleccion.remove(1)
        seleccion.remove(2)
        seleccion.append(3)

    return seleccion


def calcularTicket(serviciosElegidos):
    """Calcula el subtotal y desglose de servicios."""
    ticket = [] 
    precioFinal = 0.0

    for sId in serviciosElegidos:
        nombre, precio = servicios[sId]
        ticket.append((nombre, precio))
        precioFinal += precio
    return ticket, precioFinal


def solicitarTexto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Por favor, ingrese un nombre válido (no puede estar vacío).")


# ------------------------------------------------------------------------------
# GESTIÓN DE PRODUCTOS (agregar / editar / eliminar del catálogo)
# ------------------------------------------------------------------------------
def agregarProductoNuevo(productos, lista_productos):
    """Da de alta un producto que no está en el catálogo."""
    print("\n--- Agregar producto nuevo ---")
    nombre = solicitarTexto("Nombre del producto nuevo: ")
    if any(n.lower() == nombre.lower() for n in productos):
        print("Ese producto ya existe en el catálogo.")
        return

    while True:
        try:
            precio = float(input("Precio del producto: $"))
            if precio <= 0:
                raise ValueError
            break
        except ValueError:
            print("Ingresa un precio válido mayor a 0.")

    productos[nombre] = precio
    lista_productos.append(nombre)
    print(f"-> '{nombre}' se agregó al catálogo con éxito.")


def editarProducto(productos, lista_productos, productosElegidos):
    """Permite renombrar, cambiar el precio o eliminar un producto existente."""
    print("\n--- Editar / eliminar producto ---")
    if not lista_productos:
        print("No hay productos en el catálogo.")
        return

    for index, nombre in enumerate(lista_productos, start=1):
        print(f"{index}. {nombre:<20} ${productos[nombre]:.2f}")

    try:
        opcion = int(input("Elige el producto a editar (0 para cancelar): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return
    if opcion == 0:
        print("Operación cancelada.")
        return
    if not (1 <= opcion <= len(lista_productos)):
        print("Opción no válida.")
        return

    nombre_actual = lista_productos[opcion - 1]
    print(f"\nEditando: {nombre_actual}")
    print("1. Cambiar nombre")
    print("2. Cambiar precio")
    print("3. Eliminar producto")
    print("0. Cancelar")

    try:
        accion = int(input("Elige una opción: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

    if accion == 1:
        nuevo_nombre = solicitarTexto("Nuevo nombre: ")
        if any(n.lower() == nuevo_nombre.lower() and n != nombre_actual for n in productos):
            print("Ya existe otro producto con ese nombre.")
            return
        precio = productos.pop(nombre_actual)
        productos[nuevo_nombre] = precio
        lista_productos[lista_productos.index(nombre_actual)] = nuevo_nombre
        if nombre_actual in productosElegidos:
            productosElegidos[nuevo_nombre] = productosElegidos.pop(nombre_actual)
        print(f"-> Producto renombrado a '{nuevo_nombre}'.")

    elif accion == 2:
        try:
            nuevo_precio = float(input("Nuevo precio: $"))
            if nuevo_precio <= 0:
                raise ValueError
        except ValueError:
            print("Precio inválido. No se realizaron cambios.")
            return
        productos[nombre_actual] = nuevo_precio
        print(f"-> Precio de '{nombre_actual}' actualizado a ${nuevo_precio:.2f}.")

    elif accion == 3:
        confirmar = input(f"¿Seguro que deseas eliminar '{nombre_actual}'? (si/no): ").strip().lower()
        if confirmar == "si":
            del productos[nombre_actual]
            lista_productos.remove(nombre_actual)
            productosElegidos.pop(nombre_actual, None)
            print(f"-> '{nombre_actual}' se eliminó del catálogo.")
        else:
            print("Operación cancelada.")

    elif accion == 0:
        print("Operación cancelada.")
    else:
        print("Opción no válida.")


# ------------------------------------------------------------------------------
# GESTIÓN DE BARBEROS (elegir / agregar / editar / eliminar)
# ------------------------------------------------------------------------------
def agregarBarbero(barberos):
    """Da de alta un barbero nuevo en el equipo."""
    print("\n--- Agregar barbero nuevo ---")
    nombre = solicitarTexto("Nombre completo: ")
    if any(b["nombre"].lower() == nombre.lower() for b in barberos):
        print("Ya existe un barbero con ese nombre.")
        return
    experiencia = input("Experiencia (ej. 3 años, opcional): ").strip()
    barberos.append({"nombre": nombre, "experiencia": experiencia})
    print(f"-> '{nombre}' se agregó al equipo con éxito.")


def editarBarbero(barberos):
    """Permite renombrar, cambiar la experiencia o eliminar a un barbero."""
    print("\n--- Editar / eliminar barbero ---")
    if not barberos:
        print("No hay barberos registrados.")
        return

    for index, b in enumerate(barberos, start=1):
        exp = f" ({b['experiencia']})" if b["experiencia"] else ""
        print(f"{index}. {b['nombre']}{exp}")

    try:
        opcion = int(input("Elige el barbero a editar (0 para cancelar): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return
    if opcion == 0:
        print("Operación cancelada.")
        return
    if not (1 <= opcion <= len(barberos)):
        print("Opción no válida.")
        return

    barbero = barberos[opcion - 1]
    print(f"\nEditando: {barbero['nombre']}")
    print("1. Cambiar nombre")
    print("2. Cambiar experiencia")
    print("3. Eliminar barbero")
    print("0. Cancelar")

    try:
        accion = int(input("Elige una opción: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

    if accion == 1:
        nuevo_nombre = solicitarTexto("Nuevo nombre: ")
        if any(b["nombre"].lower() == nuevo_nombre.lower() and b is not barbero for b in barberos):
            print("Ya existe otro barbero con ese nombre.")
            return
        barbero["nombre"] = nuevo_nombre
        print(f"-> Barbero renombrado a '{nuevo_nombre}'.")

    elif accion == 2:
        barbero["experiencia"] = input("Nueva experiencia: ").strip()
        print(f"-> Experiencia de '{barbero['nombre']}' actualizada.")

    elif accion == 3:
        confirmar = input(f"¿Seguro que deseas eliminar a '{barbero['nombre']}'? (si/no): ").strip().lower()
        if confirmar == "si":
            barberos.remove(barbero)
            print(f"-> '{barbero['nombre']}' se eliminó del equipo.")
        else:
            print("Operación cancelada.")

    elif accion == 0:
        print("Operación cancelada.")
    else:
        print("Opción no válida.")


def elegirBarbero(barberos):
    """Deja escribir el nombre del peluquero libremente o elegir uno ya registrado."""
    while True:
        print("\n--- BARBEROS DISPONIBLES ---")
        for index, b in enumerate(barberos, start=1):
            exp = f" ({b['experiencia']})" if b["experiencia"] else ""
            print(f"{index}. {b['nombre']}{exp}")
        print("\nEscribe el número de un barbero, o escribe directamente su nombre.")
        print("También puedes escribir 'nuevo' para agregar un barbero o 'editar' para editar/eliminar uno.")
        entrada = input("Peluquero: ").strip()

        if not entrada:
            print("Por favor, ingresa un nombre o número válido.")
            continue

        if entrada.lower() == "nuevo":
            agregarBarbero(barberos)
            continue

        if entrada.lower() == "editar":
            editarBarbero(barberos)
            continue

        if entrada.isdigit():
            idx = int(entrada)
            if 1 <= idx <= len(barberos):
                return barberos[idx - 1]["nombre"]
            print("Número fuera de rango.")
            continue

        # Nombre escrito libremente: si coincide con uno existente lo usa tal cual,
        # si no, se toma como un peluquero nuevo (no registrado en el catálogo).
        coincidencia = next((b for b in barberos if b["nombre"].lower() == entrada.lower()), None)
        return coincidencia["nombre"] if coincidencia else entrada





#SE APLICA MEMBRESÍA O NO O SE COMPRA
def membresia(precio):
    comproMembresia = False
    print("\n---Membresía VIP---")
    print("Beneficios: 15% de descuento en todos los servicios y productos.")
    
    # Bucle por si cuenta con membresía
    while True:
        respuesta = input("¿Cuenta con membresía VIP? (si/no): ").strip().lower()
        if respuesta in ("si", "no"):
            break
        print("Opción no válida. Por favor ingresa si o no.")

    if respuesta == "si":
        descuento = 0.15 * precio
        precioFinal = precio - descuento
    else:
        # Bucle para adquirir membresía
        while True:
            adquirir = input("¿Desea adquirir la membresía VIP por $500? (si/no): ").strip().lower()
            if adquirir in ("si", "no"):
                break
            print("Opción no válida. Por favor ingresa si o no.")
            
        if adquirir == "si":
            comproMembresia = True
            descuento = 0.15 * precio
            precioFinal = (precio - descuento) + 500
        else:
            descuento = 0
            precioFinal = precio
            
    return descuento, precioFinal, comproMembresia

def calcularTotalProductos(productosElegidos):
    """Calcula el subtotal correspondiente a los productos seleccionados."""
    subtotal = 0.0
    for nombre, cantidad in productosElegidos.items():
        precio_unitario = productos[nombre]
        subtotal += precio_unitario * cantidad
    return subtotal

def tipo_de_pago(totalaPagar):
    print("\n---Propina---")
    propina = 0.0
    
    # Nuevo bucle estricto
    while True:
        agregarPropina = input("¿Desea agregar una propina para el barbero? (si/no): ").strip().lower()
        if agregarPropina in ("si", "no"):
            break
        print("Opción no válida. Por favor ingresa si o no.")

    if agregarPropina == "si":
        try:
            propina = float(input("Ingrese el monto de la propina: $"))
            if propina < 0:
                print("El monto de propina no puede ser negativo. Se registrará $0.00 de propina.")
                propina = 0.00
        except ValueError:
            print("Monto de propina no válido. Se registrará $0.00 de propina.")
            propina = 0.00

    totalaPagar += propina

    print("\n---Pago---")
    print("\n---Seleccione el tipo de pago:---")
    print("1. Efectivo")
    print("2. Tarjeta de crédito/débito")

    while True:
        try:
            opcion_pago = int(input("Ingrese el número correspondiente al tipo de pago: "))
            if opcion_pago == 1:
                print(f"Pago en efectivo. Total a pagar: ${totalaPagar:.2f}")
                print("Ingrese el monto a pagar:")
                while True:
                    try:
                        monto_pagado = float(input())
                        if monto_pagado < totalaPagar:
                            print(f"El monto insuficiente. Ingrese un monto igual o mayor a ${totalaPagar:.2f}.")
                        else:
                            cambio = monto_pagado - totalaPagar
                            print(f"Pago recibido: ${monto_pagado:.2f}")
                            print(f"Cambio a devolver: ${cambio:.2f}")
                            return opcion_pago,monto_pagado,cambio, propina, totalaPagar
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
            elif opcion_pago == 2:
                print(f"Pago con tarjeta. Total a pagar: ${totalaPagar:.2f}")
                monto_pagado = totalaPagar
                cambio = 0.00
                return opcion_pago, monto_pagado, cambio, propina, totalaPagar
            else:
                print("Opción no válida. Intente nuevamente.")

        except ValueError:
            print("Por favor, ingrese un número válido.")

        


#INICIAR SESIÓN
usuarioAutorizado = "barbero123"
password = "secret123"




# ------------------------------------------------------------------------------
# 3. PROCESAMIENTO y AUTENTIFICACIÓN
# ------------------------------------------------------------------------------

print("====================================================")
print("         AUTENTIFICACIÓN DE USUARIOS       ")
print("==================================================","\n")
while True:
    usuarioAutorizado = input("Ingresa el usuario: ").strip()
    password = input("Ingresa su contraseña: ").strip()

    if usuarioAutorizado == "barbero123" and password == "secret123":
        print("\n¡Acceso autorizado!, ¡Bienvenido al sistema!\n")
        break
    else:
        print("\nUsuario o contraseña incorrectos. Intente nuevamente.\n")







#BIENVENIDA
print("====================================================")
print("         BIENVENIDO A LA BARBERÍA EL PELÓN       ")
print("==================================================","\n")
cliente = solicitarTexto("Ingresa el nombre del cliente: ")
peluquero = elegirBarbero(barberos)

# --- SELECCIÓN DE SERVICIOS ---
serviciosElegidos = []

while True:
        print("\n--- MENÚ DE SERVICIOS ---")
        for sId, (nombre, precio) in servicios.items():
            print(f"{sId}. {nombre} - ${precio:.2f}")

        try:
            opcion = int(input("Elige un servicio (1-5): "))

            if opcion in servicios:
                serviciosElegidos = gestionarSeleccion(opcion, serviciosElegidos)
                print(f"Servicios actuales en tu lista: {serviciosElegidos}")
            else:
                print("Opción no válida. Intenta de nuevo.")
                continue
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
            continue


        while True:
            respuesta = input("¿Deseas agregar otro servicio? (si/no): ").strip().lower()
            if respuesta == "si":
                break
            elif respuesta == "no":
                break
            else:
                print("Opción no válida. Por favor ingresa si o no.")

        if respuesta == "no":
            break

# --- SELECCIÓN DE PRODUCTOS ---
productosElegidos = {}
lista_productos = list(productos.keys())

while True:
    print("\n=============================================")
    print("            CATÁLOGO DE PRODUCTOS            ")
    print("=============================================")
    
    for index, nombre in enumerate(lista_productos, start=1):
        precio = productos[nombre]
        print(f"{index}. {nombre:<20} ${precio:.2f}")
    print("-1. Eliminar / Restar un producto")
    print("-2. Agregar producto nuevo al catálogo")
    print("-3. Editar / eliminar un producto del catálogo")
    print("0. Finalizar selección de productos")

    try:
        opcion_p = int(input("\nElige un producto (-1 quitar, -2 agregar, -3 editar, 0 terminar): "))

        if opcion_p == 0:
            break

        elif opcion_p == -2:
            agregarProductoNuevo(productos, lista_productos)

        elif opcion_p == -3:
            editarProducto(productos, lista_productos, productosElegidos)

        elif opcion_p == -1:
            if productosElegidos:
                print("\n--- PRODUCTOS EN TU LISTA ---")
                for p_nombre, p_cantidad in productosElegidos.items():
                    print(f" • {p_nombre}: {p_cantidad} unidad(es)")

                prod_quitar = input("Ingresa el nombre del producto a restar: ").strip().lower()

                clave_encontrada = None
                for p_nombre in productosElegidos:
                    if p_nombre.lower() == prod_quitar:
                        clave_encontrada = p_nombre
                        break

                if clave_encontrada:
                    productosElegidos[clave_encontrada] -= 1
                    if productosElegidos[clave_encontrada] == 0:
                        del productosElegidos[clave_encontrada]
                    print(f"-> Se ha descontado una unidad de '{clave_encontrada}'.")
                else:
                    print("Producto no encontrado en tu lista.")
            else:
                print("No hay productos en tu lista para eliminar.")

        elif 1 <= opcion_p <= len(lista_productos):
            prod_nombre = lista_productos[opcion_p - 1]
            productosElegidos[prod_nombre] = productosElegidos.get(prod_nombre, 0) + 1
            print(f"-> ¡Agregado! Total {prod_nombre}: {productosElegidos[prod_nombre]}")

        else:
            print("Opción no válida. Intenta de nuevo.")

    except ValueError:
        print("Por favor, ingresa un número válido.")

# ------------------------------------------------------------------------------
# 4. PROCESAR Y MOSTRAR TICKET FINAL
# ------------------------------------------------------------------------------
ticket, totalServicios = calcularTicket(serviciosElegidos)
totalProductos = calcularTotalProductos(productosElegidos)
totalGeneral = totalServicios + totalProductos
print("\n=============================================")
print("             RESUMEN PREVIO DE COMPRA                ")
print("=============================================")
print(f"Subtotal Servicios:                 ${totalServicios:.2f}")
print(f"Subtotal Productos:                 ${totalProductos:.2f}")
print(f"Subtotal Acumulado:                 ${totalGeneral:.2f}")

#Confirmación de compra
while True:
    confirmar = input("¿Desea confirmar la compra? (si/no): ").strip().lower()
    if confirmar in ("si", "no"):
        break
    print("Opción no válida. Por favor ingresa si o no.")

if confirmar == "no":
    print("\nVenta cancelada. Saliendo del sistema...") 
    sys.exit()

# La lógica de negocio va FUERA del bucle de validación
descuento, totalPagar, comproMembresia = membresia(totalGeneral)

if totalPagar == 0:
    print("\nNo se seleccionó ningún servicio, producto ni membresía. Venta finalizada.")
    sys.exit()

pago, monto_pagado, cambio, propina, totalPagar = tipo_de_pago(totalPagar)


# ------------------------------------------------------------------------------

# Marca de tiempo única
fechaActual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Nombre de archivo
nombreArchivo = f"ticket_{cliente.replace(' ', '_')}_{fechaActual}.txt"

with open(nombreArchivo, "w", encoding="utf-8") as f:
    f.write("=============================================\n")
    f.write("             TICKET DE COMPRA                \n")
    f.write("=============================================\n")
    f.write(f"Cliente:   {cliente}\n")
    f.write(f"Atendió:   {peluquero}\n")
    f.write("---------------------------------------------\n")

    f.write("SERVICIOS:\n")
    if ticket:
        for concepto, precio in ticket:
            f.write(f" • {concepto:<30} ${precio:.2f}\n")
    else:
        f.write(" • Sin servicios\n")

    f.write("\nPRODUCTOS:\n")
    if productosElegidos:
        for nombre, cantidad in productosElegidos.items():
            subtotal_item = productos[nombre] * cantidad
            f.write(f" • {cantidad}x {nombre:<27} ${subtotal_item:.2f}\n")
    else:
        f.write(" • Sin productos\n")

    f.write("---------------------------------------------\n")
    f.write(f"Subtotal Servicios:                 ${totalServicios:.2f}\n")
    f.write(f"Subtotal Productos:                 ${totalProductos:.2f}\n")
    f.write(f"Compra de Membresía VIP:            ${(500.00 if comproMembresia else 0.00):.2f}\n")
    f.write(f"Descuento:                          ${descuento:.2f}\n")
    f.write(f"Propina:                            ${propina:.2f}\n")
    f.write(f"TOTAL A PAGAR:                      ${totalPagar:.2f}\n")
    f.write(f"Tipo de pago:                       {'Efectivo' if pago == 1 else 'Tarjeta'}\n")
    f.write(f"Monto pagado:                       ${monto_pagado:.2f}\n")
    f.write(f"Cambio a devolver:                  ${cambio:.2f}\n")
    f.write("=============================================\n")

print(f"\n¡Ticket guardado exitosamente como '{nombreArchivo}'!")