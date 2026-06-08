import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox

def buscar():
    print("Buscar")

def abrir_modulo(nombre_archivo):
    ruta_modulo = Path(__file__).with_name(nombre_archivo)
    subprocess.Popen([sys.executable, str(ruta_modulo)])
    ventana.destroy()

def clientes():
    abrir_modulo("cliente.py")

def equipos():
    abrir_modulo("equipos.py")

def servicios_tecnicos():
    abrir_modulo("servicios.py")

def reportes():
    print("Reportes")

def salir():
    ventana.destroy()


# -----------------------------
# Ventana principal
# -----------------------------
ventana = tk.Tk()

# Centrar ventana
ancho_ventana = 300
alto_ventana = 400

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
ventana.title("Menú Principal")
ventana.configure(bg="#F4F6F9")
ventana.resizable(False, False)


# -----------------------------
# Estilos
# -----------------------------
estilo = ttk.Style()

# Tema moderno de Windows
estilo.theme_use("vista")

estilo.configure(
    "Titulo.TLabel",
    font=("Segoe UI", 20, "bold"),
    background="#F4F6F9",
    foreground="#1F2937",
    justify="center"
)

estilo.configure(
    "SubTitulo.TLabel",
    font=("Segoe UI", 10, "bold"),
    background="#F4F6F9",
    foreground="#374151",
    justify="center"
)

estilo.configure(
    "Entrada.TEntry",
    font=("Segoe UI", 10),
    padding=6
)

estilo.configure(
    "Boton.TButton",
    font=("Segoe UI", 10, "bold"),
    padding=7
)

estilo.configure(
    "Salir.TButton",
    font=("Segoe UI", 10, "bold"),
    padding=7
)


# -----------------------------
# Contenido
# -----------------------------
lbl_titulo = ttk.Label(
    ventana,
    text="⚙️ SISTEMA",
    style="Titulo.TLabel"
)
lbl_titulo.grid(row=0, column=0, pady=15)

lbl_buscar = ttk.Label(
    ventana,
    text="Buscar Módulo:",
    style="SubTitulo.TLabel"
)
lbl_buscar.grid(row=1, column=0, padx=25, pady=5, sticky="w")

txt_buscar = ttk.Entry(
    ventana,
    width=32,
    style="Entrada.TEntry"
)
txt_buscar.grid(row=2, column=0, padx=25, pady=5, sticky="ew")

btn_buscar = ttk.Button(
    ventana,
    text="Buscar",
    command=buscar,
    style="Boton.TButton"
)
btn_buscar.grid(row=3, column=0, padx=25, pady=6, sticky="ew")

btn_clientes = ttk.Button(
    ventana,
    text="Clientes",
    command=clientes,
    style="Boton.TButton"
)
btn_clientes.grid(row=4, column=0, padx=25, pady=6, sticky="ew")

btn_equipos = ttk.Button(
    ventana,
    text="Equipos",
    command=equipos,
    style="Boton.TButton"
)
btn_equipos.grid(row=5, column=0, padx=25, pady=6, sticky="ew")

btn_servicios = ttk.Button(
    ventana,
    text="Servicios Técnicos",
    command=servicios_tecnicos,
    style="Boton.TButton"
)
btn_servicios.grid(row=6, column=0, padx=25, pady=6, sticky="ew")

btn_reportes = ttk.Button(
    ventana,
    text="Reportes",
    command=reportes,
    style="Boton.TButton"
)
btn_reportes.grid(row=7, column=0, padx=25, pady=6, sticky="ew")

btn_salir = ttk.Button(
    ventana,
    text="Salir",
    command=salir,
    style="Salir.TButton"
)
btn_salir.grid(row=8, column=0, padx=25, pady=10, sticky="ew")


# Para que los elementos ocupen el mismo ancho disponible
ventana.columnconfigure(0, weight=1)

ventana.mainloop()
