import tkinter as tk

class Tabela(): #Configurar
    def __init__(self, master):
        #super().__init__(master)
        self.master = master
        self.tela()
    def tela(self):
        self.framesTable()
        self.master.title("Raking Dtec")
        self.master.minsize(width = 1000, height = 600)
        self.estruturaTabela()
        self.criarTabela()
        self.gradeTable()
        self.registrarTempo()
        self.comparaTempo()
        self.mudarOrdem()
    def estruturaTabela(self):
        self.txt_placar = tk.Label (self.frame1, text = "PLACAR")
    def criarTabela(self):
        pass
    def comparaTempo(self):
        pass
    def mudarOrdem(self):
        pass
    def registrarTempo(self):
        pass
    def framesTable(self):
        self.frame1 = tk.Frame(self.master)
        self.frame2 = tk.Frame(self.master)
        self.frame3 = tk.Frame(self.master)
    def gradeTable(self):
        self.frame1.grid(row = 0)
        self.frame2.grid()
        self.frame3.grid()
        self.txt_placar.grid()
        
    
def main():
    root = tk.Tk()
    app = Tabela(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
