import numpy as np
n= int(input("Tamaño de la matriz: "))
i=int(input(f"Dame un numero en el rango de {n}"))
j=int(input(f"Dame un numero en el rango de {n}"))
matriz=np.zeros((n,n),dtype=np.uint(8))
for fila in range(n):
    for columna in range(n):
        if fila-columna== i-j:
            matriz[fila,columna]=1
for fila in range(n):
    for columna in range(n):
        if fila+columna== i+j:
            matriz[fila,columna]=1
for fila in range(n):
    matriz[i,:]=1
for columna in range(n):
    matriz[:,j]=1
print(matriz)