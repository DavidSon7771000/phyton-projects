#Quiz de David Villamil Borjas

tupla = ("Nombre", "Apellido", "Dirección", "Telefono")
lista = list(tupla)

lista.insert(2, "Edad")

lista.append("Codigo Postal")

tuplaFinal = tuple(lista)
print(tuplaFinal)

input("Presione enter para salir")