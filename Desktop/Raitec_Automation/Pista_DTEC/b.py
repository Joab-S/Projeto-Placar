import tkinter as tk

tela = tk.Tk()
texto = 'você clicou no botão'
label = tk.Label(text = "Botão sem clique")
cont = 0
def add():
    cont += 1
    label = tk.Label(text = texto)   

boton = tk.Button(text = "add", command = add())

boton.grid()
label.grid(column = 1)

tk.mainloop()

