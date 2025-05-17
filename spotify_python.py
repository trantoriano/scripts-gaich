# Análisis Exploratorio
# Frecuencia de reproducción: Número de reproducciones por mes, día de la semana y hora del día.  
# Top artistas y canciones: Los más escuchados y los que más tiempo han ocupado en tu historial.  
# Distribución de escucha: ¿Eres más nocturno o diurno?  

# Validación de hábitos musicales
# Canciones más repetidas: Identificar cuáles tienes en loop constantemente.  
# Descubrimiento de música nueva: Saber cuándo agregas nuevas canciones a tu historial.  
# Diversidad de escucha: ¿Repites los mismos artistas o exploras nueva música?  

# Visualizaciones en Python
# Gráfica de evolución de artistas** → Cómo han cambiado tus preferencias a lo largo del tiempo.  
# Tendencias de reproducción** → Análisis temporal de escucha por mes y hora del día.  
# Gráfica de canciones nuevas vs repetidas** → Cuánto tiempo exploras música nueva vs. cuánto repites canciones.  

import pandas as pd
import matplotlib.pyplot as plt

# Lista de archivos JSON
files = ["StreamingHistory_music_0.json", "StreamingHistory_music_1.json", "StreamingHistory_music_2.json"]

# Cargar y combinar los datos
df_list = [pd.read_json(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

# Mostrar información general del dataset
print(df.info())
print(df.head())

