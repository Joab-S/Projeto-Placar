"""
* Código para criação da Tabela de Ranking e regitro de tempo da competição Line Follower
* RAITec / DTec
------------------------------ IDEIA GERAL DA TABELA FINAL ---------------------------
______________________________________________________________________________________
|                                     CLASSIFICAÇÃO                                   |
--------------------------------------------------------------------------------------
|  EQUIPES  |  CHECK 1  |  CHECK 2  |  CHECK 3  |  CHECK 4  |  ...  |  CHECK n_check  |
--------------------------------------------------------------------------------------
|  EQUIPE1  |  TEMPO 1  |  TEMPO 2  |  TEMPO 3  |  TEMPO 4  |  ...  |  TEMPO n_check  |
|  EQUIPE2  |  TEMPO 1  |  TEMPO 2  |  TEMPO 3  |  TEMPO 4  |  ...  |  TEMPO n_check  |
|    ...    |    ...    |    ...    |    ...    |    ...    |  ...  |       ...       |
|  EQP_Neqp |  CHECK 1  |  CHECK 2  |  CHECK 3  |  CHECK 4  |  ...  |  CHECK n_check  |
"""
import tkinter as tk
from tkinter import scrolledtext as sc
import tkinter.font as tkFont
import pandas as pd

class Configurar:
    def __init__ (self, master):
        #fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.master = master
        self.checks = tk.StringVar()
        self.eqps = []
        self.tela()
        self.clique = 0
    def iniciaTabela(self):
        """
        IMPLEMENTAR: colocar uma MessageBox caso inicie a tabela com informação faltante ou se um dos valores
        numéricos não correspondam a números inteiros
        """
        if self.clique == 0:
            self.tabela = tk.Toplevel(self.master)
            self.app = Tabela(self.tabela)
            self.app.framesTable()
            a, b = int(self.checks.get()), self.eqps
            dfr = self.app.criarDF(a, b)
            self.app.fila(b)
            c, d = self.app.criarDF(a, b, col = True), self.app.criarDF(a, b, lin = True)
            self.app.estruturaTabela(dfr, c, d, 45)
            self.app.gradeTable()
            self.clique = 1
    def tela(self):
        # Método que reúne todos os outros da classe Configurar 
        self.frames_tela()
        self.master.title("Configurações")
        self.master.geometry ("345x200")
        self.n_checkpoints()
        self.nomear_equipes()
        self.exibir_nomes()
        self.botoes()
        self.gradeConf()
    def botoes(self):
        self.botao1 = tk.Button(self.frameB, text = "Iniciar Tabela", width = 20, command = self.iniciaTabela)
        self.botao2 = tk.Button(self.frameC, text = "Add", width = 7, command = self.add)
        self.botao3 = tk.Button(self.frameC, text = "Del", width = 7, command = self.delete)
    def nomear_equipes(self):
        """
        Cria caixa de entrada para receber o nome das equipes que serão registradas 
        """
        self.txt_equipe = tk.Label(self.frameC, text = 'Nomes das Equipes')
        self.nomes = tk.Entry(self.frameC)
    def n_checkpoints(self):
        """
        Cria caixa de entrada para receber o número de checkpoints na pista
        """
        self.txt_check = tk.Label(self.frameC, text = "N° de Checkpoints: ")
        self.n_check = tk.Entry(self.frameC, textvariable = self.checks, width = 7)
    def exibir_nomes(self):
        """
        Exibe o nome das equipes registradas na competição
        """
        self.list_equipes = tk.Listbox(self.frameD, bg = "white")
        self.scroll = tk.Scrollbar(self.frameD, orient = tk.VERTICAL, command = self.list_equipes.yview)
        self.list_equipes.configure(yscrollcommand = self.scroll)
    def add(self):
        """
        Adiciona o nome digitado a lista de equipes registradas
        """
        self.nome = self.nomes.get()
        self.eqps.append(self.nome)
        self.list_equipes.insert(tk.END, self.nome)
        self.nomes.delete(0, tk.END)
    def delete (self):
        """
        Deleta a última equipe registrada
        """
        del(self.eqps[-1])
        self.list_equipes.delete(tk.END)
    def frames_tela(self):
        """
        Os frames são usados para criar 'quadros' separados na tela, para melhor organizar a tela
        """
        self.frameA = tk.Frame(self.master)
        self.frameB = tk.Frame(self.master)
        self.frameC = tk.Frame(self.frameA)
        self.frameD = tk.Frame(self.frameA)
    def gradeConf(self):
        """
        Método onde é definida a posição de cada elemento visível na tela de configurações 
        """
        self.frameA.grid(row = 0)
        self.frameB.grid(row = 1)
        self.frameC.grid(row = 0, column = 0)
        self.frameD.grid(row = 0, column = 1)
        self.botao1.grid(row = 1)
        self.botao2.grid(row = 5, column = 1)
        self.botao3.grid(row = 6, column = 1)
        self.txt_check.grid(row = 1, column=0)
        self.n_check.grid(row = 1, column=1)
        self.txt_equipe.grid(row = 4, column = 0)
        self.nomes.grid(row = 5, column = 0)
        self.list_equipes.grid(row = 0, column = 0)
        self.scroll.grid(row = 0, column = 1, sticky = "NS")    

class Tabela(Configurar):
    def __init__(self, master):
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=15)
        self.fontCLASS = tkFont.Font(family="Lucida Grande", size=30)
        self.master = master
        super().__init__(master)
        
    def tela(self):
        self.master.title("Raking Dtec")
        #self.master.minsize(width = 1000, height = 600)
        #self.estruturaTabela(a)
        #self.criarTabela()
        #self.registrarTempo()
        #self.comparaTempo()
        #self.mudarOrdem()
    def criarDF(self, a = 0, b = 0, col = False, lin = False):
        """
        Cria um dataframe com a biblioteca pandas
        """
        self.a, self.b = a, b
        COLUNAS = ['INÍCIO']
        for i in range(1, self.a+1):
            COLUNAS.append('CHECK%d'%i)
        COLUNAS.append('FINAL')
        if col == True:
            return COLUNAS
        if lin == True:
            return b
        self.df = pd.DataFrame(columns = COLUNAS, index = b)
        return self.df
        print(self.df)
        
    def estruturaTabela(self, df, col, lin, tempo):
        """
        Método responsável por montar a estrutura da tabela baseado no número de competidores registrados
        e número de checkpoints dispostos na pista
        """
        self.txtClass = tk.Label (
            self.frameTema,
            text = "CLASSIFICAÇÃO",
            bg = "dark orange",
            font = self.fontCLASS)
        self.txtClass.pack()
        t = 8
        for m, n in zip (lin, range(len(lin))):
            frameTsu = tk.Frame(self.frameTema2, relief = tk.RAISED)
            frameTsu.grid(row = n+1, column = 0)
            txtCheck = tk.Label (frameTsu, text = m, width = t, bg = "dark orange", font=self.fontStyle)
            txtCheck.grid()
            for i, j in zip (col, range(len(col))):           
                frameTsub = tk.Frame(self.frameTema2, relief = tk.RAISED, borderwidth = 1)
                frameTsub2 = tk.Frame(self.frameTema2, relief = tk.RAISED, borderwidth = 1)
                tx = tk.Label (frameTsub2, text = i, width = t, bg = "dark orange", font=self.fontStyle)
                txtCheck = tk.Label (frameTsub, text = '', width = t, bg = "pink", font=self.fontStyle)
                frameTsub.grid(row = n+1, column = j+1)
                frameTsub2.grid(row = 0, column = j+1)
                tx.pack()
                txtCheck.pack()
                
                

##    def registrarTempo(self):
##        pass
##        """
##        Aqui, os registros de tempo recebidos do Arduino/Raspberry de cada checkpoint serão colocados na tabela completando
##        a linha referente ao carro que está correndo na vez. 
##        """
##    def comparaTempo(self):
##        pass
##        """
##        A cada checkpoint, ou seja, a cada registro de tempo, o método comparaTempo é usado para comparar o valor do checkpoint
##        atual da equipe na pista com os valores de tempo no mesmo checkpoint dos outros competidores.
##        """
##    def mudarOrdem(self):
##        pass
##        """
##        Depois de comparar o tempo e dizer quem é menor ou maior pra determinado checkpoint, o método mudarOrdem muda a ordem
##        no placar, alterando as posições no ranking de acordo com o menor tempo.
##        """
    def framesTable(self):
        """
        Os frames são usados para criar 'quadros' separados na tela, para melhor organizar a tabela
        """
        self.frame1 = tk.Frame(self.master, relief = tk.RAISED, borderwidth = 1) # Lado esquerdo da tela
        self.frame2 = tk.Frame(self.master, relief = tk.RAISED, borderwidth = 1) # Lado Direito da tela
        self.frameTema = tk.Frame(self.frame1, relief = tk.RAISED) # Texto 'CLASSIFICAÇÃO' no topo
        self.frameTema2 = tk.Frame(self.frame1, relief = tk.RAISED) # 
        self.frameFila = tk.Frame(self.frame2) # Frame que vai conter a fila de competidores
    def gradeTable(self):
        """
        
        """
        self.frame1.grid(row = 0, column = 0)
        self.frame2.grid(row = 0, column = 1)
        self.frameTema.grid(row = 0, sticky = "nsew")
        self.frameTema2.grid(row = 1, column = 0)
        self.frameFila.grid()
    def fila (self, a):
        for i, j in zip(a, range(len(a))):
            self.frameF = tk.Frame(self.frameFila, relief = tk.RAISED, borderwidth = 1)
            self.fila = tk.Label(self.frameF, text = i, width = 10, font=self.fontStyle)
            self.frameF.grid(sticky = "nsew")
            self.fila.grid(row = j)
        """
        Aqui haverá uma coluna cujas linhas apresentam, na ordem exibida, o nome do competidor atual, seguido
        pelo nome das próximas equipes a competir, tal qual uma fila.
        """


def main():
    root = tk.Tk()
    app = Configurar(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
