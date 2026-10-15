def main():
    nombre = ""
    instagram = 0.0
    tiktok = 0.0
    netflix = 0.0
    snapchat = 0.0
    whatsapp = 0.0
    suma = 0.0
    porcentajeDia = 0.0
    limiteHorasDiarias = 5.0 
    print("==================================================")
    print("Bienvenido a la calculadora de horas digitales.")
    print("==================================================")
    print()

    print("¿Cuál es tu nombre?")
    nombre = input()
    
    print("¿Cuántas horas diarias le dedicas a instagram?")
    instagram = float(input())
    
    print("¿Cuántas horas diarias le dedicas a tiktok?")
    tiktok = float(input())
    
    print("¿Cuántas horas diarias le dedicas a netflix?")
    netflix = float(input())
    
    print("¿Cuántas horas diarias le dedicas a snapchat?")
    snapchat = float(input())
    
    print("¿Cuántas horas diarias le dedicas a whatsapp?")
    whatsapp = float(input())
    
    suma = instagram + tiktok + netflix + snapchat + whatsapp
    porcentajeDia = (suma / 24) * 100
    
    print(f"Hola {nombre}, pasas en total {suma} horas, lo que es {porcentajeDia:.2f}% de tu día.")
    
    if suma > limiteHorasDiarias:
        print(f"¡{nombre}! Pasas demasiadas horas de tu día en plataformas digitales.")
    elif suma < limiteHorasDiarias:
        print("Estas dentro de un rango saludable.")

main()