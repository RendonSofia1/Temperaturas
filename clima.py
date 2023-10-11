import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo XLS
file_path = "C:/Users/rendo/Documents/proyectosING/Clima/temperatura.xls" 
df = pd.read_excel(file_path)

#print(df.columns); #ver columnas

# Calcular estadísticas
temp = df['Temperatura']
media = np.mean(temp)
mediana = np.median(temp)
maximo = np.max(temp)
minimo = np.min(temp)
desviacion_estandar = np.std(temp)

# print(f"Media: {media}")
# print(f"Mediana: {mediana}")
# print(f"Máximo: {maximo}")
#print(f"Mínimo: {minimo}")
#print(f"Desviación Estándar: {desviacion_estandar}")


# Crear un gráfico
dias = df['Dia']
plt.figure(figsize=(10, 6))
plt.plot(dias, temp, label='Temperatura')
plt.axhline(media, color='r', linestyle='--', label='Media')
plt.axhline(mediana, color='y', linestyle='--', label='Mediana')
plt.scatter(dias[temp.idxmax()], maximo, color='g', marker='o', label='Máximo')
plt.scatter(dias[temp.idxmin()], minimo, color='b', marker='o', label='Mínimo')
plt.fill_between(dias, media - desviacion_estandar, media + desviacion_estandar, color='y', alpha=0.3, label='Desviación Estándar')
plt.xlabel('Día')
plt.ylabel('Temperatura')
plt.title('Gráfico de Temperaturas por Día')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()