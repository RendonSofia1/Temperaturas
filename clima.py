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

# Mostrar resultados
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Desviación Estándar: {desviacion_estandar}")

# Crear un gráfico con los días en el eje x
dias = df['Dia']
plt.figure(figsize=(10, 6))
plt.plot(dias, temp)
plt.xlabel('Día')
plt.ylabel('Temperatura')
plt.title('Gráfico de Temperaturas en la semana')
plt.xticks(rotation=45)  # Para rotar las etiquetas del eje x
plt.grid(True)
plt.tight_layout()
plt.show()
