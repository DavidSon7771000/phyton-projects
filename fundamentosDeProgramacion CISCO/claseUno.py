print("Hola mundo")
print("Saúl\"Canelo\" Álvarez")
print("El primer presidente de México fue: \n\tGuadalupe Victoria")
print("Guárdalo en la carpeta: \\Mis documentos\\respaldo")


a=11
b=3.0

print("La suma es: ", a+b)
print("La resta es: ", a-b)
print("La multiplicación es: ", a*b)
print("La división es: ", a/b)
print("La división entera es: ", a//b)
print("El residuo es: ", a%b)
print("La exponenciación es: ", a**b)

x=input("Ingresa un número: ")
y=input("Dame otro número: ")

z = ((x == y) ) and (x != y) or not (x == y)
print("¿Son iguales? ", not (z))

print("===================================================================")
num1 = float(input("Ingresa un número: "))
num2 = float(input("Ingresa otro número: "))

print(f"La suma es: {num1 + num2}")

print("===================================================================")
altura = float(input("Ingresa tu altura en metros: "))
base = float(input("Ingresa la base de tu rectángulo en metros: "))
print(f"El área del triangulo es: {base * altura / 2} metros cuadrados")

print("===================================================================")
note1 = float(input("Ingresa tu primera calificación: "))
note2 = float(input("Ingresa tu segunda calificación: "))
note3 = float(input("Ingresa tu tercera calificación: "))

print(f"Tu promedio es: {(note1 + note2 + note3) / 3}")
print("Tu promedio")