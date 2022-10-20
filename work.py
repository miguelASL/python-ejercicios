import numpy as np
import pandas as pd
from datetime import date, time, datetime
import matplotlib.pyplot as plt
import seaborn as sbr

datos = pd.read_csv("datos.csv", header=0)

dias_consecutivos = 0
dias_max_consecutivos = 0
dias_max_consecutivos_index = 0
for index,line in datos.iterrows():
    if line['Open'] < line['Close']:
        dias_consecutivos += 1
    else:
        if dias_consecutivos > dias_max_consecutivos:
            dias_max_consecutivos = dias_consecutivos
            dias_max_consecutivos_index = index - dias_consecutivos    
        dias_consecutivos = 0

print(datos)
print(dias_max_consecutivos_index)
print(datos.iloc[dias_max_consecutivos_index:dias_max_consecutivos_index + dias_max_consecutivos,:])