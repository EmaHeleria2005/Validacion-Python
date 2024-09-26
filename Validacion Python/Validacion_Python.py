import tkinter as tk
from tkinter import messagebox

def es_numero(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def es_texto(s):
    return s.isalpha()

def validar_entrada():
    nombre = entry_nombre.get().strip()
    apellido = entry_apellido.get().strip()
    telefono = entry_telefono.get().strip()
    estatura = entry_estatura.get().strip()
    edad = entry_edad.get().strip()
    genero = var_genero.get()

    # Verificar si todos los campos están completos
    if not nombre or not apellido or not telefono or not estatura or not edad or not genero:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return False

    # Validar que nombre y apellido solo contengan letras
    if not es_texto(nombre) or not es_texto(apellido):
        messagebox.showerror("Error", "El nombre y apellido solo pueden contener letras.")
        return False

    # Validar los campos numéricos
    errores = []
    if not es_numero(telefono):
        errores.append("Teléfono")
    if not es_numero(edad):
        errores.append("Edad")
    if not es_numero(estatura):
        errores.append("Estatura")
    
    if errores:
        messagebox.showerror("Error", f"Los siguientes campos deben contener solo números: {', '.join(errores)}")
        return False

    return True

def guardar():
    if validar_entrada():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        estatura = entry_estatura.get()
        edad = entry_edad.get()
        genero = var_genero.get()

        messagebox.showinfo("Guardado", f"Datos guardados:\n\nNombre: {nombre}\nApellido: {apellido}\nTeléfono: {telefono}\nEstatura: {estatura}\nEdad: {edad}\nGénero: {genero}")
        limpiar_campos()

def cancelar():
    limpiar_campos()

def limpiar_campos():
 
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_estatura.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    var_genero.set(None)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Información")

# Crear etiquetas y entradas
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Apellido:").grid(row=1, column=0, padx=10, pady=5)
entry_apellido = tk.Entry(ventana)
entry_apellido.grid(row=1, column=1)

tk.Label(ventana, text="Teléfono:").grid(row=2, column=0, padx=10, pady=5)
entry_telefono = tk.Entry(ventana)
entry_telefono.grid(row=2, column=1)

tk.Label(ventana, text="Estatura (cm):").grid(row=3, column=0, padx=10, pady=5)
entry_estatura = tk.Entry(ventana)
entry_estatura.grid(row=3, column=1)

tk.Label(ventana, text="Edad:").grid(row=4, column=0, padx=10, pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=4, column=1)

tk.Label(ventana, text="Género:").grid(row=5, column=0, padx=10, pady=5)
var_genero = tk.StringVar(value=None)
tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value="Hombre").grid(row=5, column=1, sticky=tk.W)
tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value="Mujer").grid(row=5, column=1, sticky=tk.E)

# Crear botones
btn_guardar = tk.Button(ventana, text="Guardar", command=guardar)
btn_guardar.grid(row=6, column=0, padx=10, pady=10)

btn_cancelar = tk.Button(ventana, text="Cancelar", command=cancelar)
btn_cancelar.grid(row=6, column=1, padx=10, pady=10)

# Iniciar el bucle de la interfaz
ventana.mainloop()

