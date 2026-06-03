import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# Función para ingresar datos
# -----------------------------
def ingresar():
    datos = {
        "Código": codigo.get(),
        "Nombre": nombre.get(),
        "Marca": marca.get(),
        "Modelo": modelo.get(),
        "Ingreso": ingreso.get(),
        "Salida": salida.get(),
        "Empleado": empleado.get()
    }

    mensaje = ""
    for clave, valor in datos.items():
        mensaje += f"{clave}: {valor}\n"

    messagebox.showinfo("Datos Registrados", mensaje)


# -----------------------------
# Función buscar
# -----------------------------
def buscar():
    messagebox.showinfo("Buscar", f"Buscando código: {codigo.get()}")


# -----------------------------
# Ventana principal
# -----------------------------
ventana = tk.Tk()
ventana.title("Recepción de Servicios")
ventana.geometry("560x520")
ventana.resizable(False, False)
ventana.configure(bg="#F4F6F9")


# -----------------------------
# Estilos ttk
# -----------------------------
estilo = ttk.Style()

try:
    estilo.theme_use("vista")
except:
    estilo.theme_use("clam")

estilo.configure(
    "Titulo.TLabel",
    font=("Segoe UI", 16, "bold"),
    background="#F4F6F9",
    foreground="#1F2937"
)

estilo.configure(
    "Subtitulo.TLabel",
    font=("Segoe UI", 9),
    background="#F4F6F9",
    foreground="#6B7280"
)

estilo.configure(
    "TLabel",
    font=("Segoe UI", 10),
    background="#FFFFFF",
    foreground="#374151"
)

estilo.configure(
    "TLabelframe",
    background="#FFFFFF",
    borderwidth=1,
    relief="solid"
)

estilo.configure(
    "TLabelframe.Label",
    font=("Segoe UI", 11, "bold"),
    background="#FFFFFF",
    foreground="#1F2937"
)

estilo.configure(
    "TEntry",
    font=("Segoe UI", 10),
    padding=5
)

estilo.configure(
    "TCombobox",
    font=("Segoe UI", 10),
    padding=5
)

estilo.configure(
    "Accion.TButton",
    font=("Segoe UI", 10, "bold"),
    padding=(12, 8)
)


# -----------------------------
# Título superior
# -----------------------------
lbl_titulo = ttk.Label(
    ventana,
    text="Recepción de Servicios",
    style="Titulo.TLabel"
)
lbl_titulo.pack(pady=(18, 2))

lbl_subtitulo = ttk.Label(
    ventana,
    text="Registro y búsqueda de equipos para soporte técnico",
    style="Subtitulo.TLabel"
)
lbl_subtitulo.pack(pady=(0, 12))


# -----------------------------
# Marco principal
# -----------------------------
frame = ttk.LabelFrame(
    ventana,
    text=" Datos del Equipo ",
    padding=(20, 15)
)
frame.pack(padx=25, pady=10, fill="both", expand=True)

# Configuración de columnas
frame.columnconfigure(0, weight=0)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=0)


# -----------------------------
# Campos
# -----------------------------
ttk.Label(frame, text="Código").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=7)
codigo = ttk.Entry(frame, width=28)
codigo.grid(row=0, column=1, sticky="ew", pady=7)

ttk.Label(frame, text="Nombre").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=7)
nombre = ttk.Combobox(frame, values=["Laptop", "PC", "Impresora"], width=25, state="readonly")
nombre.grid(row=1, column=1, sticky="ew", pady=7)

ttk.Label(frame, text="Marca").grid(row=2, column=0, sticky="w", padx=(0, 10), pady=7)
marca = ttk.Combobox(frame, values=["HP", "Dell", "Lenovo", "Epson", "Samsung"], width=25, state="readonly")
marca.grid(row=2, column=1, sticky="ew", pady=7)

ttk.Label(frame, text="Modelo").grid(row=3, column=0, sticky="w", padx=(0, 10), pady=7)
modelo = ttk.Entry(frame, width=28)
modelo.grid(row=3, column=1, sticky="ew", pady=7)

ttk.Label(frame, text="Ingreso").grid(row=4, column=0, sticky="w", padx=(0, 10), pady=7)
ingreso = ttk.Entry(frame, width=28)
ingreso.grid(row=4, column=1, sticky="ew", pady=7)

ttk.Label(frame, text="Salida").grid(row=5, column=0, sticky="w", padx=(0, 10), pady=7)
salida = ttk.Entry(frame, width=28)
salida.grid(row=5, column=1, sticky="ew", pady=7)

ttk.Label(frame, text="Empleado").grid(row=6, column=0, sticky="w", padx=(0, 10), pady=7)
empleado = ttk.Entry(frame, width=28)
empleado.grid(row=6, column=1, sticky="ew", pady=7)


# -----------------------------
# Botones
# -----------------------------
btn_buscar = ttk.Button(
    frame,
    text="Buscar",
    command=buscar,
    style="Accion.TButton"
)
btn_buscar.grid(row=1, column=2, padx=(25, 0), pady=7, sticky="ew")

btn_ingresar = ttk.Button(
    frame,
    text="Ingresar",
    command=ingresar,
    style="Accion.TButton"
)
btn_ingresar.grid(row=3, column=2, padx=(25, 0), pady=7, sticky="ew")


# -----------------------------
# Iniciar ventana
# -----------------------------
ventana.mainloop()