import tkinter as lib
from tkinter import ttk as lib2


# ============================
# VENTANA PRINCIPAL
# ============================
ventana = lib.Tk()
ventana.title("Sistema de Soporte Técnico - Registro de Clientes")
ventana.resizable(False, False)
ventana.configure(bg="#F3F4F6")


# ============================
# CENTRAR VENTANA
# ============================
ancho_ventana = 1050
alto_ventana = 610

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

pos_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
pos_y = int((alto_pantalla / 2) - (alto_ventana / 2))

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")


# ============================
# ESTILOS
# ============================
estilo = lib2.Style()
estilo.theme_use("vista")

estilo.configure(
    "Titulo.TLabel",
    font=("Segoe UI", 18, "bold"),
    foreground="#111827",
    background="#F3F4F6"
)

estilo.configure(
    "Subtitulo.TLabel",
    font=("Segoe UI", 9),
    foreground="#6B7280",
    background="#F3F4F6"
)

estilo.configure(
    "Formulario.TLabelframe",
    background="#FFFFFF",
    borderwidth=1,
    relief="solid"
)

estilo.configure(
    "Formulario.TLabelframe.Label",
    font=("Segoe UI", 10, "bold"),
    foreground="#374151",
    background="#FFFFFF"
)

estilo.configure(
    "Campo.TLabel",
    font=("Segoe UI", 9, "bold"),
    foreground="#374151",
    background="#FFFFFF"
)

estilo.configure(
    "Campo.TEntry",
    font=("Segoe UI", 9),
    padding=4
)

estilo.configure(
    "Boton.TButton",
    font=("Segoe UI", 9, "bold"),
    padding=6
)

estilo.configure(
    "Treeview",
    font=("Segoe UI", 9),
    rowheight=25,
    background="#FFFFFF",
    fieldbackground="#FFFFFF",
    foreground="#111827",
    borderwidth=0
)

estilo.configure(
    "Treeview.Heading",
    font=("Segoe UI", 9, "bold"),
    background="#E5E7EB",
    foreground="#111827"
)

estilo.map(
    "Treeview",
    background=[("selected", "#DDEBFF")],
    foreground=[("selected", "#111827")]
)


# ============================
# ENCABEZADO
# ============================
frame_encabezado = lib.Frame(ventana, bg="#F3F4F6")
frame_encabezado.pack(fill="x", padx=25, pady=(15, 8))

lbl_titulo = lib2.Label(
    frame_encabezado,
    text="REGISTRO DE CLIENTES",
    style="Titulo.TLabel"
)
lbl_titulo.pack(anchor="w")

lbl_subtitulo = lib2.Label(
    frame_encabezado,
    text="Sistema de Soporte Técnico - CETPRO San José Obrero",
    style="Subtitulo.TLabel"
)
lbl_subtitulo.pack(anchor="w", pady=(2, 0))


# ============================
# CONTENEDOR PRINCIPAL
# ============================
frame_contenedor = lib.Frame(ventana, bg="#F3F4F6")
frame_contenedor.pack(fill="both", expand=True, padx=25, pady=5)


# ============================
# FORMULARIO
# ============================
lbl_frame_formulario = lib2.Labelframe(
    frame_contenedor,
    text=" Datos del cliente ",
    style="Formulario.TLabelframe"
)
lbl_frame_formulario.pack(fill="x", padx=5, pady=5)

frame_formulario = lib.Frame(lbl_frame_formulario, bg="#FFFFFF")
frame_formulario.pack(fill="x", padx=18, pady=(12, 8))


# ============================
# CAMPOS DEL FORMULARIO
# ============================

lbl_nombre = lib2.Label(frame_formulario, text="Nombre:", style="Campo.TLabel")
lbl_nombre.grid(column=0, row=0, sticky="w", padx=8, pady=5)

txt_nombre = lib2.Entry(frame_formulario, width=30, style="Campo.TEntry")
txt_nombre.grid(column=1, row=0, sticky="ew", padx=8, pady=5)


lbl_apellido = lib2.Label(frame_formulario, text="Apellido:", style="Campo.TLabel")
lbl_apellido.grid(column=2, row=0, sticky="w", padx=8, pady=5)

txt_apellido = lib2.Entry(frame_formulario, width=30, style="Campo.TEntry")
txt_apellido.grid(column=3, row=0, sticky="ew", padx=8, pady=5)


lbl_telefono = lib2.Label(frame_formulario, text="Teléfono:", style="Campo.TLabel")
lbl_telefono.grid(column=0, row=1, sticky="w", padx=8, pady=5)

txt_telefono = lib2.Entry(frame_formulario, width=30, style="Campo.TEntry")
txt_telefono.grid(column=1, row=1, sticky="ew", padx=8, pady=5)


lbl_dni = lib2.Label(frame_formulario, text="DNI:", style="Campo.TLabel")
lbl_dni.grid(column=2, row=1, sticky="w", padx=8, pady=5)

txt_dni = lib2.Entry(frame_formulario, width=30, style="Campo.TEntry")
txt_dni.grid(column=3, row=1, sticky="ew", padx=8, pady=5)


lbl_edad = lib2.Label(frame_formulario, text="Edad:", style="Campo.TLabel")
lbl_edad.grid(column=0, row=2, sticky="w", padx=8, pady=5)

txt_edad = lib2.Entry(frame_formulario, width=30, style="Campo.TEntry")
txt_edad.grid(column=1, row=2, sticky="ew", padx=8, pady=5)


lbl_correo = lib2.Label(frame_formulario, text="Correo:", style="Campo.TLabel")
lbl_correo.grid(column=2, row=2, sticky="w", padx=8, pady=5)

txt_correo = lib2.Entry(frame_formulario, width=30, style="Campo.TEntry")
txt_correo.grid(column=3, row=2, sticky="ew", padx=8, pady=5)


lbl_direccion = lib2.Label(frame_formulario, text="Dirección:", style="Campo.TLabel")
lbl_direccion.grid(column=0, row=3, sticky="w", padx=8, pady=5)

txt_direccion = lib2.Entry(frame_formulario, width=75, style="Campo.TEntry")
txt_direccion.grid(column=1, row=3, sticky="ew", padx=8, pady=5, columnspan=3)


# Ajustar columnas internas del formulario
frame_formulario.columnconfigure(1, weight=1)
frame_formulario.columnconfigure(3, weight=1)


# ============================
# BOTONES
# ============================
frame_botones = lib.Frame(lbl_frame_formulario, bg="#FFFFFF")
frame_botones.pack(fill="x", padx=18, pady=(2, 12))

boton_registrar = lib2.Button(
    frame_botones,
    text="📁 REGISTRAR",
    width=18,
    style="Boton.TButton"
)
boton_registrar.grid(column=0, row=0, padx=6, pady=5, sticky="ew")

boton_actualizar = lib2.Button(
    frame_botones,
    text="✏️ ACTUALIZAR",
    width=18,
    style="Boton.TButton"
)
boton_actualizar.grid(column=1, row=0, padx=6, pady=5, sticky="ew")

boton_eliminar = lib2.Button(
    frame_botones,
    text="❌ ELIMINAR",
    width=18,
    style="Boton.TButton"
)
boton_eliminar.grid(column=2, row=0, padx=6, pady=5, sticky="ew")

boton_limpiar = lib2.Button(
    frame_botones,
    text="🧹 LIMPIAR",
    width=18,
    style="Boton.TButton"
)
boton_limpiar.grid(column=3, row=0, padx=6, pady=5, sticky="ew")


# Para que los botones tengan el mismo ancho
for i in range(4):
    frame_botones.columnconfigure(i, weight=1)


# ============================
# TABLA
# ============================
lbl_frame_tabla = lib2.Labelframe(
    frame_contenedor,
    text=" Lista de clientes registrados ",
    style="Formulario.TLabelframe"
)
lbl_frame_tabla.pack(fill="both", expand=True, padx=5, pady=(6, 8))

frame_tabla = lib.Frame(lbl_frame_tabla, bg="#FFFFFF")
frame_tabla.pack(fill="both", expand=True, padx=12, pady=12)


columnas = (
    "Nº",
    "NOMBRE",
    "APELLIDO",
    "TELÉFONO",
    "DNI",
    "EDAD",
    "DIRECCIÓN",
    "CORREO"
)

lista = lib2.Treeview(
    frame_tabla,
    columns=columnas,
    show="headings",
    height=9
)

scroll_y = lib2.Scrollbar(frame_tabla, orient="vertical", command=lista.yview)
scroll_x = lib2.Scrollbar(frame_tabla, orient="horizontal", command=lista.xview)

lista.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

lista.grid(column=0, row=0, sticky="nsew")
scroll_y.grid(column=1, row=0, sticky="ns")
scroll_x.grid(column=0, row=1, sticky="ew")

frame_tabla.grid_columnconfigure(0, weight=1)
frame_tabla.grid_rowconfigure(0, weight=1)


# ============================
# CONFIGURACIÓN DE COLUMNAS
# ============================
lista.column("Nº", width=50, anchor="center", stretch=False)
lista.column("NOMBRE", width=130, anchor="center", stretch=False)
lista.column("APELLIDO", width=140, anchor="center", stretch=False)
lista.column("TELÉFONO", width=110, anchor="center", stretch=False)
lista.column("DNI", width=95, anchor="center", stretch=False)
lista.column("EDAD", width=60, anchor="center", stretch=False)
lista.column("DIRECCIÓN", width=220, anchor="center", stretch=False)
lista.column("CORREO", width=200, anchor="center", stretch=False)

for columna in columnas:
    lista.heading(columna, text=columna)


# ============================
# DATOS DE EJEMPLO
# ============================
lista.insert(
    "",
    "end",
    values=("1", "Juan", "Ramos Pérez", "987654321", "76543210", "28", "Huaraz", "juan@gmail.com")
)

lista.insert(
    "",
    "end",
    values=("2", "María", "Torres Luna", "912345678", "70123456", "32", "Independencia", "maria@gmail.com")
)


# ============================
# PIE DE VENTANA
# ============================
frame_pie = lib.Frame(ventana, bg="#E5E7EB", height=28)
frame_pie.pack(fill="x", side="bottom")

lbl_pie = lib.Label(
    frame_pie,
    text="Proyecto App Soporte Técnico | Sprint 1 | Developer: Sayuri",
    bg="#E5E7EB",
    fg="#4B5563",
    font=("Segoe UI", 8)
)
lbl_pie.pack(pady=5)


ventana.mainloop()