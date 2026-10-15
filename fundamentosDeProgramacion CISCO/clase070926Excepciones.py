# try:
#     # 1. Código que podria fallar o causar un error
#     numero = int(input("Ingresa un número: "))
#     resultado = 10 / numero
#     print(f"El resultado es: {resultado}")

# except ZeroDivisionError:
#     # 2. Qué hacer si el usuario ingresó 0
#     print("¡Error! No puedes dividir entre cero.")

# except ValueError:
#     # 3. Qué hacer si el usuario ingresó texto en vez de números
#     print("¡Error! Debes ingresar un número entero válido.")




    #Crear diccionario de animales, mandarlo a imprimir, usar un try para mandar a buscar una key que no existe y poder usar el except

animales = {
    "perro": "Beagle" " Lucky",
    "gato": "Gato Siámes" " Leia",
    "serpiente": "Piton bola" " Sneaky",
}

print(animales)


try:
    busqueda = input("Ingresa la clave del animal: ").strip().lower()
    print(f"El animal es: {animales[busqueda]}")
except KeyError:
    print("ERROR; La key (clave) buscada no existe en el diccionario de animales")




# try:
#     busqueda = animales["Pájaro"]
#     print(f"El animal es: {busqueda}")
# except KeyError:
#     print("ERROR; La key (clave) buscada no existe en el diccionario de animales")