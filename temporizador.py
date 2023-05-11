import time 

def temportizador(segundos):
    for s in range(segundos, 0, -1):
        print(f"Faltan {s} segundos")
        time.sleep(1)
    print("¡¡¡ Tiempo agotado !!!")
    
temportizador(5)