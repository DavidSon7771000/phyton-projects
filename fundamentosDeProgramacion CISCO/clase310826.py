# Creamos la matriz vacía
matriz = []

# Capturamos datos de 3 alumnos
for i in range(3):
    print(f"\nAlumno {i + 1}")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    calificacion = float(input("Calificación: "))

    matriz.append([nombre, apellido, calificacion])

# Mostramos los alumnos
print("\nLista de alumnos:")

for alumno in matriz:
    print(alumno[0], alumno[1], alumno[2])

# Sumamos las calificaciones
suma = 0

for alumno in matriz:
    suma = suma + alumno[2]

# Calculamos el promedio general
promedio = suma / 3

print("\nPromedio general del grupo:", promedio)
