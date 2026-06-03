import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# Datos de acceso
# -----------------------------
usuario = "administrador"
clave = "123456"
contador = 0


# -----------------------------
# Función acceder
# -----------------------------
def acceder():
    global contador

    usuario_ingresado = txt_usuario.get()
    clave_ingresada = txt_clave.get()

    if usuario == usuario_ingresado and clave == clave_ingresada:
        messagebox.showinfo("Acceso correcto", "Puede ingresar al sistema")
        ventana.destroy()
        import dashboard

    else:
        contador += 1

        if contador < 3:
            messagebox.showwarning(
                "Acceso incorrecto",
                f"Las credenciales no existen.\nIntento {contador} de 3."
            )

        elif contador == 3:
            messagebox.showwarning(
                "Último intento",
                f"Las credenciales no existen.\nIntento {contador} de 3.\nEste es tu último intento."
            )

        else:
            messagebox.showerror(
                "Acceso bloqueado",
                "Agotó todos sus intentos.\nEl programa se cerrará."
            )
            ventana.destroy()




# -----------------------------
# Ventana principal
# -----------------------------
ventana = tk.Tk()
ventana.title("Acceso al Sistema de Soporte Técnico")
ventana.geometry("420x700+520+30")
ventana.resizable(False, False)
ventana.configure(bg="#EEF3FA")

ventana.bind("<Return>", lambda event: acceder())

# -----------------------------
# Estilos
# -----------------------------
estilo = ttk.Style()

# Usar tema vista si está disponible
if "vista" in estilo.theme_names():
    estilo.theme_use("vista")
else:
    estilo.theme_use("clam")

estilo.configure(
    "Fondo.TFrame",
    background="#EEF3FA"
)

estilo.configure(
    "Card.TFrame",
    background="#FFFFFF",
    relief="flat"
)

estilo.configure(
    "Titulo.TLabel",
    background="#FFFFFF",
    foreground="#172033",
    font=("Segoe UI", 20, "bold")
)

estilo.configure(
    "Subtitulo.TLabel",
    background="#FFFFFF",
    foreground="#6B7280",
    font=("Segoe UI", 10)
)

estilo.configure(
    "Texto.TLabel",
    background="#FFFFFF",
    foreground="#1F2937",
    font=("Segoe UI", 10, "bold")
)

estilo.configure(
    "Ayuda.TLabel",
    background="#FFFFFF",
    foreground="#6B7280",
    font=("Segoe UI", 9)
)

estilo.configure(
    "Campo.TEntry",
    font=("Segoe UI", 11),
    padding=8
)

estilo.configure(
    "Principal.TButton",
    font=("Segoe UI", 11, "bold"),
    padding=10
)

estilo.configure(
    "Limpiar.TButton",
    font=("Segoe UI", 10),
    padding=8
)


# -----------------------------
# Contenedor general
# -----------------------------
ventana.columnconfigure(0, weight=1)

frame_principal = ttk.Frame(ventana, style="Fondo.TFrame")
frame_principal.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)
frame_principal.columnconfigure(0, weight=1)


# -----------------------------
# Sombra simulada
# -----------------------------
sombra = tk.Frame(
    frame_principal,
    bg="#CBD5E1",
    bd=0
)
sombra.grid(row=0, column=0, sticky="nsew", padx=(5, 0), pady=(5, 0))


# -----------------------------
# Tarjeta blanca
# -----------------------------
card = ttk.Frame(
    frame_principal,
    style="Card.TFrame",
    padding=30
)
card.grid(row=0, column=0, sticky="nsew")
card.columnconfigure(0, weight=1)


# -----------------------------
# Logo o encabezado
# -----------------------------
try:
    logo_imagen = tk.PhotoImage(file="images/logo.png")
    logo_imagen = logo_imagen.subsample(10)

    lbl_logo = ttk.Label(card, image=logo_imagen, background="white")
    lbl_logo.grid(row=0, column=0, pady=(0, 15))

except tk.TclError:
    lbl_logo_texto = ttk.Label(
        card,
        text="🛠",
        background="white",
        foreground="#14388B",
        font=("Segoe UI Emoji", 40)
    )
    lbl_logo_texto.grid(row=0, column=0, pady=(0, 8))


# -----------------------------
# Título
# -----------------------------
lbl_titulo = ttk.Label(
    card,
    text="Bienvenido",
    style="Titulo.TLabel"
)
lbl_titulo.grid(row=1, column=0, pady=(0, 5))

lbl_subtitulo = ttk.Label(
    card,
    text="Sistema de Soporte Técnico",
    style="Subtitulo.TLabel"
)
lbl_subtitulo.grid(row=2, column=0, pady=(0, 25))


# -----------------------------
# Campo usuario
# -----------------------------
lbl_usuario = ttk.Label(
    card,
    text="Usuario",
    style="Texto.TLabel"
)
lbl_usuario.grid(row=3, column=0, sticky="w", pady=(0, 5))

txt_usuario = ttk.Entry(
    card,
    style="Campo.TEntry"
)
txt_usuario.grid(row=4, column=0, sticky="ew", ipady=5, pady=(0, 15))
txt_usuario.focus()


# -----------------------------
# Campo contraseña
# -----------------------------
lbl_clave = ttk.Label(
    card,
    text="Contraseña",
    style="Texto.TLabel"
)
lbl_clave.grid(row=5, column=0, sticky="w", pady=(0, 5))

txt_clave = ttk.Entry(
    card,
    show="*",
    style="Campo.TEntry"
)
txt_clave.grid(row=6, column=0, sticky="ew", ipady=5, pady=(0, 10))


# -----------------------------
# Texto de ayuda
# -----------------------------
lbl_ayuda = ttk.Label(
    card,
    text="Ingrese sus credenciales para acceder al sistema.",
    style="Ayuda.TLabel"
)
lbl_ayuda.grid(row=7, column=0, sticky="w", pady=(0, 25))


# -----------------------------
# Botón ingresar
# -----------------------------
btn_acceso = ttk.Button(
    card,
    text="Iniciar sesión",
    style="Principal.TButton",
    command=acceder
)
btn_acceso.grid(row=8, column=0, sticky="ew", pady=(0, 12))


ventana.mainloop()