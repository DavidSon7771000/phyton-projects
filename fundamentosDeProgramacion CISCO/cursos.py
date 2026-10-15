print("2")
print(2)

print(0o123)  #Octal
print(0x123)  #Hexadecimal

print(0b1010)  #Binary
print(2.5e2)  #Scientific notation, e= exponente, por diez a la número de la derecha
# número de avogadro = 6.02214076e23:
print(6.02214076e23)
print(0.0000000000000000000000000000001) #phyton pondrá una e= 1e-31= que significa 1x10^-31



print(2.5)
print(0.4)
print(.4)


#Cadenas
#para poner comillas dentro de una cadeana ya determinada por comillas
#opción 1: simplemente poner dos comillas y comillas simples
print('hola, me gusta la película "Orgullo y prejuicio"')
#opción 2: usar diagonal invertida
print("Hola, me gusta la pelicula \"Orgulla y prejuicio\"")
print("I´m David")
print("I\'m David")

print(True > False) #True equals 1
print(True < False) #False equals 0
#por lo tanto evalua 1 > 0 = True y posteriormente 1 < 0 = False
print(1 > 0) #True
print(1 < 0) #False

#Literales de phyton
print("Estoy", end = " ")
print("\"\"aprendiendo\"\"", end= " " ) 
#o
print('""aprendiendo""', end = " ")
print(" \"\"\"Phyton\"\"\"")
#O
print('"""Phyton"""')

print("==========================================")
print('"Estoy"\n ""aprendiendo""\n """Phyton"""')



print(10//2) #imprime solo el entero
print(10/2) #imprime el entero y el decimal
print("\n")



print(2 ** 3)     # Resultado: 8   (Entero) entero por entero
print(2 ** 3.)    # Resultado: 8.0 (Flotante) entero por flotante
print(2. ** 3)    # Resultado: 8.0 (Flotante) flotante por entero
print(2. ** 3.)   # Resultado: 8.0 (Flotante) flotante por flotante

#Lo mismo con suma, resta, multiplicacion y división

print(6 // 4)
print(6. // 4)
print(6 // 4.)
print(6. // 4.)

print(14 % 4) #Resultado: 2, porque 14 es divisible por 4 y residuo ES: 2
print(14. % 4) #% es para imprimir el residuo
print(14 % 4.)

print(2 + 3 * 5)





print("==========================================")
a = 1
while a <= 10:
    a = a + a
    print(a)

print(3/2)
print(3//2) #redondea hacia abajo




var1 = 1
var2 = 2

print(var1 < var2)
print(var1 > var2)
answer = print(var1 == var2)

print("-------------------------------------")
planta = input("¿Cuál es tu planta preferida? ")
if planta == "TULIPAN":
    print("Si, el TULIPAN ES MUY BONITO")
elif planta == "tulipan":
    print("No, quiero un gran tulipan")
else:
    print(f"No, es TULIPAN, NO {planta}")

