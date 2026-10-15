print("=================================")
print("Museo de Antropología e Historia")
print("=================================")

p1=30.0
p2=45.0
print("Descuentos:")
mayor=0.12
profesor=0.10
estudiante=0.10

print("\n      Costos")
print("  Tipo de Visitante A\t Descuentos")
print("=====================================")
print("     Adulto mayor\t   ",                "12%")
print("     Profesor\t           ",                    "10%")
print("     Estudiante\t           ",                  "10%")
print()
personas=int(input("Cuántos boletos desea comprar:"))
for i in range(personas):
    edad=int(input("Ingrese la edad de la persona:"))
    print()
    tipo=int(input("Seleccione:1)Profesor 2)Adulto Mayor 3)Menor de Edad 4)Estudiante:"))

    if edad>=18 and tipo==1:
        profesor=p2profesor
        p2-=profesor
        print("Cantidad de boleto a pagar:",p2)
    elif edad>=18 and tipo==2:
        mayor=p2mayor
        p2=p2-mayor
        print("Cantidad de boleto a pagar:",p2)
    elif edad<18 and edad>=3 and tipo==4:
        estudiante=p1*estudiante
        p1=p1-estudiante
        print("Cantidad de boleto a pagar:",p1)
    elif edad<18 and edad>=3 and tipo==3:
            print("Cantidad de boleto a pagar:",p1)
    elif edad<3:
            p1=0
            print("Cantidad de boleto a pagar:",p1)