# print("================================================================")
# print("\tMuseo de Antropología e Historia de Villahermosa\n")
# print("================================================================")
# print("Tipo de visitante\t Descuento")
# print("================================================================")
# print("Adulto mayor\t           12%")
# print("Profesor\t           10%")
# print("Estudiante\t           10%")

# menores = 30                   #de 4 a 17 años
# mayores = 45                   #de 18 en adelante
# ninos = 0                      #de 0 a 3 años
# precioFinal = 0
# profesor =


# print("Bienvenido al museo de Antropolía e Historia de Villahermosa")
# boletos = int(input("¿Cuántos boletos desea? "))
# for personas in range(boletos):
#     edad = int(input("¿Cuántos años tienes?"))
#     if edad <= 3:
#         precioFinal = ninos
#         continue
#     elif edad > 3 and edad < 18:
#         precioFinal = menores
#         continue
#     elif edad > 18:
#         precioFinal = mayores
#     elif edad >= 60:
#         precioFinal = mayores * 0.88
#     else:
#     estatus = input("¿Eres un profesor o estudiante? ").strip().lower()
#     if estatus == "si":
#         precioFinal = precioFinal



TARIFA_MENOR = 30.0
TARIFA_MAYOR = 45.0
TARIFA_NINO = 0.0

DESC_ADULTO_MAYOR = 0.12  # 12%
DESC_ESTUDIANTE_PROF = 0.10  # 10%

precioFinal = 0.0
ticket = []

#MENÚ
print("==================================================")
print("\tMuseo de Antropología e Historia")
print("==================================================")
print("Tipo de visitante\tDescuento")
print("==================================================")
print("Adulto mayor\t\t12%")
print("Profesor\t\t10%")
print("Estudiante\t\t10%")
print("==================================================\n")

print("Bienvenido al museo de Antropología e Historia de Villahermosa")
boletos = int(input("¿Cuántos boletos desea? "))

#CICLO PRINCIPAL
for personas in range(1, boletos + 1):
    print(f"\n--- Datos para el boleto {personas} ---")
    edad = int(input("¿Cuántos años tienes?: "))

    # 1. Cláusula BREAK: Seguridad ante datos inválidos
    if edad < 0:
        print("\n[ERROR] Edad inválida ingresada. Cancelando la transacción...")
        break

    # 2. Cláusula CONTINUE: Niños menores de 3 años
    if edad <= 3:
        print("-> Los niños de 3 años o menos entran gratis.")
        ticket.append(f"Persona {personas} (Edad {edad}): Niño -> $0.00")
        continue  # Salta el resto y pasa directamente a la siguiente persona

    # 3. Determinación de precio y descuentos
    precio_boleto = 0.0
    descripcion = ""

    # Caso A: Menores de edad (4 a 17 años)
    if edad < 18:
        estatus = input("¿Eres estudiante? (si/no): ").strip().lower()
        if estatus == "si":
            precio_boleto = TARIFA_MENOR * (1 - DESC_ESTUDIANTE_PROF)
            descripcion = "Menor de edad (Estudiante - 10% desc.)"
        else:
            precio_boleto = TARIFA_MENOR
            descripcion = "Menor de edad"

    # Caso B: Adultos mayores (60 años o más) - Prioridad 12%
    elif edad >= 60:
        precio_boleto = TARIFA_MAYOR * (1 - DESC_ADULTO_MAYOR)
        descripcion = "Adulto mayor (12% desc.)"

    # Caso C: Adultos de 18 a 59 años
    else:
        estatus = input("¿Eres profesor o estudiante? (si/no): ").strip().lower()
        if estatus == "si":
            precio_boleto = TARIFA_MAYOR * (1 - DESC_ESTUDIANTE_PROF)
            descripcion = "Adulto (Profesor/Estudiante - 10% desc.)"
        else:
            precio_boleto = TARIFA_MAYOR
            descripcion = "Adulto (Tarifa regular)"

    # Acumulamos el costo y registramos en la lista para el ticket
    precioFinal += precio_boleto
    ticket.append(f"Persona {personas} (Edad {edad}): {descripcion} -> ${precio_boleto:.2f}")

# --- IMPRESIÓN DEL TICKET FINAL ---
print("\n==================================================")
print("\t\tTICKET DE COMPRA")
print("==================================================")
for linea in ticket:
    print(linea)
print("--------------------------------------------------")
print(f"TOTAL A PAGAR: ${precioFinal:.2f}")
print("==================================================")