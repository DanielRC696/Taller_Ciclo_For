# 3. Escribe un programa que lea una lista de palabras e imprima la lista de palabras que comiencen con una determinada letra

# lista vacia
palabras = []

# Ingresar la lista de Nombres
while True:
    palabra = input("Ingrese una palabra (o escriba 'salir' para terminar): ")
    if palabra.lower() == 'salir': # condicion de salida
        break
    palabras.append(palabra) # agrega el nombre a la lista

# ordenar  lista de palabras
palabras.sort()

# Ingresar la letra por la cual desea filtrar
letra = input("Ingrese la letra por la cual desea filtrar las palabras: " ).lower()

# imprimir lista filtrada por letra
print(f"\nPalabras que comienzan con la letra '{letra.upper()}':")
for palabra in palabras:
    if palabra.lower().startswith(letra): # verifica si el nombre comienza con la letra
     print(palabra)