import numpy as np
import matplotlib.pyplot as plt
import os

def cargar_datos(nombre_archivo):
    """
    Lee el archivo línea por línea y almacena los datos en arreglos de NumPy.
    """
    lista_dias = []
    lista_temp = []
    lista_rad = []
    
    # Leer el archivo línea por línea
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # Limpiar espacios y separar por comas
            datos = linea.strip().split(',')
            
            # Asegurarnos de que haya exactamente 3 valores antes de procesar
            if len(datos) == 3:
                lista_dias.append(int(datos[0]))
                lista_temp.append(float(datos[1]))
                lista_rad.append(float(datos[2]))
                
    # Convertir a arreglos independientes de NumPy
    dias = np.array(lista_dias)
    temperaturas = np.array(lista_temp)
    radiaciones = np.array(lista_rad)
    
    return (dias, temperaturas, radiaciones)

def analizar_clima(dias, temperaturas, radiaciones):
    """
    Calcula e imprime los estadísticos básicos de temperatura y radiación.
    """
    temp_promedio = np.mean(temperaturas)
    temp_max = np.max(temperaturas)
    rad_promedio = np.mean(radiaciones)
    
    # Encontrar el índice donde ocurre la temperatura máxima para saber el día
    indice_max_temp = np.argmax(temperaturas)
    dia_max_temp = dias[indice_max_temp]
    
    print("--- Análisis del Clima ---")
    print(f"Temperatura promedio: {temp_promedio:.2f} °C")
    print(f"Temperatura máxima registrada: {temp_max:.2f} °C")
    print(f"Día de la temperatura máxima: {dia_max_temp}")
    print(f"Radiación solar promedio: {rad_promedio:.2f} W/m²")
    print("--------------------------\n")

def graficar_clima(dias, temperaturas, radiaciones):
    """
    Genera una figura con 2 subgráficas en una columna para visualizar los datos.
    """
    # Crear figura con 2 filas y 1 columna
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Gráfico superior: Días vs Temperaturas (Línea)
    ax1.plot(dias, temperaturas, color='red', marker='o', linestyle='-')
    ax1.set_title('Registro Semanal de Temperatura')
    ax1.set_ylabel('°C')
    ax1.grid(True)
    
    # Gráfico inferior: Días vs Radiaciones (Barras)
    ax2.bar(dias, radiaciones, color='orange', edgecolor='darkorange')
    ax2.set_title('Radiación Solar')
    ax2.set_xlabel('Día')
    ax2.set_ylabel('W/m²')
    ax2.grid(True, linestyle='--', alpha=0.5) # alpha=0.5 hace la cuadrícula tenue
    
    # Ajustar espacios y mostrar
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    nombre_archivo = 'datos_de_clima_hermosillo_ultimos_50_dias.txt '
    

    # 1. Lectura y Procesamiento
    dias, temperaturas, radiaciones = cargar_datos(nombre_archivo)
    
    if len(dias) > 0:
        # 2. Cálculos y Análisis
        analizar_clima(dias, temperaturas, radiaciones)
        
        # 3. Visualización Gráfica
        graficar_clima(dias, temperaturas, radiaciones)
    else:
        print("El archivo está vacío o no tiene el formato correcto.")