import tkinter as tk

root= tk.Tk()
root.title("Mi app")
root.geometry("500x300")
root.resizable(False, False)

label=tk.Label(root, text="Bienvenido a mi aplicación", font=("Arial", 16), fg="black", bg="skyblue")
label.pack(pady=10)

texto=tk.Text(root, height=5, width=40)
texto.insert("1.0", "Escribe aquí tu texto...")
texto.pack(pady=10)

def leer_texto():
    print("Contenido:", texto.get("1.0", "end"))

boton=tk.Button(root, text="Leer texto", command=leer_texto, font=("Arial", 12))
boton.pack()

def cerrar():
    print("Cerrando la aplicación...")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", cerrar)

root.mainloop()