#!/usr/bin/env python
# coding: utf-8

# In[1]:

## Aplicación de modelo Malthus en diversas poblaciones indígenas
## en Colombia 2005 y 2018 con proyecciones a años posteriores:
# 1. Se toma la base de datos subida a la página del DANE:
#    https://www.dane.gov.co/index.php/estadisticas-por-tema/enfoque-diferencial-e-interseccional/autorreconocimiento-etnico
# 2. Se decarga el documento en Excel en formato .xlsx llamado visor-pueblos-indígenas-06-2021.xlsx
# 3. Se crea una hoja nueva (Hoja1) para replicar los valores de las celdas que detallan el total
#    de la población en los años 2055 y 2018 y una celda que replique el dato de la comunidad indígena
#    que se analiza para el modelo.


# Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lee el archivo .xlsx y selecciona la Hoja1 para la captura de datos
df = pd.read_excel("G:/Mi unidad/Octubre 2023/Ecuaciones Diferenciales/Entregables/ACA 3/visor-pueblos-indigenas-06-2021.xlsx", sheet_name="Hoja1")

# Asigna las columnas a variables parametrizadas en la hoja de cálculo en la pestaña Hoja1
año = df["Año"]
poblacion = df["Población"]
comunidad_indigena = df["Pueblo indígena"][0]

## Captura de datos de las celdas 
# Se presentan los valores de las filas y columnas en la hoja de cálculo en la pestaña Hoja1
A2 = df.iloc[0, 0] # Año 2005
A3 = df.iloc[1, 0] # Año 2018
B2 = df.iloc[0, 1] # Población en el 2005
B3 = df.iloc[1, 1] # Población en el 2018

## Calcula la tasa de crecimiento r
# Usa la fórmula P(t) = P0 * e^(r*t) y
# se despeja r = (log(P(t)/P0))/t
r = (np.log(B3/B2)) / (A3 - A2)

## Predicción la población futura hasta el 2058 en este ejemplo de la ejecución.
# El valor del año se puede modificar para ver el comportamiento en la gráfica: año_futuro = np.arange(A2, AÑO DESEADO + 1).
año_futuro = np.arange(A2, 2059) 
poblacion_futura = B2 * np.exp(r * (año_futuro - A2))
año_rango = 2058

## Gráfica los datos y la predicción
# Se establecen los ejes «x» y «y»
plt.plot(A2, B2, "o", label="Población inicial")
plt.plot(A3, B3, "o", label="Población final")
plt.plot(año_futuro, poblacion_futura, "-", label="Predicción")
plt.xlabel("Año")
plt.ylabel("Población")
plt.title(f"Proyección de crecimiento poblacional de la comunidad indígena {comunidad_indigena} (modelo Mathus)", pad = 20)
plt.legend()
plt.show()


# In[2]:


print(f"Datos de comunidad indígena: {comunidad_indigena}")

print("-------------------------------------------------------")
print(f"A2 representa el año {A2}")
print(f"A3 representa el año {A3}")
print(f"B2 representa al total de habitantes censados: {B2} en el año {A2}")
print(f"B3 representa al total de habitantes censados: {B3} en el año {A3}")
print(f"r representa la tasa de cambio de los dos años: {r}")



# In[3]:


# Representación de la población año a año hasta 2028
print(poblacion_futura)


# In[4]:


# Equivale a  P(t) = P0 * e^(r*t), donde P0 = B2, r = 0,017 y año_rango = 2058.
poblacion_futura = B2 * np.exp(r * (año_rango - 2005))
print(f"La población indígena {comunidad_indigena} en el año {año_rango} sería de {poblacion_futura:.0f} personas, según el modelo de Malthus.")


# In[5]:


## Conclusión uno:
# El modelo Malthus no considera aspecto ambientales en el comportamiento del incremento poblacional.
# El gráfico del modelo Malthus muestra una curva exponencial que representa el aumento de población en el tiempo,
# La curva es más ascendente a medida de los años transcurren.
# En este ejemplo, se modificó el año de proyección... se puede apreciar el cambio a partir del año 2058.


# In[6]:

## Conclusión dos:
# Para estimar la llegada a una catástrofe de Malthus, se debe incorporar un segundo grupo de datos que estimen recursos;
# Los recursos pueden ser de disponibilidad de alimentos y demás bienes de consumo.
# El modelo Malthus es útil para el crecimiento poblacional de comunidades indígenas cuando se puede estimar con precisión...
# ... que dicho grupo indígena está bajo la entidad territorial de resguardo y se contrasta con recursos alimenticios.
# En el ejemplo de una comunidad indígena que tenga una tasa de natalidad y de mortalidad media en contraste con los recursos disponibles,
# conllevaría a una catástrofe de Malthus si el Estado interviene en la comunidad en cuanto a asistencia médica en partos y educación de natalidad.
# Está estimacipón obtenida con el modelo Malthus delimitaría los alcances del asistencialismo en el resguardo.



