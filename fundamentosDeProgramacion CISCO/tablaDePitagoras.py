#Título del Programa "Tabla de Pitágoras"
print("===================================")
print("\t Tabla de Pitágoras")
print("===================================","\n")

tabla=[]
for i in range(11):
    filas=[]
    for j in range(11):
        filas.append(j*i)
    tabla.append(filas)
print("    ",end=" ")
for i in range(1,11):
    print(f"{i:3}", end=" ")
print("\n","_"*45)

for i in range(1,11):
    print(f"{i:3}|", end=" ")
    for j in range(1,11):
        print(f"{tabla[i][j]:3}", end=" ")
    print()

print()
while True:
    print("Qué números desea multiplicar?, (Escriba '1000' para salir)",end="\n")

    dato1=int(input("Ingrese el primer numero del 1 al 10: "))
    if dato1 == 1000:
        break
    dato2=int(input("Ingrese el segundo numero del 1 al 10: "))
    if dato2 ==1000 or dato2 == 1000:
        break

    elif dato1 > 10 or dato1 <= 0 or dato2 > 10 or dato2 <= 0:
        print("No podemos multiplicar números menores de 1 y/o mayores de 10")
    elif dato1 < 10 or dato1 > 0 or dato2 < 10 or dato2 > 0:
        resultado=tabla[dato1][dato2]
        print(f"El resultado de {dato1} x {dato2} es {resultado}")

input("Presione Enter para salir")

