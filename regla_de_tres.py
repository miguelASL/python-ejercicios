import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def calcular_regla_de_tres():
    try:
        valor_a = float(entry_valor_a.get())
        valor_b = float(entry_valor_b.get())
        valor_x = float(entry_valor_x.get())

        # Regla de tres: (valor_a es a valor_b) => (valor_x es a ?)
        resultado = (valor_x * valor_b) / valor_a

        lbl_resultado.config(text=f"Resultado: {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos")


# Configuración de la ventana principal
app = tk.Tk()
app.title("Regla de Tres Simple")
app.geometry("800x600")
app.configure(bg="lightblue")


# Widgets
lbl_instruccion = ttk.Label(app, text="Completa la frase:", font=("Arial", 16))
lbl_instruccion.pack(pady=20)

lbl_frase = ttk.Label(app, text="Si ___ es a ___ entonces ___ es a ...", font=("Arial", 14))
lbl_frase.pack(pady=20)

entry_valor_a = ttk.Entry(app, font=("Arial", 14))
entry_valor_a.place(x=150, y=180, width=100)

entry_valor_b = ttk.Entry(app, font=("Arial", 14))
entry_valor_b.place(x=350, y=180, width=100)

entry_valor_x = ttk.Entry(app, font=("Arial", 14))
entry_valor_x.place(x=550, y=180, width=100)

btn_calcular = ttk.Button(app, text="Calcular", command=calcular_regla_de_tres, width=20)
btn_calcular.place(x=340, y=250)

lbl_resultado = ttk.Label(app, text="Resultado: -", font=("Arial", 16))
lbl_resultado.pack(pady=175)

lbl_emoticon = ttk.Label(app)
lbl_emoticon.pack(pady=10)

app.mainloop()