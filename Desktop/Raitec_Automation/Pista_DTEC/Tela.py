"""
   * Código para apresentação visual de ranking de competidores
     baseado no tempo de corrida

   * Feito por: Joab da Silva
   * RAITec / Dtec

"""

"""--------IMPORTAÇÕES DE BIBLIOTECAS NECESSÁRIAS----------"""

import tkinter as tk    

"""------------------VARIÁVEIS GLOBAIS --------------------"""

n_comp = 4                      # Número de competidores
n_cp   = 3                    # Número de checkpoints
lin = []
col = []

for i in range(n_comp + 1):
    lin.append(i)
for j in range(n_cp   + 2):
    col.append(j)

"""-------------------------------------------------------"""

tela = tk.Tk()
tela.title("PLACAR DTEC - CONFIRA SEU RANKING")
tela.rowconfigure   (lin, minsize=30)
tela.columnconfigure(col, minsize=50)

"""--------------------------------------------------------"""

placar = tk.Label(text = "PLACAR", fg = "black", bg = "dark orange")
placar.grid(row = 0, column = 0, columnspan = len(col)+2, sticky = "wens")

"""---------------------------------------------------------"""

txt_ordem = tk.Label(text = "ORDEM", bg = "dark orange")
txt_ordem.grid(row = 1, column=0, sticky = "nsew")

for i in range(1, len(lin)):
    ordem = tk.Label(text = str(i) + "°", bg = "dark orange")
    ordem.grid(row=i+1, column=0, sticky = "nsew")

"""---------------------------------------------------------"""

txt_equipe = tk.Label(text = "NOME DA EQUIPE", bg = "gray60")
txt_equipe.grid(row = 1, column=1, sticky = "nsew")

"""---------------------------------------------------------"""

txt_start = tk.Label(text = "START", bg = "gray60")
txt_start.grid(row = 1, column=2, sticky = "nsew", ipadx = 20)

"""---------------------------------------------------------"""

for i in range(1, n_cp+1):
    txt_check = tk.Label(text = "CHECKPOINT " + str(i), bg = "gray60")
    txt_check.grid(row = 1, column=i+2, sticky = "nsew")

"""---------------------------------------------------------"""

txt_finish = tk.Label(text = "FINISH", bg = "gray60")
txt_finish.grid(row = 1, column = len(col)+1, sticky = "nsew", ipadx = 20)

"""---------------------------------------------------------"""

for j in range (n_comp):
    for i in range (len(col)):
        pontos = tk.Label(text = "t = " + str(i), bg = "peach puff")
        pontos.grid(row=j+2, column=i+2, sticky = "nsew")

for j in range (n_comp):
    nome = input("Digite o nome da equipe:")
    nome_equipe = tk.Label(text = nome, bg = "pink")
    nome_equipe.grid(row = j+2, column=1, sticky = "nsew")
    


"""for i in range(n_cp):
    for j in range(n_comp):
        tabela = tk.Frame( master = tela, relief = tk.RAISED,borderwidth=1)
        tabela.grid(row=i, column=j)
        label = tk.Label(master=tabela, text=f"Row {i}\nColumn {j}")
        label.pack()"""


tela.mainloop()
