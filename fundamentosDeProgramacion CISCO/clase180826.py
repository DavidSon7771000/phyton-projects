# herencia = float (input("¿Cuánto vale la herencia? "))
# casado = str (input("¿Eres casado? (Si/No) ")).strip().lower()
# hijos = int (input("¿Cuántos hijos tienes? "))
# herenciaTotal = (herencia / hijos) if hijos > 0 else 0

# if casado == "si" or casado == "sí":
#    estaCasado = True
# elif casado == "no":
#    estaCasado = False


# if estaCasado == True and hijos == 1:
#    print(f"Hola, a tu hijo le corresponde {herenciaTotal/2} como valor de la herencia.")
# elif estaCasado == True and hijos >= 2:
#    print(f"Hola, a cada hijo tuyo le corresponde {herenciaTotal/2} como valor de la herencia.")
# elif estaCasado == False and hijos == 1:
#    print(f"Hola, a tu hijo le corresponde {herenciaTotal/2} como Valor de la herencia.")
# elif estaCasado == False and hijos >= 1:
#    print(f"Hola, a cada uno de tus hijos le corresponde {herenciaTotal/2} como Valor de la herencia.")
# elif hijos == 0:
#    print(f"La cantidad de la herencia es 0")







#Ciclo while
# num = 501
# val = float(input("Ingrese un número: "))
# while val != num:
#     print("Valor incorrecto, vuelva a intentarlo")
#     val = float(input("Valor del número secreto: "))
# else:
#     print("Correcto")



contador = 1

final = 20

while contador < final:
    contador += 1
    print(f"El contador es {contador}")
    if contador == 10:
        break