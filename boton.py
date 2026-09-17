import tkinter as tk

root= tk.Tk()
root.title("Mi primer boton")
root.geometry("500x300")
root.resizable(False, False)

label=tk.Label(root, text="Bienvenido a mi aplicación", font=("Arial", 16), fg="black", bg="yellow")
label.pack(pady=10)

def saludo():
    etiqueta.config(text= "Hola, bienvenido a mi aplicación!")

boton=tk.Button(root, text="Click aquí", command=saludo, bg="brown", fg="white", font=("Arial", 12))
boton.pack(pady=10)

etiqueta=tk.Label(root, text="", font=("Arial", 12), fg="black", bg="lightgray")
etiqueta.pack(pady=10)

def cerrar():
    print("Cerrando la aplicación...")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", cerrar)

root.mainloop()