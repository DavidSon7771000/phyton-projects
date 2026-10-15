# paises = ["México", "Holanda", "Portugal", "Noruega", "España" ]
# print(paises[3])
# paises.append("Tabasco")
# print(paises)
# del paises[2]
# print(paises)



#Programa que pida cuantas frutas tendrá la lista e imprimer posición 4

# frutas = []
# cantidad = int(input("¿Cuántas frutas tendrá la lista?"))
# if cantidad < 5 or cantidad > 6:
#     print("Las frutas deben ser 4 elementos")
# else:
#     for i in range(cantidad):
#         nombre = input("Ingrese su tipo de fruta: ")
#     frutas.append(nombre)
# print(cantidad[4])

#programa imprimir cuadrado de lista de numeros
# numeros = [1,2,3,4,5,6]
# # for i in numeros:
# #     print(f"Numero {i} es: {i**2}")

# print(f"La suma de los numeros es: {sum(numeros)}")
# print(f"Los numeros pares son: {[x for x in numeros if x%2==0]}")
# print(f"Los numeros impares son: {[x for x in numeros if x%2!=0]}")

print("================================================================")



# colores = ["Rojo", "Naranja", "Azul", "Verde", "Amarillo", "Gris"]
# colores.insert(3, "Negro")
# print(colores)


colores = ["rojo", "naranja", "azul", "verde", "amarillo", "gris"]
print("¿Cuál color está buscando?")
color = input("").strip().lower()
if color in colores:
    print("¡Es un color válido!")
else:
    print("Ese color no está registrado en la lista")