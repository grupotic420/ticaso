# Listas donde se guardan ingresos y gastos
ingresos = []
gastos = []

import tkinter as tk
from tkinter import messagebox

# Función para agregar un ingreso
def agregar_ingreso():
    try:
        cantidad = float(entry.get())
        ingresos.append(cantidad)
        messagebox.showinfo("Éxito", "Ingreso agregado correctamente.")
        entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Introduce un número válido.")

# Función para agregar un gasto
def agregar_gasto():
    try:
        cantidad = float(entry.get())
        gastos.append(cantidad)
        messagebox.showinfo("Éxito", "Gasto registrado correctamente.")
        entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Introduce un número válido.")

# Función que calcula y muestra el balance
def ver_balance():
    total_ingresos = sum(ingresos)
    total_gastos = sum(gastos)
    balance = total_ingresos - total_gastos

    if balance < 0:
        label_balance.config(text=f"Balance: {balance:.2f}", fg="red")
    else:
        label_balance.config(text=f"Balance: {balance:.2f}", fg="green")

# Función para mostrar todos los movimientos
def ver_movimientos():
    texto = "Ingresos:\n"
    for i in ingresos:
        texto += f"  + {i}\n"

    texto += "\nGastos:\n"
    for g in gastos:
        texto += f"  - {g}\n"

    messagebox.showinfo("Movimientos", texto)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Ingresos y Gastos")
ventana.geometry("350x400")

# Etiqueta de instrucciones
label = tk.Label(ventana, text="Introduce una cantidad:", font=("Arial", 12))
label.pack(pady=10)

# Caja donde se escribe el número
entry = tk.Entry(ventana, font=("Arial", 12))
entry.pack(pady=5)

# Botón para ingresos
btn_ingreso = tk.Button(ventana, text="Agregar Ingreso", command=agregar_ingreso)
btn_ingreso.pack(pady=5)

# Botón para gastos
btn_gasto = tk.Button(ventana, text="Agregar Gasto", command=agregar_gasto)
btn_gasto.pack(pady=5)

# Botón para mostrar balance
btn_balance = tk.Button(ventana, text="Mostrar Balance", command=ver_balance)
btn_balance.pack(pady=5)

# Botón para mostrar movimientos
btn_movimientos = tk.Button(ventana, text="Mostrar Movimientos", command=ver_movimientos)
btn_movimientos.pack(pady=5)

# Etiqueta donde se actualiza el balance
label_balance = tk.Label(ventana, text="Balance: 0.00", font=("Arial", 14))
label_balance.pack(pady=10)

# Mantiene la ventana abierta
ventana.mainloop()
