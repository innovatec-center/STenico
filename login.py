import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

usuario = "administrador"
clave = "123456"
contador = 1

def acceder():
    usuario_ingresado = txt_usuario.get()
    clave_ingresada = txt_clave.get()

    if(usuario==usuario_ingresado and clave==clave_ingresada):
        messagebox.showinfo("Acceso correcto", "Puede ingresar al sistema")
        ventana.destroy()
        import dashboard

    else:
        messagebox.showerror("Acceso incorrecto", f"Las credenciales no existen tienes {contador} intento(s)")
        

# Configuración básica de la ventana
ventana = tk.Tk()
ventana.title("Acceso al Sistema de Soporte Técnico")
ventana.geometry("380x550+550+100") # Aumenté un poco el tamaño para dar más aire visual
ventana.resizable(False, False)

# NUEVO: Cambiar el color de fondo de la ventana principal para que coincida con el estilo moderno
ventana.configure(bg="#F4F6F9") 

# Configuración de estilos con ttk
estilo = ttk.Style()
estilo.theme_use("vista") # Cambiado a 'clam': es más flexible para personalizar colores que 'vista'

# NUEVO: Configurar el fondo general de los Labels del contenedor para que no tengan un recuadro gris
estilo.configure(".", background="#F4F6F9")

# Estilo para las etiquetas de texto
estilo.configure(
    "lblTexto.TLabel",
    foreground="#1E293B", # Un azul oscuro/gris pizarra más moderno que el azul puro
    font=("Segoe UI", 11, "bold") # 'Segoe UI' se ve más limpia y profesional que Arial
)

# NOTA APRENDIZAJE: ttk.Entry no acepta 'font' ni 'width' directamente en el estilo en todos los temas.
# Es una buena práctica de Tkinter pasar esos parámetros directamente al crear el widget.

# NUEVO: Estilo personalizado para el botón de acceso (Estilo moderno tipo Web)
estilo.configure(
    "btnModerno.TButton",
    foreground="white",
    background="#0F172A", # Fondo azul oscuro empresarial
    font=("Segoe UI", 11, "bold"),
    borderwidth=0,
    focusthickness=0
)
# NUEVO: Efecto "Hover" (Cambia de color el botón al pasar el mouse por encima)
estilo.map("btnModerno.TButton", background=[("active", "#334155")])

# Configuración de las columnas de la ventana para que los elementos se centren correctamente
ventana.columnconfigure(0, weight=1)

# --- IMAGEN / LOGO ---
# Nota: Asegúrate de tener la imagen en la ruta correcta. 
# Añadí un bloque try/except por si ejecutas el código sin la imagen, así no se romperá el programa.
try:
    logo_imagen = tk.PhotoImage(file="images/logo.png")
    logo_imagen = logo_imagen.subsample(10)
    lbl_logo = ttk.Label(ventana, image=logo_imagen)
    lbl_logo.grid(row=0, column=0, pady=(30, 20), sticky="n") # Agregado espacio arriba y abajo
except tk.TclError:
    # Si no encuentra la imagen, pone un texto temporal elegante para que el código corra igual
    lbl_logo = ttk.Label(ventana, text="SOPORTE TÉCNICO", font=("Segoe UI", 16, "bold"), foreground="#0F172A")
    lbl_logo.grid(row=0, column=0, pady=(40, 30), sticky="n")

# NUEVO: Contenedor central (Frame). Agrupar los campos en un marco hace que el diseño sea más limpio.
# Nos permite centrar todo el bloque de inicio de sesión fácilmente en la pantalla.
frm_contenedor = ttk.Frame(ventana)
frm_contenedor.grid(row=1, column=0, padx=40, sticky="nsew")
frm_contenedor.columnconfigure(0, weight=1)

# --- CAMPO: USUARIO ---
lbl_usuario = ttk.Label(frm_contenedor, text="Usuario", style="lblTexto.TLabel")
lbl_usuario.grid(row=0, column=0, sticky="w", pady=(0, 5))

# MEJORA: Definimos ancho (width) y fuente directamente en el widget para evitar fallos de estilos de ttk
txt_usuario = ttk.Entry(frm_contenedor, font=("Segoe UI", 11), width=28)
txt_usuario.grid(row=1, column=0, ipady=6, pady=(0, 15), sticky="ew") 
# 'ipady=6' le da una altura interna al campo de texto, haciéndolo lucir como una app moderna

# --- CAMPO: CLAVE ---
lbl_clave = ttk.Label(frm_contenedor, text="Contraseña", style="lblTexto.TLabel")
lbl_clave.grid(row=2, column=0, sticky="w", pady=(0, 5))

txt_clave = ttk.Entry(frm_contenedor, show="*", font=("Segoe UI", 11), width=28)
txt_clave.grid(row=3, column=0, ipady=6, pady=(0, 25), sticky="ew")

# --- BOTÓN DE ACCESO ---
# MEJORA: Aplicamos el nuevo estilo 'btnModerno.TButton' y usamos 'cursor="hand2"'
# NUEVO: 'cursor="hand2"' cambia la flecha del mouse por la mano de "click" al pasar sobre el botón
btn_acceso = tk.Button(
    frm_contenedor, 
    text="Iniciar Sesión", 
    bg="#14388B", 
    fg="white", 
    font=("Segoe UI", 11, "bold"),
    activebackground="#334155",
    activeforeground="#D1EC91",
    bd=0, 
    cursor="hand2",
    command=acceder
)
btn_acceso.grid(row=4, column=0, ipady=8, sticky="ew") 
# 'sticky="ew"' hace que el botón se estire y ocupe el mismo ancho que los campos de texto anteriores

ventana.mainloop()