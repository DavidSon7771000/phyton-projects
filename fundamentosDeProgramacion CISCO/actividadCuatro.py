# Uso de tuplas
def suma_total(x):
    return sum(x)

numeros = (2, 3, 4, 5, 6)
print(f"Tercer elemento: {numeros[2]}")

digito_1 = int(input("Ingrese un número: "))
digito_2 = int(input("Ingrese otro número: "))
numeros += (digito_1, digito_2)

lista_numeros = list(numeros)
lista_numeros.sort()
print(f"Lista ordenada: {lista_numeros}")

print(f"La suma de todos los elementos es {suma_total(numeros)}")

# Uso de diccionarios

# Crea un diccionario llamado "contactos" con, al menos, tres entradas, donde las claves sean los nombres de las personas y los valores correspondan a sus números de teléfono.
# Por medio de una captura, agrega un nuevo contacto al diccionario.
# Itera sobre las claves del diccionario e imprime en pantalla los nombres de los contactos.
# Crea una función que reciba el diccionario de contactos y un nombre como parámetro para que, posteriormente, retorne el número de teléfono correspondiente al contacto ingresado.
# Aplica la función creada en el paso anterior para buscar el número de teléfono de uno de los contactos y muestra el resultado.
print("\n\n--------------------------------------------------------------------------------")


contactos= {
    'David': 9933973970,
    'Ian': 9212737815,
    'Eduardo': 9931105680
    
}

print("Ingrese un nuevo contacto")
nombre = input("Nombre: ")
numero = input("Numero: ")
contactos[nombre] = numero
print(contactos)


print("\nLista de nombres de contactos:")
for clave in contactos:
    print(clave)

def buscarNumero(contactos, nombre):
    return contactos.get(nombre, "No existe el contacto")

nombreBuscado = input("Ingrese el nombre del contacto a buscar: ")
numeroBuscado = buscarNumero(contactos, nombreBuscado)
print(f"El numero de teléfono del contacto {nombreBuscado} es {numeroBuscado}")


#Uso de excepciones

#    Crea un programa que solicite al usuario que ingrese dos números enteros.
#    Utiliza un bloque try-except para manejar la excepción que ocurrirá si el usuario ingresa un valor no numérico.
#    Si el usuario ingresa valores no numéricos, muestra un mensaje de error; en cambio, si los valores son numéricos, muestra la suma de los dos números ingresados.
#    Agrega una excepción personalizada para manejar la división entre cero; por tanto, en caso de que el segundo número ingresado sea cero, muestra un mensaje de error adecuado.
print("\n\n--------------------------------------------------------------------------------")

class DivisionPorCeroError(Exception):
    """Excepción personalizada para la división entre cero."""
    pass

print("Ingrese dos números enteros")
try:
    numero1 = int(input("Primer número: "))
    numero2 = int(input("Segundo número: "))

    if numero2 == 0:
        raise DivisionPorCeroError("Error: El segundo número no puede ser cero.")
    
   
    suma = numero1 + numero2
    print(f"La suma de los dos números es: {suma}")

except ValueError:
    print("Error: Los valores ingresados deben ser numéricos enteros.")
except DivisionPorCeroError as e:
    print(e)






# Uso de strings

# Crea una variable llamada "mensaje" que contenga un texto de tu elección.
# Imprime en pantalla la longitud del mensaje.
# Utiliza un método de strings para convertir todo el texto del mensaje a mayúsculas.
# Utiliza otro método de strings para reemplazar una palabra específica en el mensaje por otra de tu elección.
# Crea una función que reciba un string como parámetro y retorne la cantidad de palabras que contiene.
# Aplica la función creada en el paso anterior al mensaje y muestra el resultado.
print("\n\n--------------------------------------------------------------------------------")


mensaje = "Hola, bonita tarde"
print(len(mensaje))
print(mensaje.upper())
nuevaMensaje = mensaje.replace("tarde", "noche")
print(nuevaMensaje)
def cantidadDePalabras(mensaje):
    return len(mensaje.split())
print(cantidadDePalabras(mensaje))





#Menú principal

# Crea un menú principal que permita elegir qué tipo de dato se desea capturar.
# De acuerdo con la elección hecha por el usuario, llama a la función indicada para proceder a su ejecución.
# Agrega una opción para finalizar la ejecución.
print("\n\n--------------------------------------------------------------------------------")


