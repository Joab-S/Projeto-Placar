import tkinter as tk
import random

simu_tempo = ['01:02','01:50','01:17','01','','','','','','','']
comp, pontos = 4, []
window = tk.Tk()

def comparar(a, b):
    pass
def receber(a, b):
    pass

for i in range(comp):
    for j in range(5):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text = 'bol',width=10, height = 2)
        
window.mainloop()


