# def suma(a,b):
#     print("La suma es:  ", a+b)

# suma(a=1, b=2)



def suma (numero1, numero2):
    return numero1 + numero2

def resta (numero1, numero2):
    return numero1 - numero2

def multiplicacion (numero1, numero2):
    return numero1 * numero2

def division (numero1, numero2):
    if numero2 == 0:
        return "No se puede dividir entre cero"
    else:
        return numero1 / numero2



while True:

    print("===========================================\n")
    print("Ingrese un primer número: ")
    numero1 = int(input())
    print("Ingrese un segundo número: ")
    numero2 = int(input())

    print("\n============ Menú de funciones  ============")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("===========================================")
    opcion = int(input("Elija una opción: "))
    print("===========================================")
    print("\n")



    if opcion == 1:
        resultado = suma(numero1, numero2)
        print(f"La suma es: {resultado}")
    elif opcion == 2:
        resultado = resta(numero1, numero2)
        print(f"La resta es: {resultado}")
    elif opcion == 3:
        resultado = multiplicacion(numero1, numero2)
        print(f"La multiplicación es: {resultado}")
    elif opcion == 4:
        resultado = division(numero1, numero2)
        if resultado is not None:
            print(f"La división es: {resultado}")
    elif opcion == 5:
        print("Saliendo del programa...")
        break





