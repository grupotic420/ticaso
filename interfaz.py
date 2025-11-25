import tkinter as tk
from tkinter import messagebox

ingresos = []
gastos = []

def agregar_ingreso():
    try:
        cantidad = float(entry.get())
        ingresos.append(cantidad)
        messagebox.showinfo("Éxito", "Ingreso agregado correctamente.")
        entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Introduce un número válido.")

def agregar_gasto():
    try:
        cantidad = float(entry.get())
        gastos.append(cantidad)
        messagebox.showinfo("Éxito", "Gasto registrado correctamente.")
        entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Introduce un número válido.")

def ver_balance():
    total_ingresos = sum(ingresos)
    total_gastos = sum(gastos)
    balance = total_ingresos - total_gastos
    messagebox.showinfo("Balance", f"Balance total: {balance:.2f}")

def ver_movimientos():
    texto = "Ingresos:\n"
    for i in ingresos:
        texto += f"  + {i}\n"
    texto += "\nGastos:\n"
    for g in gastos:
        texto += f"  - {g}\n"

    messagebox.showinfo("Movimientos", texto)

ventana = tk.Tk()
ventana.title("Calculadora de Ingresos y Gastos")
ventana.geometry("350x350")

label = tk.Label(ventana, text="Introduce una cantidad:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(ventana, font=("Arial", 12))
entry.pack(pady=5)

btn_ingreso = tk.Button(ventana, text="Agregar Ingreso", command=agregar_ingreso)
btn_ingreso.pack(pady=5)

btn_gasto = tk.Button(ventana, text="Agregar Gasto", command=agregar_gasto)
btn_gasto.pack(pady=5)

btn_balance = tk.Button(ventana, text="Mostrar Balance", command=ver_balance)
btn_balance.pack(pady=5)

btn_movimientos = tk.Button(ventana, text="Mostrar Movimientos", command=ver_movimientos)
btn_movimientos.pack(pady=5)

ventana.mainloop()
