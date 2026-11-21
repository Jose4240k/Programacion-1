import csv
from pathlib import Path

# Leo el archivo CSV del IMC.
carpeta = Path(__file__).resolve().parent
camino_archivo = carpeta / "datos_entrada_imc.csv"
camino_salida = carpeta / "ListadoIMC.csv"

with camino_archivo.open("r", encoding="utf-8", newline="") as archivo:
    filas = csv.reader(archivo)
    next(filas)  # Ignora el encabezado.
    #Escribo el archivo de salida con los resultados del IMC.
    with camino_salida.open("w", encoding="utf-8", newline="") as salida:
        escritor = csv.writer(salida)
        escritor.writerow(["Nombre", "IMC"])
        for fila in filas:
            if not fila:
                continue
            nombre = fila[0]
            peso = float(fila[1])
            altura = float(fila[2])
            imc = peso / (altura ** 2)
            escritor.writerow([nombre, f"{imc:.2f}"])