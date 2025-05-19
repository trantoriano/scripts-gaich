# Descubrimiento de música nueva: Saber cuándo agregas nuevas canciones a tu historial.
# Diversidad de escucha: ¿Repites los mismos artistas o exploras nueva música?

# Visualizaciones en Python
# Gráfica de evolución de artistas** → Cómo han cambiado tus preferencias a lo largo del tiempo.
# Tendencias de reproducción** → Análisis temporal de escucha por mes y hora del día.
# Gráfica de canciones nuevas vs repetidas** → Cuánto tiempo exploras música nueva vs. cuánto repites canciones.

#Código generado con Copilot

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lista de archivos JSON
files = [
    "StreamingHistory_music_0.json",
    "StreamingHistory_music_1.json",
    "StreamingHistory_music_2.json",
]

# Cargar y combinar los datos
df_list = [pd.read_json(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

# Mostrar información general del dataset
print(df.info())
print(df.head())

# Frecuencia de reproducción: ¿Qué días o meses escuchas más música?

# Convertir la columna de fecha a formato datetime
df["timestamp"] = pd.to_datetime(df["endTime"])

# Análisis por mes
df["month"] = df["timestamp"].dt.month
monthly_counts = df["month"].value_counts().sort_index()

# Análisis por día de la semana
df["day_of_week"] = df["timestamp"].dt.day_name()
daily_counts = df["day_of_week"].value_counts()

# Extraer la hora de reproducción
df["hour"] = df["timestamp"].dt.hour

# 1. Análisis de patrones de escucha

print("Escuchas por mes:")
print(monthly_counts)

print("\nEscuchas por día de la semana:")
print(daily_counts)

# Artistas más reproducidos

# Top 10 artistas más escuchados
top_artists = df["artistName"].value_counts().head(10)
print("Top 10 artistas más escuchados:")
print(top_artists)

# Hora de escucha: ¿Eres más nocturno o diurno?

hourly_counts = df["hour"].value_counts().sort_index()

print("Frecuencia de escucha por hora:")
print(hourly_counts)

# Canciones repetidas: ¿Escuchas las mismas en loop?
repeat_songs = df["trackName"].value_counts().head(10)
print("Top 10 canciones más repetidas:")
print(repeat_songs)

# Descubrimiento de música nueva

# Ordenamos por fecha de reproducción y verificamos nuevas canciones
df_sorted = df.sort_values("timestamp")
df_sorted["new_song"] = (
    df_sorted["trackName"]
    .duplicated(keep="first")
    .apply(lambda x: "Nueva" if not x else "Repetida")
)

print(df_sorted[["timestamp", "trackName", "new_song"]].head(20))

### Tendencias de escucha ###

# Conteo de reproducciones por mes
monthly_counts = df["month"].value_counts().sort_index()
print("Reproducciones por mes:\n", monthly_counts)

# Conteo por día de la semana
daily_counts = df["day_of_week"].value_counts()
print("Reproducciones por día de la semana:\n", daily_counts)

# Tiempo total de reproducción por artista
artist_playtime = (
    df.groupby("artistName")["msPlayed"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("Tiempo total de reproducción por artista:\n", artist_playtime)

# 2. Análisis de repetición y descubrimiento

df_sorted = df.sort_values("timestamp")
df_sorted["new_song"] = (
    df_sorted["trackName"]
    .duplicated(keep="first")
    .apply(lambda x: "Nueva" if not x else "Repetida")
)

# Conteo de canciones nuevas vs repetidas
new_vs_repeated = df_sorted["new_song"].value_counts()
print("Canciones nuevas vs repetidas:\n", new_vs_repeated)

# 3. Tendencia de escucha a lo largo del año

# Agrupar por mes
monthly_counts = df.groupby(df["timestamp"].dt.to_period("M")).size()

# Agrupar por horas
hourly_counts = df.groupby(df["timestamp"].dt.hour).size()

# Agrupar por mes y artista
artist_trends = (
    df.groupby([df["timestamp"].dt.to_period("M"), "artistName"])
    .size()
    .unstack()
    .fillna(0)
)

# Seleccionar los 5 artistas más reproducidos
top_artists = df["artistName"].value_counts().head(5).index
artist_trends = artist_trends[top_artists]

monthly_playtime = df.groupby(df["timestamp"].dt.to_period("M"))[
    "msPlayed"
].sum()

# Agrupar por mes y calcular el número de reproducciones
monthly_counts = df.groupby(df["timestamp"].dt.to_period("M")).size()

# Calcular la variabilidad de escucha
variability = np.std(monthly_counts) / np.mean(monthly_counts) * 100
print(f"Variabilidad de escucha: {variability:.2f}%")

artist_avg_playtime = (
    df.groupby("artistName")["msPlayed"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
print("Duración promedio de reproducción por artista:\n", artist_avg_playtime)

# ¿Cuánto tiempo escuchas cada artista en promedio?

artist_avg_playtime = (
    df.groupby("artistName")["msPlayed"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
print("Duración promedio de reproducción por artista:\n", artist_avg_playtime)

# ¿Cuánto tiempo pasas en una misma canción antes de cambiarla?
# Definir un umbral de reproducción "completa" (por ejemplo, si dura más de 90% de la canción)
song_full_played_threshold = df[
    "msPlayed"
].median()  # Se asume que el tiempo medio es referencia

df["fully_listened"] = df["msPlayed"] >= song_full_played_threshold
song_completion_stats = df["fully_listened"].value_counts()

print(
    "Canciones escuchadas completamente vs cambiadas a mitad:\n",
    song_completion_stats,
)

############ Gráficas ############

# Gráfica de días de la semana
plt.figure(figsize=(10, 5))
daily_counts.plot(kind="bar", color="skyblue")
plt.title("Frecuencia de escucha por día de la semana")
plt.xlabel("Día")
plt.ylabel("Número de reproducciones")
plt.show()

# Gráfica de horas del día
plt.figure(figsize=(10, 5))
hourly_counts.plot(kind="bar", color="lightcoral")
plt.title("Frecuencia de escucha por hora del día")
plt.xlabel("Hora")
plt.ylabel("Número de reproducciones")
plt.show()

# Gráfica de tiempo de reproducción por artista
artist_playtime.plot(kind="bar", figsize=(10, 5), color="purple")
plt.title("Tiempo de reproducción por artista (en ms)")
plt.xlabel("Artista")
plt.ylabel("Tiempo total de reproducción")
plt.show()

# Gráfica´ de canciones más repetidas
repeat_songs.plot(kind="bar", figsize=(10, 5), color="green")
plt.title("Canciones más repetidas")
plt.xlabel("Canción")
plt.ylabel("Número de reproducciones")
plt.show()

# Gráfica´ de música nueva
new_vs_repeated.plot(
    kind="pie", autopct="%1.1f%%", colors=["blue", "orange"], figsize=(7, 7)
)
plt.title("Porcentaje de canciones nuevas vs repetidas")
plt.show()

# Graficar Tendencia de escucha a lo largo del año
plt.figure(figsize=(12, 5))
monthly_counts.plot(kind="line", marker="o", color="royalblue")
plt.title("Tendencia de reproducción por mes")
plt.xlabel("Mes")
plt.ylabel("Número de reproducciones")
plt.grid(True)
plt.show()

# Graficar Horas con más reproducciones
plt.figure(figsize=(10, 5))
hourly_counts.plot(kind="line", marker="o", color="darkorange")
plt.title("Frecuencia de escucha por hora del día")
plt.xlabel("Hora")
plt.ylabel("Número de reproducciones")
plt.grid(True)
plt.show()

# Graficar la evolución de los artistas más escuchados
plt.figure(figsize=(12, 6))
artist_trends.plot(marker="o")
plt.title("Evolución de reproducción de los 5 artistas más escuchados")
plt.xlabel("Mes")
plt.ylabel("Número de reproducciones")
# plt.legend(title="Artista")
plt.grid(True)
plt.show()


# Graficar variación en duración de reproducción
plt.figure(figsize=(12, 5))
monthly_playtime.plot(kind="line", marker="o", color="purple")
plt.title("Tendencia de tiempo de reproducción por mes")
plt.xlabel("Mes")
plt.ylabel("Milisegundos reproducidos")
plt.grid(True)
plt.show()

# ¿Cuánto tiempo escuchas cada artista en promedio?
artist_avg_playtime.plot(kind="bar", figsize=(12, 5), color="crimson")
plt.title("Duración promedio de escucha por artista")
plt.xlabel("Artista")
plt.ylabel("Milisegundos por reproducción")
plt.show()

# Gráfica canciones escuchadas completamente
song_completion_stats.plot(
    kind="pie", autopct="%1.1f%%", figsize=(7, 7), colors=["green", "red"]
)
plt.title("Porcentaje de canciones reproducidas completamente vs cambiadas")
plt.show()


# ¿Cuándo agregas más canciones nuevas a tu historial?

df["new_song"] = (
    df["trackName"]
    .duplicated(keep="first")
    .apply(lambda x: "Nueva" if not x else "Repetida")
)
new_song_counts = (
    df.groupby(df["timestamp"].dt.to_period("M"))["new_song"]
    .value_counts()
    .unstack()
)

# Graficar la evolución de descubrimiento musical
plt.figure(figsize=(12, 6))
new_song_counts["Nueva"].plot(kind="line", marker="o", color="blue")
plt.title("Evolución de descubrimiento de música nueva")
plt.xlabel("Mes")
plt.ylabel("Número de canciones nuevas escuchadas")
plt.grid(True)
plt.show()

# ¿Qué tan variado es tu historial de artistas?

unique_artists_per_month = df.groupby(df["timestamp"].dt.to_period("M"))[
    "artistName"
].nunique()

plt.figure(figsize=(12, 5))
unique_artists_per_month.plot(kind="line", marker="o", color="darkgreen")
plt.title("Cantidad de artistas diferentes escuchados por mes")
plt.xlabel("Mes")
plt.ylabel("Número de artistas únicos")
plt.grid(True)
plt.show()