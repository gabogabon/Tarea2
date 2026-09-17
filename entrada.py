import tkinter as tk

root= tk.Tk()
root.title("Entrada de texto")
root.geometry("500x300")
root.resizable(False, False)

label=tk.Label(root, text="Bienvenido a mi aplicación", font=("Arial", 16), fg="black", bg="yellow")
label.pack(pady=10)

entry=tk.Entry(root, show="*")
entry.pack(pady=10)

def mostrar_texto():
    print("Texto ingresado:", entry.get())

boton=tk.Button(root, text="Mostrar texto", command=mostrar_texto, font=("Arial", 12))
boton.pack()

def cerrar():
    print("Cerrando la aplicación...")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", cerrar)

root.mainloop()