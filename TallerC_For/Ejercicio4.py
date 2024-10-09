# 4. Escribe un programa lea una lista de números e imprima la suma de los números pares.

numeros = [1,2,3,8,10,12,19]

# inicializa suma de numeros pares
suma_pares = 0
for numero in numeros:
    if numero % 2==0: # verifica si el numero es par
        suma_pares += numero # suma el numero si es par

# resultado
print(f"la suma de los numero pares es : {suma_pares}")




