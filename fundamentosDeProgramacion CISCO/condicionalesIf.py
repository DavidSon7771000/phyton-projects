#nombre = str(input("Ingrese su nombre: "))
#promedio = float(input("Ingrese su promedio del 0.0 al 10.0: "))
#if promedio <= 5:
#    print(f"Hola {nombre}, tu promedio es de {promedio}, es deficiente, debes mejorar")
#elif promedio > 5 and promedio <= 7:
#    print(f"Hola {nombre}, tu promedio es de {promedio}, es regular, debes esforzarte más")
#elif promedio > 7 and promedio <= 9:
#    print(f"Hola {nombre}, tu promedio es de {promedio}, es bueno, sigue así")
#elif promedio > 9 and promedio <= 10:
#    print(f"Hola {nombre}, tu promedio es de {promedio}, es sobresaliente, felicidades")
#elif promedio > 10:
#    print(f"Hola {nombre}, tu promedio es de {promedio}, es inválido, el promedio debe ser de 0.0 a 10.0")



#nombre = str(input("Ingrese su nombre: "))
#edad = int(input("Ingrese su edad: "))

#print(f"Hola {nombre}, tu edad es de {edad} años")
#print("Talleres disponibles:")
#print("- Taller de Natación")
#print("- Taller de Equitación")
#print("- Taller de Tenis")

#taller = str(input("Ingrese el taller al que desea inscribirse: ")).strip().lower()
#certificado = str(input("¿Cuenta con certificado médico? (si/no): ")).strip().lower()

#if edad >= 8 and ("equitacion" in taller or "equitación" in taller):
#    print(f"Hola {nombre}, tu edad es de {edad} años, puedes inscribirte en el taller de equitación")

#elif ("natacion" in taller or "natación" in taller) and certificado in ["si", "sí"]:
#    print(f"Hola {nombre}, tu edad es de {edad} años, puedes inscribirte en el taller de natación")

#else:
#    print(f"Hola {nombre}, tu edad es de {edad} años, puedes inscribirte en el taller de tenis")

herencia = float (input("¿Cuánto vale la herencia? "))
casado = str (input("¿Eres casado? (Si/No) ")).strip().lower()
hijos = int (input("¿Cuántos hijos tienes? "))

if casado == "si" or casado == "sí":
    estaCasado = True
elif casado == "no":
    estaCasado = False


if estaCasado == True and hijos >=1:
    print(f"Hola, a tu cónyugue le corresponde {herencia/2} como valor de la herencia")
elif estaCasado == True and hijos <=0:
    print(f"Hola, a ti te corresponde 0 pesos de herencia, a tu cónyuge le corresponde {herencia}")
elif estaCasado == False:
    print(f"Hola, te corresponde 0 pesos del valor de la herencia")
