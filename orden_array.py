x = [int(x) for x in input("Ingrese 10 numeros enteros separados por espacio: ").split()]
ordenada = True
creciente = True
decreciente = True

for i in range(len(x)-1):
    x.append(i)
    
    if x[i] > x[i+1]:
        creciente = False
        
    elif x[i] < x[i + 1]:
        decreciente = False
        
    break
if ordenada :
    if creciente == True and decreciente == False :
        print("El array es creciente")
        
    elif creciente == False and decreciente == True :
        print("El array es decreciente")
        
else:
    print("La serie esta desordenada")