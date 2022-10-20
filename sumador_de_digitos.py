import re

def sumar_digito(numero):
    numero = re.sub("[.-]","", numero )
    if numero.isnumeric():
        sumador = 0
        if int(numero) > 0:
            for n in numero :
                sumador += int(n)
            print ("La suma de sus digitos es: ", sumador )
        else:
            print(" Ingresa un numero correcto")

numero = -1
while(numero != "0"):
    numero = input("Ingresar otro numero: ") 