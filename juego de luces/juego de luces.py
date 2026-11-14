import tkinter as tk
import random
from tkinter import messagebox

class JuegoLuces:
    def __init__(self, root, num_luces=7):
        self.root = root
        self.root.title("Juego de Luces (1D)")
        self.num_luces = num_luces
        self.estado = [0] * num_luces
        self.botones = []

        # Contenedor principal
        frame = tk.Frame(root, bg="#222")
        frame.pack(padx=20, pady=20)
        self.root.configure(bg="#222")

        # Crear la fila de focos (botones)
        for i in range(num_luces):
            btn = tk.Button(
                frame, 
                width=4, height=2, 
                relief="raised",
                command=lambda idx=i: self.presionar_foco(idx)
            )
            btn.pack(side=tk.LEFT, padx=5)
            self.botones.append(btn)

        # Generar un tablero aleatorio pero con solución garantizada
        self.mezclar()
        self.actualizar_interfaz()

    def mezclar(self):
        # Simulamos clics aleatorios para asegurar que el rompecabezas tenga solución
        for _ in range(self.num_luces * 2):
            idx = random.randint(0, self.num_luces - 1)
            self._logica_cambio(idx)

    def _logica_cambio(self, i):
        # Cambiar el estado del foco actual
        self.estado[i] = 1 - self.estado[i]
        # Cambiar el vecino izquierdo (si existe)
        if i > 0:
            self.estado[i-1] = 1 - self.estado[i-1]
        # Cambiar el vecino derecho (si existe)
        if i < self.num_luces - 1:
            self.estado[i+1] = 1 - self.estado[i+1]

    def presionar_foco(self, i):
        self._logica_cambio(i)
        self.actualizar_interfaz()
        self.verificar_victoria()

    def actualizar_interfaz(self):
        for i in range(self.num_luces):
            # Amarillo si está encendido (1), Gris oscuro si está apagado (0)
            color_fondo = "#FFD700" if self.estado[i] == 1 else "#555555"
            self.botones[i].config(bg=color_fondo, activebackground=color_fondo)

    def verificar_victoria(self):
        # El objetivo es apagar todas las luces (todos los estados en 0)
        if all(luz == 0 for luz in self.estado):
            messagebox.showinfo("¡Felicidades!", "¡Has apagado todas las luces!")
            self.mezclar()
            self.actualizar_interfaz()

if __name__ == "__main__":
    root = tk.Tk()
    # Puedes cambiar el número 7 para hacer la fila más larga o más corta
    app = JuegoLuces(root, num_luces=7) 
    root.mainloop()