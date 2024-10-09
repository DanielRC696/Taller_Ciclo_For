# 2. Escribe un programa que lea una lista de nombres e imprima la lista en orden alfabético.

# lista vacia
nombres = []

# Ingresar la lista de Nombres
while True:
    nombre = input("Ingrese un nombre (o escriba 'salir' para terminar): ")
    if nombre.lower() == 'salir': # condicion de salida
        break
    nombres.append(nombre) # agrega el nombre a la lista

# ordenar  lista alfabeticamente
nombres.sort()

print(" Lista de nombres en orden alfabetico")
for nombre in nombres:
    print(nombre)






