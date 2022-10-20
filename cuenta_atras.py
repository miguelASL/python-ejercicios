n = int(input("ingresa un numero: "))
lista = []
for c in range(n):
    x = int(input("ingresa x: "))
    lista.append(x)
print(lista)
menor = 9999
if numero in lista:
    if numero < menor:
        menor = numero 
        print(" el numero es: ", menor)