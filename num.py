
from IPython.display import display, HTML
import numpy as np

caracter = "*"
n = 7
ancho = 2 * n - 1


def imprimir(matriz):
    for fila in matriz:
        print("".join(fila))


# 2. Triangulo lleno no invertido
display(HTML("<h2 style='color:blue'>2. Triangulo lleno no invertido</h2>"))

matriz = np.full((n, ancho), " ", dtype="U1")

for fila in range(n):
    for columna in range(ancho):
        if abs(columna - (n - 1)) <= fila:
            matriz[fila, columna] = caracter

imprimir(matriz)


# 3. Triangulo vacio no invertido
display(HTML("<h2 style='color:purple'>3. Triangulo vacio no invertido</h2>"))

matriz = np.full((n, ancho), " ", dtype="U1")

for fila in range(n):
    for columna in range(ancho):
        if columna == n - 1 - fila or columna == n - 1 + fila or fila == n - 1:
            matriz[fila, columna] = caracter

imprimir(matriz)


# 4. Reloj de arena lleno
display(HTML("<h2 style='color:green'>4. Reloj de arena lleno</h2>"))

matriz = np.full((ancho, ancho), " ", dtype="U1")

for fila in range(ancho):
    dist = min(fila, ancho - 1 - fila)
    c = dist
    d = ancho - dist

    matriz[fila, c:d] = caracter

imprimir(matriz)


# 5. Rombo vacio
display(HTML("<h2 style='color:orange'>5. Rombo vacio</h2>"))

matriz = np.full((ancho, ancho), " ", dtype="U1")

for fila in range(ancho):
    for columna in range(ancho):
        if abs(fila - ancho // 2) + abs(columna - ancho // 2) == ancho // 2:
            matriz[fila, columna] = caracter

imprimir(matriz)


# 6. Casa
display(HTML("<h2 style='color:brown'>6. Casa</h2>"))

alto = 11
ancho_casa = 13
centro = ancho_casa // 2

matriz = np.full((alto, ancho_casa), " ", dtype="U1")

# Techo
for fila in range(5):
    for columna in range(ancho_casa):
        if columna == centro - fila or columna == centro + fila:
            matriz[fila, columna] = caracter

# Paredes
for fila in range(5, alto):
    for columna in range(ancho_casa):
        if fila == 5 or columna == 2 or columna == 10 or fila == alto - 1:
            matriz[fila, columna] = caracter

# Puerta
for fila in range(7, 10):
    matriz[fila, centro - 1] = caracter
    matriz[fila, centro + 1] = caracter

matriz[6, centro - 1] = caracter
matriz[6, centro + 1] = caracter

# Ventanas
for fila in range(6, 8):
    for columna in range(3, 5):
        matriz[fila, columna] = caracter
    for columna in range(8, 10):
        matriz[fila, columna] = caracter

imprimir(matriz)


