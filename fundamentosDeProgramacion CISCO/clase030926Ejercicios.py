print("\n")
print("===========================================")
ciudades = ("Roma", "Madrid", "Paris", "Villahermosa", "Londres")
print(ciudades[0:3])
print(ciudades[0], ciudades [4])
print("===========================================")
print("\n")





numeros = (10, 20, 30, 40, 50)
indice = numeros[2]
print(indice)
print("===========================================")
print("\n")






tuplaPrincipal = (("David", "villami", "Borjas", ), ["a", "b", "c"])

elemento = tuplaPrincipal[1][1]
print(elemento)
print("===========================================")
print("\n")
#TUPLA ()
#LISTA []
#MATRIZ []
#       []


# colores = ("rojo", "verde", "azul")
# colores[1] = "amarillo"
#NO SE PUEDE PORQUE LAS TUPLAS SON IMMUTABLES
print("NO SE PUDO CORRER EL PROCESO PORQUE LAS TUPLAS SON INMUTABLES")
print("===========================================")
print("\n")




persona = ("María", 25, "México")
a, b, c = persona
print(a)
print(b)
print(c)
print("===========================================")
print("\n")






frutas = ("manzana", "pera", "uva")
for elemento in frutas:
    print(elemento)
print("===========================================")
print("\n")



print("EJERCICIO FINAL CLASE")
carreras = ("Sistemas", "Derecho", "Arquitectura", "Contabilidad")
carrera2 = list(carreras)

carrera2[1] = "Medicina"

print(carreras)
print(carrera2)