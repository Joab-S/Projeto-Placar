import tkinter as tk
from tkinter import scrolledtext as sc

class Configurar:
    def __init__ (self, master):
        self.master = master
        self.tela()
    def iniciaTabela(self):
        self.tabela = tk.Toplevel(self.master)
        self.app = Tabela(self.tabela)
    def tela(self):
        self.frames_tela()
        self.master.title("Configurações")
        self.master.geometry ("400x200")
        self.n_competidores()
        self.nomear_equipes()
        self.n_checkpoints()
        self.botoes()
        self.gradeConf()
    def botoes(self):
        self.botao1 = tk.Button(self.frame2, text = "Concluído", width = 25, command = self.iniciaTabela)
    def nomear_equipes(self):
        self.txt_equipe = tk.Label(self.frame1, text = 'Nomes das Equipes')
        self.nomes = sc.ScrolledText(self.frame1,width=20,height=4)
    def n_competidores(self):
        self.txt_comp = tk.Label(self.frame1, text = 'Número de Competidores')
        self.n_comp = tk.Entry(self.frame1)
    def n_checkpoints(self):
        self.txt_check = tk.Label(self.frame1, text = "Número de Checkpoints")
        self.n_check = tk.Entry(self.frame1)
    def frames_tela(self):
        self.frame1 = tk.Frame(self.master)
        self.frame2 = tk.Frame(self.master)
    def gradeConf(self):
        self.frame1.grid(row = 0)
        self.frame2.grid(row = 1)
        self.botao1.grid()
        self.txt_equipe.grid(row = 0, column = 1)
        self.nomes.grid(row = 1, column = 1)
        self.txt_comp.grid(row = 0)
        self.n_comp.grid(row = 1)
        self.txt_check.grid(row = 2)
        self.n_check.grid(row = 3)
        
class Tabela(Configurar):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
    def comparaTempo(self):
        pass
    def mudarOrdem(self):
        pass
    def tela(self):
        self.framesTable()
        self.master.title("Raking Dtec")
        self.master.minsize(width = 1000, height = 600)
    def registrarTempo(self):
        pass
    def gradeTable(self):
        pass
    def framesTable(self):
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        
def main():
    root = tk.Tk()
    app = Configurar(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
