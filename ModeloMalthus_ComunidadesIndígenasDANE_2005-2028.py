#!/usr/bin/env python
# coding: utf-8

# In[141]:


# Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lee el archivo .xlsx y selecciona la Hoja2
df = pd.read_excel("G:/Mi unidad/Octubre 2023/Ecuaciones Diferenciales/Entregables/ACA 3/visor-pueblos-indigenas-06-2021.xlsx", sheet_name="Hoja1")

# Asigna las columnas a variables
año = df["Año"]
poblacion = df["Población"]
comunidad_indigena = df["Pueblo indígena"][0]

A2 = df.iloc[0, 0] # Año 2005
A3 = df.iloc[1, 0] # Año 2018
B2 = df.iloc[0, 1] # Población en el 2005
B3 = df.iloc[1, 1] # Población en el 2018

# Calcular la tasa de crecimiento r
# Usar la fórmula P(t) = P0 * e^(r*t)
# Despejar r = (log(P(t)/P0))/t
r = (np.log(B3/B2)) / (A3 - A2)

# Predecir la población futura hasta el 2028
año_futuro = np.arange(A2, 2058)
poblacion_futura = B2 * np.exp(r * (año_futuro - A2))
año_rango = 2058

# Graficar los datos y la predicción
plt.plot(A2, B2, "o", label="Población inicial")
plt.plot(A3, B3, "o", label="Población final")
plt.plot(año_futuro, poblacion_futura, "-", label="Predicción")
plt.xlabel("Año")
plt.ylabel("Población")
plt.title(f"Proyección de crecimiento poblacional de la comunidad indígena {comunidad_indigena} (modelo Mathus)", pad = 20)
plt.legend()
plt.show()


# In[121]:


print(f"Datos de comunidad indígena: {comunidad_indigena}")

print("-------------------------------------------------------")
print(f"A2 representa el año {A2}")
print(f"A3 representa el año {A3}")
print(f"B2 representa al total de habitantes censados: {B2} en el año {A2}")
print(f"B3 representa al total de habitantes censados: {B3} en el año {A3}")
print(f"r representa la tasa de cambio de los dos años: {r}")



# In[103]:


# Representación de la población año a año hasta 2028
print(poblacion_futura)


# In[142]:


# Equivale a  P(t) = P0 * e^(r*t), donde P0 = B2, r = 0,017 y año_rango = 2058.
poblacion_futura = B2 * np.exp(r * (año_rango - 2005))
print(f"La población indígena {comunidad_indigena} en el año {año_rango} sería de {poblacion_futura:.0f} personas, según el modelo de Malthus.")


# In[ ]:


## Conclusión uno
# El modelo Malthus no considera aspecto ambientales en el comportamiento del incremento poblacional
# El gráfico del modelo Malthus muestra una curva exponencial que representa el aumento de población en el tiempo,
# la curva sees más ascendente a medida de los años transcurren.
# En este ejemplo, se modificó el año de proyección... se puede apreciar el cambio a partir del año 2058.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




