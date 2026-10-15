#____________________________
# Abrir el archivo en modo lectura
with open("archivo_nuevo.txt", "r") as archivo:
    # Recorrer cada línea del archivo
    for linea in archivo:
        print(linea.strip())


try:
    archivo = open("C:\\Users\\aogue\\OneDrive\\Varios\\Documentos\\archivo1.txt", "r")
    for linea in archivo:
        print(linea)

except FileNotFoundError:
    print("No existe el archivo")
except PermissionError:
    print("No tienes permisos")

archivo = open("archivo_nuevo.txt", "a")
archivo.write('\nmi')
archivo.write("\nnombre es")
archivo.write("\npedro")
#Esta instrucción cierra el archivo
archivo.close()

archivo = open("personas.txt", "a")

continuar = "s"

while continuar == "s":
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    ciudad = input("Ciudad: ")

    archivo.write(nombre + "," + edad + "," + ciudad + "\n")

    continuar = input("¿Desea agregar otra persona? (s/n): ")

archivo.close()

print("Datos guardados correctamente.")



archivo = open("ticket.txt", "a")
total_general = 0
archivo.write("\n")
archivo.write("===== TICKET DE VENTA =====\n")

while True:

    producto = input("Producto: ")

    cantidad = int(input("Cantidad: "))

    precio = float(input("Precio: "))

    total = cantidad * precio

    total_general += total

    archivo.write(f"{producto} {cantidad} x ${precio} = ${total}\n")

    opcion = input("¿Agregar otro producto? (s/n): ")

    if opcion.lower() != "s":
        break

archivo.write("--------------------------\n")

archivo.write(f"TOTAL A PAGAR: ${total_general}\n")

archivo.write("==========================\n")

archivo.close()
print("Ticket guardado correctamente.")
