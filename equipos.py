import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox


# -----------------------------
# Función registrar
# -----------------------------
def registrar_equipo():
    info = (
        f"Nombre: {entry_nombre.get()}\n"
        f"Marca: {combo_marca.get()}\n"
        f"Código: {entry_codigo.get()}\n"
        f"Color: {entry_color.get()}\n"
        f"Estado: {combo_estado.get()}\n"
        f"Observaciones: {entry_obs.get()}"
    )

    messagebox.showinfo(
        "Registro exitoso",
        f"Equipo registrado correctamente:\n\n{info}"
    )


# -----------------------------
# Ventana principal
# -----------------------------
app = tk.Tk()
app.title("Registro de Equipos")

ancho_ventana = 460
alto_ventana = 380

ancho_pantalla = app.winfo_screenwidth()
alto_pantalla = app.winfo_screenheight()

posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))

app.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
app.resizable(False, False)
app.configure(bg="#F3F4F6")

def cerrar_ventana():
    ruta_dashboard = Path(__file__).with_name("dashboard.py")
    subprocess.Popen([sys.executable, str(ruta_dashboard)])
    app.destroy()

app.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# -----------------------------
# Estilos
# -----------------------------
style = ttk.Style()
style.theme_use("vista")

style.configure(
    "Titulo.TLabel",
    font=("Segoe UI", 16, "bold"),
    background="#F3F4F6",
    foreground="#111827"
)

style.configure(
    "Formulario.TLabel",
    font=("Segoe UI", 10),
    background="#F3F4F6",
    foreground="#374151"
)

style.configure(
    "Campo.TEntry",
    font=("Segoe UI", 10),
    padding=4
)

style.configure(
    "Campo.TCombobox",
    font=("Segoe UI", 10),
    padding=4
)

style.configure(
    "Principal.TButton",
    font=("Segoe UI", 10, "bold"),
    padding=7
)


# -----------------------------
# Título
# -----------------------------
titulo = ttk.Label(
    app,
    text="Registro de Equipo",
    style="Titulo.TLabel"
)
titulo.grid(row=0, column=0, columnspan=2, pady=(18, 12))


# -----------------------------
# Nombre del Equipo
# -----------------------------
lbl_nombre = ttk.Label(
    app,
    text="Nombre del Equipo:",
    style="Formulario.TLabel"
)
lbl_nombre.grid(row=1, column=0, padx=(35, 10), pady=6, sticky="w")

entry_nombre = ttk.Entry(
    app,
    width=28,
    style="Campo.TEntry"
)
entry_nombre.grid(row=1, column=1, padx=(5, 35), pady=6, sticky="ew")


# -----------------------------
# Marca
# -----------------------------
lbl_marca = ttk.Label(
    app,
    text="Marca:",
    style="Formulario.TLabel"
)
lbl_marca.grid(row=2, column=0, padx=(35, 10), pady=6, sticky="w")

combo_marca = ttk.Combobox(
    app,
    values=["HP", "Dell", "Lenovo", "Apple", "Asus", "Otra"],
    width=26,
    state="readonly",
    style="Campo.TCombobox"
)
combo_marca.grid(row=2, column=1, padx=(5, 35), pady=6, sticky="ew")
combo_marca.current(0)


# -----------------------------
# Código
# -----------------------------
lbl_codigo = ttk.Label(
    app,
    text="Código:",
    style="Formulario.TLabel"
)
lbl_codigo.grid(row=3, column=0, padx=(35, 10), pady=6, sticky="w")

entry_codigo = ttk.Entry(
    app,
    width=28,
    style="Campo.TEntry"
)
entry_codigo.grid(row=3, column=1, padx=(5, 35), pady=6, sticky="ew")


# -----------------------------
# Color
# -----------------------------
lbl_color = ttk.Label(
    app,
    text="Color:",
    style="Formulario.TLabel"
)
lbl_color.grid(row=4, column=0, padx=(35, 10), pady=6, sticky="w")

entry_color = ttk.Entry(
    app,
    width=28,
    style="Campo.TEntry"
)
entry_color.grid(row=4, column=1, padx=(5, 35), pady=6, sticky="ew")


# -----------------------------
# Estado
# -----------------------------
lbl_estado = ttk.Label(
    app,
    text="Estado:",
    style="Formulario.TLabel"
)
lbl_estado.grid(row=5, column=0, padx=(35, 10), pady=6, sticky="w")

combo_estado = ttk.Combobox(
    app,
    values=["Nuevo", "Buen estado", "Mantenimiento", "Baja"],
    width=26,
    state="readonly",
    style="Campo.TCombobox"
)
combo_estado.grid(row=5, column=1, padx=(5, 35), pady=6, sticky="ew")
combo_estado.current(1)


# -----------------------------
# Observaciones
# -----------------------------
lbl_obs = ttk.Label(
    app,
    text="Observaciones:",
    style="Formulario.TLabel"
)
lbl_obs.grid(row=6, column=0, padx=(35, 10), pady=6, sticky="w")

entry_obs = ttk.Entry(
    app,
    width=28,
    style="Campo.TEntry"
)
entry_obs.grid(row=6, column=1, padx=(5, 35), pady=6, sticky="ew")


# -----------------------------
# Botón Registrar
# -----------------------------
btn_registrar = ttk.Button(
    app,
    text="Registrar Equipo",
    command=registrar_equipo,
    style="Principal.TButton"
)
btn_registrar.grid(
    row=7,
    column=0,
    columnspan=2,
    padx=120,
    pady=(20, 10),
    sticky="ew"
)


# -----------------------------
# Ajuste de columnas
# -----------------------------
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=2)


# -----------------------------
# Ejecutar aplicación
# -----------------------------
app.mainloop()
