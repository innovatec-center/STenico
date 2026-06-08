
def agregar_usuario():
    nombre = "Juan"
    apellido = "Díaz"

    with open("users.txt","a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} {apellido}\n")
    
agregar_usuario()