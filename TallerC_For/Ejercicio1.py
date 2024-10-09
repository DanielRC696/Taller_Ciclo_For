""""
1. Pide al usuario que ingrese una palabra o frase y usa un ciclo for para contar cuántas vocales (a, e, i, o, u) contiene.
 Luego, muestra el conteo de cada vocal por separado.
"""
texto = input("Ingresa una palabra o frase: ")

vocales = 'aeiou'

# diccionario para contar las vocales
contador_vocales = {'a':0,'e':0,'i':0,'o':0,'u':0,}

# Ciclo for para revisar  la frase
for letra in texto.lower(): # convertir en minusculas
    if letra in vocales: # si la letra es una vocal
        contador_vocales[letra] +=1 # se aumenta el contador de la vocal

# Mostrar conteo de cada vocal
for vocal, conteo in contador_vocales.items():  # devuelve lista de tuplas con clave y valor correspondiente
    print(f" La vocal '{vocal}' aparece { conteo} veces")