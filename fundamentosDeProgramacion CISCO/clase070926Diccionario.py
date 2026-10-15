mi_lista = ["manzana", "banana", "naranja"]
mi_tupla = (10, 20, 30)
mi_diccionario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
# Matriz de 3x3
mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



#Crear un diccionario
persona = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Chihuahua',
    'trabajo': 'Programador'
}


#Crear un diccionario versión 2
diccionario = dict([
    ('nombre', 'Pedro'),
    ('edad', 33),
    ('ciudad', 'Mexico'),
    ('trabajo', 'Ingeniero')
])

print(persona)
print(diccionario)


for x, y in persona.items():
    print(x,":", y)

for x, y in diccionario.items():
    print(x,":", y)





dic = {'a': 1, 'b': 2, 'c': 3}
dic.popitem()
print(dic)


dic1 = {'a': 1, 'b': 2, 'c': 3}