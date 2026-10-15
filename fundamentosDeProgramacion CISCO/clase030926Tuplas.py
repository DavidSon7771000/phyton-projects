#Accesar elementos de una tupla
tupla = (1, 2, 3, 4, 5)
print(tupla[0]) #Imprime el primer elemento: 1
print(tupla[2:4]) #Imprime una posición de la tupla: 3,4

#Desempaquetado de una tupla
tupla = (1, 2, 3, 4, 5)
a, b, c, d, e = tupla
print(a) #Imprime el primer elemento: 1
print(b) #Imprime el segundo elemento: 2
print(c) #Imprime el tercer elemento: 3
print(d) #Imprime el cuarto elemento: 4
print(e) #Imprime el quinto elemento: 5


#Concatenando tuplas
tupla1 = (1, 2, 3, 4, 5)
tupla2 = (6, 7, 8, 9, 10)
tuplaConcatenada = tupla1 + tupla2
print(tuplaConcatenada) #Imprime (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#Comparadndo tuplas
tupla1 = (1, 2, 3, 4, 5)
tupla2 = (6, 7, 8, 9, 10)
print(tupla1 == tupla2) #Imprime False
print(tupla1 != tupla2) #Imprime True

#Midiendo la longitud de una tupla
tupla = (1, 2, 3, 4, 5)
print(len(tupla)) #Imprime 5

print("\n")

# #Iterando una tupla
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

print("\n")

#Busqueda de un elemento en una tupla
tupla = (1, 2, 3, 4, 5)
indice = tupla.index(3)
print(indice) #Imprime: 2




print("\n")
print("===========================================")
print("Ejemplo de uso de tuplas")
print("===========================================")

#Cálculo de la distancia entre dos puntos
import math

# Lista de coordenadas
coordenadas = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Función para calcular la distancia euclidiana entre dos puntos
def distancia_euclidiana(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distancia = math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)
    return distancia

# Calcular la distancia euclidiana entre cada par de puntos
for i in range(len(coordenadas)):
    for j in range(i + 1, len(coordenadas)):
        distancia = distancia_euclidiana(coordenadas[i], coordenadas[j])
        print(f"La distancia entre {coordenadas[i]} y {coordenadas[j]} es: {distancia}")