numeros = []
positivos = []
negativos =[]
contador_ceros = 0

#Leer 5 numeros por teclado y guaradrlo en un array.
for i in range(5):
    numero = int(input("Introduce un numero: "))
    numeros.append(numero)
    
# Calcularnla media de los numeros positivos, la media de los numeros negativos y el conteo de los ceros.
for numero in numeros:
    if numero > 0:
        positivos.append(numero)
    elif numero < 0:
        negativos.append(numero)
    else:
        contador_ceros += 1
        
media_positivos = sum(positivos) / len(positivos) if len(positivos) > 0 else 0
media_negativos = sum(negativos) / len(negativos) if len(negativos) > 0 else 0


print("La medica de los numeros positivos es ",  media_positivos)
print("La media de los numeros negativos es ", media_negativos)
print("El conteo de los cero es", contador_ceros)