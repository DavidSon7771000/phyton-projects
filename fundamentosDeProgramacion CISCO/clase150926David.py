#Biblioteca (Prestamo de libros)
import os



def libro():
    autor = input("Autor: ")
    anio = input("Año: ")
    editorial = input("Editorial: ")
    nombre = input("Nombre: ")



    return {
        "autor": autor,
        "anio": anio,
        "editorial": editorial,
        "nombre": nombre

    }


def guardarEscritorio(unLibro):
    escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
    rutaArchivo = os.path.join(escritorio, "libros_biblioteca.txt")

    with open(rutaArchivo, "a", encoding="utf-8") as archivo:
        archivo.write(f"{unLibro['autor']}, {unLibro['anio']}, {unLibro['editorial']}, {unLibro['nombre']}\n")





biblioteca = []





primerLibro = libro()
biblioteca.append(primerLibro)
guardarEscritorio(primerLibro)
print(primerLibro)

print("Desea agregar mas libros? (si/no)")
opcion = input().strip().lower()

while opcion == "si":
    nuevoLibro = libro()
    biblioteca.append(nuevoLibro)
    guardarEscritorio(nuevoLibro)
    print(nuevoLibro)


    print("Desea agregar mas libros? (si/no)")
    opcion = input().strip().lower()



print("Todos tus libros registrados:")
for unLibro in biblioteca:
    print(unLibro)


