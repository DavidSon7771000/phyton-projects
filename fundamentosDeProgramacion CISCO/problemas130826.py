print("Problematicas")
input("Presiona enter para continuar...")
print("Ejercicio 1: Conversión de temperatura celsius a fahrenheit y kelvin")
print("")
print("Ingrese la temperatura en grados Celsius:")
celsius = float(input())
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")
print(f"La temperatura en grados Kelvin es: {kelvin}")
input("Presiona enter para continuar...")
print("===================================================================")
print("Ejercicio 2: Calcula el perímetro de un círculo")
print("")
print("Ingrese el radio del círculo:")
radio = float(input())
perimetro = 2 * 3.1416 * radio
print(f"El perímetro del círculo es: {perimetro}")
input("Presiona enter para continuar...")
print("===================================================================")
print("Ejercicio 3: Volumen de un cubo")
print("")
print("Ingrese la longitud de un lado del cubo en cm:")
lado = float(input())
volumen = lado **3
print(f"El volumen del cubo es: {volumen} cm³")
input("Presiona enter para continuar...")
print("===================================================================")
print("Ejercicio 4: Conversión de metros a centímetros")
print("")
print("Ingrese la longitud en metros:")
centimetros = float(input()) * 100
print(f"La longitud en centímetros es: {centimetros} cm")
input("Presiona enter para continuar...")
print("===================================================================")
print("Ejercicio 5: Pasar de horas a segundos")
print("")
print("Ingrese la cantidad de horas:")
segundos = float(input()) * 3600
print(f"La cantidad de segundos es: {segundos} seg")
input("Presiona enter para continuar...")
print("===================================================================")
print("Ejercicio 6: Calcular el precio de un producto con el 21% de IVA")
print("")
print("Ingrese el precio del producto:")
precioFinal = float(input()) * 1.21
print(f"El precio final del producto con 21% de IVA es: {precioFinal}")


