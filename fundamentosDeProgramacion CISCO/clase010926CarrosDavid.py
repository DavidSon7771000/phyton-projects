# Vehículos

matriz = []
costosFinales = []

print("¿Cuántos vehículos desea registrar?")
numVehiculos = int(input())

for i in range(numVehiculos):
    print(f"\n--- Registro del Vehículo {i + 1} ---")
    print(f"¿Cuál es la marca del vehículo {i + 1}?")
    marca = input()
    print(f"¿Cuál es el modelo del vehículo {i + 1}?")
    modelo = input()
    print(f"¿Cuál es el año del vehículo {i + 1}?")
    anio = int(input())
    print(f"¿Cuál es el color del vehículo {i + 1}?")
    color = input()
    print(f"¿Cuál es el costo del vehículo {i + 1}?")
    costoInicial = float(input())

    # Aplicación de descuento
    if costoInicial > 200000:
        costoFinal = costoInicial * 0.7
    else:
        costoFinal = costoInicial * 0.85
        
    print(f"El costo final del vehículo {i + 1} es: ${costoFinal:.2f}")

    # Guardar fila en la matriz y costo en la lista de suma
    matriz.append([marca, modelo, anio, color, costoInicial, costoFinal])
    costosFinales.append(costoFinal)

print("\n================ LISTA DE VEHÍCULOS ================")
for i in range(numVehiculos):
    print(f"Vehículo {i + 1}: Marca: {matriz[i][0]}, Modelo: {matriz[i][1]}, Año: {matriz[i][2]}, Color: {matriz[i][3]}, Costo Inicial: ${matriz[i][4]:.2f}, Costo Final: ${matriz[i][5]:.2f}")

print("----------------------------------------------------")
print(f"La suma total de los costos finales es: ${sum(costosFinales):.2f}\n")
