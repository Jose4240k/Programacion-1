# PROGRAMACION1
# Ejercicio del Examen3
# 17 de noviembre del 2026

from profiling.tracing import label

import matplotlib.pyplot as plt
import numpy as np
from datetime import date, timedelta
import matplotlib.dates as mdates
from dateutil.relativedelta import relativedelta
from pathlib import Path
#-------------------------------------------------------
def cargar_datos_btc(nombre_archivo: str) -> tuple[list[str], np.ndarray, np.ndarray, np.ndarray]:
    """Lee el archivo CSV de Bitcoin y separa fechas, precios de apertura, cierre y volumen.

    Args:
        nombre_archivo (str): Ruta del archivo CSV de entrada.

    Returns:
        tuple: Una tupla (fechas, apertura, cierre, volumen) donde 'fechas' es una lista
            de cadenas y 'apertura', 'cierre' y 'volumen' son arreglos 1D de NumPy (float).
    """
    ruta_archivo = Path(nombre_archivo)
    if not ruta_archivo.is_absolute():
        ruta_archivo = Path(__file__).resolve().parent / ruta_archivo

    fechas = []
    lista_apertura = []
    lista_cierre = []
    lista_volumen = []
    try:
        with ruta_archivo.open("r", encoding="utf-8") as archivo:
            encabezado = next(archivo, None)  # Omitir la primera línea
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    partes = linea.split(",")
                    fechas.append(partes[0])
                    lista_apertura.append(float(partes[1]))
                    lista_cierre.append(float(partes[2]))
                    lista_volumen.append(float(partes[3]))
    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"No se encontró el archivo '{ruta_archivo}'. "
            "Verifica que el CSV exista junto a bitcoin.py."
        ) from error
    
    return fechas, np.array(lista_apertura), np.array(lista_cierre), np.array(lista_volumen)
#-------------------------------------------------------
def graficar_precio_cierre( fechas: list[str], cierre: np.ndarray) -> None:
    """Genera una gráfica histórica del precio de Bitcoin al cierre.

    Args:
        fechas (list[str]): Lista de fechas en formato 'AAAA-MM-DD'.
        cierre (np.ndarray): Arreglo 1D con los precios de cierre en USD.
    """
    eje_x = np.arange(len(cierre))

    plt.figure(num="Bitcoin: precio de cierre", figsize=(13, 6))

    # Curva de precios al cierre
    plt.plot(eje_x, cierre, color="blue", linewidth=1.2, label="Precio de Cierre (USD)")   

    # Configurar etiquetas del eje X mostrando años
    paso_ticks = max(1, len(fechas) // 12)
    posiciones_ticks = eje_x[::paso_ticks]
    etiquetas_ticks = [fechas[i][:7] for i in posiciones_ticks]  # Formato AAAA-MM
    plt.xticks(posiciones_ticks, etiquetas_ticks, rotation=45)

    plt.title(f"Precio de cierre de Bitcoin (USD) desde el 17 de septiembre de 2014", fontsize=14, fontweight="bold")
    plt.xlabel("Fecha (Año-Mes)", fontsize=11)
    plt.ylabel("Precio en USD ($)", fontsize=11)
    plt.grid(True, linestyle=":", alpha=0.5)
    plt.legend(loc="upper left")
    plt.tight_layout()
    #plt.show()
#-------------------------------------------------------
#TODO Modificar la siguiente funcion para que muestre la gráfica del valor promedio del precio del bitcoin,
#     en lugar de mostrar el valor del cierre y de la apertura en los últimos tres meses
def graficar_estadisticas_ultimo_periodo(fechas, apertura, cierre):
    if len(fechas) == 0:
        print("No hay datos para graficar.")
        return
    else:
        promedio = (apertura + cierre) / 2        
    fechas_convertidas = [date.fromisoformat(fecha) for fecha in fechas]
    fecha_fin = max(fechas_convertidas)
    fecha_inicio = fecha_fin - relativedelta(months=3) # <--- marca el inicio para abarcar los últimos tres meses

    fechas_periodo_seleccionado = []
    apertura_periodo_seleccionado = []
    cierre_periodo_seleccionado = []

    for fecha, precio_apertura, precio_cierre in zip(
        fechas_convertidas, apertura, cierre):

        if fecha_inicio <= fecha <= fecha_fin:
            fechas_periodo_seleccionado.append(fecha)
            apertura_periodo_seleccionado.append(precio_apertura)
            cierre_periodo_seleccionado.append(precio_cierre)
    
    fig = plt.figure(num="Bitcoin: últimos tres meses",figsize=(13, 6))
    #Curva del promedio del precio del bitcoin
    plt.plot(fechas_periodo_seleccionado, promedio[-len(fechas_periodo_seleccionado):], color="tab:green", label="Promedio")

    eje = plt.gca()
    eje.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    eje.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
    eje.set_xlim(fecha_inicio, fecha_fin)

    eje.grid(False, which="both")
    eje.grid(True, which="major", axis="x", linestyle=":")

    plt.xticks(rotation=60, ha="right", fontsize=8)
    plt.title(f"Precio de Bitcoin del {fecha_inicio:%d/%m/%Y} al {fecha_fin:%d/%m/%Y}")
    plt.xlabel("Fecha")
    plt.ylabel("Precio (USD)")
    
    plt.legend()
    plt.tight_layout()
    plt.show()
#-------------------------------------------------------
# --- BLOQUE PRINCIPAL DE EJECUCIÓN ---
#-------------------------------------------------------
if __name__ == "__main__":    
    fechas, apertura, cierre, volumen = cargar_datos_btc("bitcoin_historico.csv")
    graficar_precio_cierre(fechas, cierre)   
    graficar_estadisticas_ultimo_periodo(fechas,apertura, cierre)
    
    print(f"Este programa imprime algunas estadístcas sobre el precio del BITCOIN desde el {fechas[0]}")
    
    #imprimir en pantalla el día que se obtuvo el máximo histórico del precio del bitcoin al cierre y el monto
    cierre_maximo = np.max(cierre)
    indice_maximo = np.argmax(cierre)
    fecha_maximo = fechas[indice_maximo]
    print(f"Fecha del precio máximo al cierre:   {fecha_maximo} | Precio máximo: ${cierre_maximo:10,.2f}")
    
    #TODO imprimir en pantalla el día que se obtuvo el máximo histórico del precio de apertura del bitcoin y el monto
    maxima_apertura = np.max(apertura)
    print(f"Fecha del precio maximo a la apertura: {fechas[np.argmax(apertura)]} con un monto de ${maxima_apertura:10,.2f}\n")



    #ENDTODO

    #la variacion en el precio del bitcoin se calcula con la siguiente instrucción, en puntos porcentuales
    variacion = (cierre - apertura) / apertura * 100  

    # identificando los días en los que hubo una caída drástica del precio del bitcoin
    # cuando la variacion es menor al -15%, hubo una caída en el precio mayor al 15%
    dias_caida_drastica = np.where(variacion <= -15)[0]
    if len(dias_caida_drastica) > 0:
        print("Días en los que hubo una caída drástica del precio del bitcoin:")
        for dia in dias_caida_drastica:
          print(f"Fecha: {fechas[dia]} | Precio de apertura: ${apertura[dia]:10,.2f} | Precio de cierre: ${cierre[dia]:10,.2f} | Variación porcentual: {variacion[dia]:10,.2f}%") 

    #TODO: IDENTIFICAR LOS DÍAS EN LOS QUE HUBO UNA SUBIDA DRÁSTICA EN EL PRECIO DEL BITCOIN (MAYOR AL 10%)
    dia_de_subida_drastica = np.where(variacion >= 10)[0]
    if len(dia_de_subida_drastica) > 0:
        print("Días en los que hubo una subida drástica del precio del bitcoin:")
        for dia in dia_de_subida_drastica:
            print(f"Fecha: {fechas[dia]} | Precio de apertura: ${apertura[dia]:10,.2f} | Precio de cierre: ${cierre[dia]:10,.2f} | Variación porcentual: {variacion[dia]:10,.2f}%")
            
    #ENDTODO
