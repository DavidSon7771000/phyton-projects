#Cajero automático

contraseña = "phyton123"
intentos = 1
saldo = 1000

print("Bienvenido")
entrada = input("Ingrese su contraseña: ")
while entrada != contraseña and intentos < 3:
    print("Contraseña incorrecta")
    intentos += 1
    entrada = input("Ingrese su contraseña: ")
if entrada == contraseña:
    print("Bienvenido al cajero automático")
    opcion = 0
    #Menú
    while opcion != 4:
        print("\nPresiona 1 para consultar saldo")
        print("Presiona 2 para depositar dinero")
        print("Presiona 3 para retirar dinero")
        print("Presiona 4 para salir\n")

        opcion = int(input("Opción : "))
        if opcion == 1:
            print(f"saldo actual: {saldo}")
            volver = 0
            while volver != 4:
             volver = int(input("Presiona 4 para volver al menú: "))
             if volver != 4:
                print("Opción inválida, presione 4 para volver al menú")

        elif opcion == 2:
            depositar = int(input("Ingrese la cantidad a depositar: "))
            if depositar < 0:
                print("Cantidad inválida")
            else:
                saldo += depositar
                print(f"Deposito exitoso, ahora tu saldo es: {saldo}")


        elif opcion == 3:
            retirar = int(input("Ingrese la cantidad a retirar: "))
            if retirar > saldo:
                print("Fondos insuficientes")
            elif retirar < 0:
                print("Cantidad inválida")
            else:
                saldo -= retirar
                print(f"Retiro exitoso, ahora tu saldo es: {saldo}")


        elif opcion == 4:
            print("Saliendo del cajero automático")
        else: 
            print("Opción no válida. Intente nuevamente")


            


else:
    print("Acceso bloqueado")
    exit()

