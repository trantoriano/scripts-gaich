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

#Frecuencia de reproducción: ¿Qué días o meses escuchas más música?

# Convertir la columna de fecha a formato datetime
df['timestamp'] = pd.to_datetime(df['endTime'])

# Análisis por mes
df['month'] = df['timestamp'].dt.month
monthly_counts = df['month'].value_counts().sort_index()

# Análisis por día de la semana
df['day_of_week'] = df['timestamp'].dt.day_name()
daily_counts = df['day_of_week'].value_counts()

print("Escuchas por mes:")
print(monthly_counts)

print("\nEscuchas por día de la semana:")
print(daily_counts)

#Artistas más reproducidos

# Top 10 artistas más escuchados
top_artists = df["artistName"].value_counts().head(10)
print("Top 10 artistas más escuchados:")
print(top_artists)

#Hora de escucha: ¿Eres más nocturno o diurno?

# Extraer la hora de reproducción
df['hour'] = df['timestamp'].dt.hour
hourly_counts = df['hour'].value_counts().sort_index()

print("Frecuencia de escucha por hora:")
print(hourly_counts)

#Canciones repetidas: ¿Escuchas las mismas en loop?

repeat_songs = df["trackName"].value_counts().head(10)
print("Top 10 canciones más repetidas:")
print(repeat_songs)

#Descubrimiento de música nueva

# Ordenamos por fecha de reproducción y verificamos nuevas canciones
df_sorted = df.sort_values("timestamp")
df_sorted["new_song"] = df_sorted["trackName"].duplicated(keep="first").apply(lambda x: "Nueva" if not x else "Repetida")

print(df_sorted[["timestamp", "trackName", "new_song"]].head(20))
