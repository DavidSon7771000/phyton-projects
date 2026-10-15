#programa cajero de boletos


totalBoletos = 0

while True:
    boletos = int(input("Ingrese el numero de boletos que desea comprar: "))

    if boletos == 0:
        break
    elif boletos > 5:
        print("No puedes comprar más de 5 boletos")
    elif boletos < 0:
        print("Cantidad inválida")
    else:
        totalBoletos += boletos
        print(f"El total de boletos que desea compra es {totalBoletos} boletos")



totalDinero = totalBoletos * 50

for boleto in range(totalBoletos):
    print(f"Gracias por su compra")


print(f"El total de la compra es de {totalDinero} pesos por {totalBoletos} boletos")