import random
from pathlib import Path
## Genera una matriz de nxn donde n es un número aleatorio entre 1 y 10 inicializada en ceros
n = random.randint(5, 20)
matriz = [[0 for _ in range(n)] for _ in range(n)]
#formo un triangulo de asteriscos debajo de la diagonal principal de la matriz
for i in range(n):
    for j in range(i):
        matriz[i][j] = "*"
for fila in matriz:
    print(fila)
camino_archivo = Path(__file__).with_name("triangulo_inferior.txt")
#Genero un archivo de texto con la matriz generada
with open(camino_archivo, "w") as archivo:
    for fila in matriz:
        archivo.write(" ".join(str(x) for x in fila) + "\n")
        