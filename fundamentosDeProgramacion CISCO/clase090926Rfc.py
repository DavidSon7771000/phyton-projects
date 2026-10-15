#Crear rfc de una persona
nombre = "David"
ap = "Villamil"
am = "Borjas"
fecha = "25-06-2008"
homo = "RHB"

"vibd080625rhb"

rfc = "{}-{}-{}-{}-{}".format(nombre, ap, am, fecha, homo)
print(rfc)


print("========================================================================")
resultado = ((ap[0:2]) + (am[0:1]) + (nombre[0]) + (fecha[8:10]) + (fecha[3:5]) + (fecha[0:2]) + (homo)).upper()
print(resultado)