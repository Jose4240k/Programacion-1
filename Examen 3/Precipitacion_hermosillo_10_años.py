from pathlib import Path
import matplotlib.pyplot as plt

ruta_csv = Path(__file__).with_name("precipitacion_en_10_años.csv")

with ruta_csv.open("r", encoding="utf-8") as archivo:
    encabezado = next(archivo, None) #Ignoro la primera linea
    fechas = []
    preci = []
    #Guardo los datos en listas
    for linea in archivo:
        datos = linea.strip().split(",")
        fechas.append(datos[0])
        preci.append(float(datos[1]))
#Identifico los dias con precipitacion mayor a 20mm con formato DD/MM/YYYY
dias_alta_precipitacion = [i for i, p in enumerate(preci) if p >= 20]
print(f"Días con precipitación mayor a 20mm: {len(dias_alta_precipitacion)}")
dia_con_fecha = zip(dias_alta_precipitacion, [fechas[i] for i in dias_alta_precipitacion])
print(list(dia_con_fecha))
#Grafico la precipitacion diaria
plt.figure(figsize=(12, 6))
plt.bar(fechas, preci, color='blue')
plt.title("Precipitación diaria en Hermosillo durante 10 años")
plt.ylabel("Precipitación (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
