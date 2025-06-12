import tkinter as tk
from tkinter import messagebox

class JuegoDelGato:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Gato")
        self.turno = "X"
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.botones = [[None for _ in range(3)] for _ in range(3)]
        self.puntaje_x = 0
        self.puntaje_o = 0

        self.marco_superior = tk.Frame(self.root)
        self.marco_superior.pack()

        self.etiqueta_puntaje = tk.Label(self.marco_superior, text=self.obtener_texto_puntaje(),
                                         font=("Arial", 14))
        self.etiqueta_puntaje.pack(pady=10)

        self.marco_tablero = tk.Frame(self.root)
        self.marco_tablero.pack()

        self.crear_interfaz()

    def obtener_texto_puntaje(self):
        return f"Puntos - X: {self.puntaje_x}    O: {self.puntaje_o}"

    def crear_interfaz(self):
        for fila in range(3):
            for col in range(3):
                boton = tk.Button(self.marco_tablero, text="", font=("Arial", 40), width=5, height=2,
                                  command=lambda f=fila, c=col: self.jugar(f, c))
                boton.grid(row=fila, column=col)
                self.botones[fila][col] = boton

    def jugar(self, fila, col):
        if self.tablero[fila][col] == "":
            self.tablero[fila][col] = self.turno
            self.botones[fila][col].config(text=self.turno, state="disabled")
            if self.verificar_ganador(self.turno):
                messagebox.showinfo("Fin del juego", f"¡{self.turno} ha ganado!")
                if self.turno == "X":
                    self.puntaje_x += 1
                else:
                    self.puntaje_o += 1
                self.etiqueta_puntaje.config(text=self.obtener_texto_puntaje())
                self.reiniciar_juego()
            elif self.tablero_lleno():
                messagebox.showinfo("Fin del juego", "¡Empate!")
                self.reiniciar_juego()
            else:
                self.turno = "O" if self.turno == "X" else "X"

    def verificar_ganador(self, jugador):
        for i in range(3):
            if all(self.tablero[i][j] == jugador for j in range(3)) or \
               all(self.tablero[j][i] == jugador for j in range(3)):
                return True
        if all(self.tablero[i][i] == jugador for i in range(3)) or \
           all(self.tablero[i][2 - i] == jugador for i in range(3)):
            return True
        return False

    def tablero_lleno(self):
        return all(self.tablero[fila][col] != "" for fila in range(3) for col in range(3))

    def reiniciar_juego(self):
        self.turno = "X"
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        for fila in range(3):
            for col in range(3):
                self.botones[fila][col].config(text="", state="normal")

# Crear ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoDelGato(root)
    root.mainloop()