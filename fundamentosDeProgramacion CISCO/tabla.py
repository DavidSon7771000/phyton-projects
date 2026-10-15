#Se asignan los valores a las variables
verdadero=True
falso=False


#Se muestra la tabla de verdad
print("\n       Tabla de Verdad")
print("  A     B\t  and\t  or")
print("=================================")
print("True  True\t", verdadero and verdadero, "\t", verdadero or verdadero)
print("True  False\t", verdadero and falso, "\t", verdadero or falso)
print("False True\t", falso and verdadero, "\t", falso or verdadero)
print("False False\t", falso and falso, "\t", falso or falso)


print("\n       Tabla de verdad con not")
print("Condición  A     Condición B\t", verdadero,"\t",not verdadero)
print("Condición A     Condición B\t", falso,"\t",not falso)



print("==============================================================")
print("\n       Tabla de calificaciones")
print("Materia\t        P1\t        P2\t        P3")
print("==============================================================")
print("Física\t         8\t         9\t         6")
print("Química\t         9\t        10\t        10")
print("Biología\t 6\t         7\t        10")
print("Matemáticas\t 9\t         8\t         8")
print("Español\t         7\t         8\t         7")


#print("==============================================================")

#nombre = str(input("Ingrese su nombre: "))
#calificacion = float(input("ingresa tu calificación: "))
#print(f"Hola {nombre}, bienvenido")

#if calificacion >= 7:
#    print(f"felicidades {nombre}, aprobaste la materia con una calificación de {calificacion}")
#else:
#    print(f"Reprobaste {nombre}, tu calificación es de {calificacion}")

#print("")
#print("")
#print("==============================================================")
#print("Si tu venta es mayor a 40,000 tienes un descuento del 20%")
#venta = float(input("Ingrese el monto de la venta: "))
#descuento = 0.20
#montoDescuento = venta * descuento
#montoFinal = venta - montoDescuento

#if venta >= 40000:
#    print(f"Tu compra es de {venta}, por lo que tienes un descuento del 20% que equivale a {montoDescuento}, tu monto final a pagar es de {montoFinal}")
#else:
#    print(f"Tu compra es de {venta}, no tienes descuento")


#print("")
#print("")
#print("==============================================================")
#nombre = str(input("Ingrese su nombre: "))
#antiguedad = int(input("Ingrese su antigüedad en años: "))
#puntos = int(input("Ingrese su cantidad de puntos acumulados: "))

#if antiguedad >= 2 and puntos >=350:
#    print(f"felicidades {nombre}, tienes un ascenso por tu antigüedad  de {antiguedad} años y {puntos} puntos acumulados")
#else:
#    print(f"Lo sentimos {nombre}, no aplicas para un ascenso, tan solo tienes {antiguedad} años de antiguedad y {puntos} puntos acumulados")





# print("")
# print("")
# print("==============================================================")
# 7# Pregunta la edad de la persona
# edad=int(input("¿Qué edad tiene la persona? "))

# print("\nLa persona está en:")
# if edad>=0 and edad<6:
#     print("Infancia (0 a 6 años)")
# elif edad>=6 and edad<12:
#     print("Niñez (6 a 12 años)")
# elif edad>=12 and edad<20:
#     print("Adolescencia (12 a 20 años)")
# elif edad>=20 and edad<25:
#     print("Juventud (20 a 25 años)")
# elif edad>=25 and edad<60:
#     print("Adultez (25 a 60 años)")
# elif edad>=60:
#     print("Tercera Edad (60 años y más)")