# # Definición de cadena de carateres e impresión del tipo de dato
# cadena = "Programa en Python"
# print(type(cadena))




# # Uso de la barra invertida dentro de una cadena de caracteres
# print("Decimos 'si' entre comillas")
# #Decimos 'si' entre comillas
# print('Decimos \'si\' entre comillas')
# #Decimos 'si' entre comillas

cadena = "Texto en phyton"
# cadena[0] es el primer caracter
'T'
# cadena[-1]
'n' 
print(cadena[0])
print(cadena[-1])


print("========================================================================")
# Segmentación (rebanado de texto)
cadenaDos = "Programa en Python"
print(cadenaDos[0:8:1]) #comienza en 0 y termina en 8 y va de 1 en 1

print(cadenaDos[12:18:1]) #comienza en 12 y termina en 18 y va de 1 en 1


print("========================================================================")
#Concatenación de cadenas
nombre = "David"
apellido = "Villamil"
print(nombre + " " + apellido)

print("========================================================================")
#Split permite la separación de una cadena acorde a un parámetro



print("========================================================================")
# uso de format para concatenar cadenas de texto
print("Mi {} se llama {} y tiene {} años".format("Amigo", "Alberto", "25"))
'Mi Amigo se llama Alberto y tiene 25 años'



print("========================================================================")
mensaje = "Hola"
mensaje += " "
mensaje += "Mundo"
print(mensaje)