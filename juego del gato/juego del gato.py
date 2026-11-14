import tkinter as tk
from tkinter import messagebox
import random

# Función que verifica si alguien ganó y devuelve "X", "O" o None
def verificar_ganador():
    for i in range(3):
        if botones[i][0]['text'] == botones[i][1]['text'] == botones[i][2]['text'] != "":
            return botones[i][0]['text']
        if botones[0][i]['text'] == botones[1][i]['text'] == botones[2][i]['text'] != "":
            return botones[0][i]['text']
            
    if botones[0][0]['text'] == botones[1][1]['text'] == botones[2][2]['text'] != "":
        return botones[0][0]['text']
    if botones[0][2]['text'] == botones[1][1]['text'] == botones[2][0]['text'] != "":
        return botones[0][2]['text']
        
    return None

# Función que verifica si el tablero está lleno
def verificar_empate():
    for fila in range(3):
        for columna in range(3):
            if botones[fila][columna]['text'] == "":
                return False
    return True

# Función que maneja el fin de la partida
def procesar_estado():
    ganador = verificar_ganador()
    if ganador:
        if ganador == "X":
            messagebox.showinfo("¡Fin del juego!", "¡Felicidades, ganaste!")
        else:
            messagebox.showinfo("¡Fin del juego!", "¡La computadora ha ganado!")
        return True
    elif verificar_empate():
        messagebox.showinfo("¡Fin del juego!", "¡Es un empate!")
        return True
    return False

# Turno de la computadora
def movimiento_computadora():
    global turno_jugador
    
    # 1. Buscar todas las casillas que están vacías
    casillas_vacias = []
    for fila in range(3):
        for columna in range(3):
            if botones[fila][columna]['text'] == "":
                casillas_vacias.append((fila, columna))
                
    # 2. Si hay casillas vacías, elegir una al azar
    if casillas_vacias:
        fila, columna = random.choice(casillas_vacias)
        botones[fila][columna]['text'] = "O"
        
        # 3. Comprobar si la computadora ganó con este movimiento
        if not procesar_estado():
            # Si nadie ha ganado, le toca de nuevo al jugador
            turno_jugador = True
            etiqueta_turno.config(text="Tu turno (X)")

# Turno del jugador
def clic_boton(fila, columna):
    global turno_jugador

    # Solo registrar el clic si es el turno del jugador y la casilla está vacía
    if turno_jugador and botones[fila][columna]['text'] == "":
        botones[fila][columna]['text'] = "X"
        turno_jugador = False  # Bloqueamos los clics para que el jugador no haga trampa
        
        # Comprobar si el jugador ganó
        if not procesar_estado():
            etiqueta_turno.config(text="Computadora pensando...")
            # Llamar a la computadora después de 500 milisegundos (medio segundo)
            ventana.after(500, movimiento_computadora)

# Limpiar tablero
def reiniciar_juego():
    global turno_jugador
    turno_jugador = True
    etiqueta_turno.config(text="Tu turno (X)")
    
    for fila in range(3):
        for columna in range(3):
            botones[fila][columna].config(text="")

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Gato: Jugador vs Computadora")
ventana.resizable(False, False)

# Variable de control de turnos
turno_jugador = True # True = Jugador(X), False = Computadora(O)

etiqueta_turno = tk.Label(ventana, text="Tu turno (X)", font=('Arial', 14, 'bold'))
etiqueta_turno.grid(row=0, column=0, columnspan=3, pady=10)

botones = [[None for _ in range(3)] for _ in range(3)]

for fila in range(3):
    for columna in range(3):
        botones[fila][columna] = tk.Button(
            ventana, text="", font=('Arial', 40, 'bold'), width=4, height=1,
            command=lambda f=fila, c=columna: clic_boton(f, c)
        )
        botones[fila][columna].grid(row=fila+1, column=columna, padx=2, pady=2)

boton_reinicio = tk.Button(ventana, text="Reiniciar Juego", font=('Arial', 12), command=reiniciar_juego)
boton_reinicio.grid(row=4, column=0, columnspan=3, pady=10)

ventana.mainloop()