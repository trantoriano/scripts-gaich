import pandas as pd
import matplotlib.pyplot as plt

# Lista de archivos JSON
files = ["StreamingHistory_music_0.json", "StreamingHistory_music_1.json", "StreamingHistory_music_2.json"]

# Cargar y combinar los datos
df_list = [pd.read_json(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

# Revisar las primeras filas para verificar que la columna exista
print(df.head())  # Esto nos ayuda a confirmar que 'timestamp' está en los datos

df['endTime'] = pd.to_datetime(df['endTime'])
df['day_of_week'] = df['endTime'].dt.day_name()
df['hour'] = df['endTime'].dt.hour  # Extraer la hora

# Agrupar por día de la semana
daily_counts = df['day_of_week'].value_counts()

# Agrupar por hora del día
hourly_counts = df['hour'].value_counts().sort_index()

# Gráfica de días de la semana
plt.figure(figsize=(10,5))
daily_counts.plot(kind='bar', color='skyblue')
plt.title("Frecuencia de escucha por día de la semana")
plt.xlabel("Día")
plt.ylabel("Número de reproducciones")
plt.show()

# Gráfica de horas del día
plt.figure(figsize=(10,5))
hourly_counts.plot(kind='bar', color='lightcoral')
plt.title("Frecuencia de escucha por hora del día")
plt.xlabel("Hora")
plt.ylabel("Número de reproducciones")
plt.show()






