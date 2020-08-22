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
import pandas as pd

class Configurar:
    def __init__ (self, master):
        self.master = master
        self.checks = tk.StringVar()
        self.eqps = []
        self.tela()
    def iniciaTabela(self):
        """
        IMPLEMENTAR: colocar uma MessageBox caso inicie a tabela com informação faltante ou se um dos valores
        numéricos não correspondam a números inteiros
        """
        self.tabela = tk.Toplevel(self.master)
        self.app = Tabela(self.tabela)
        self.app.framesTable()
        a, b = int(self.checks.get()), self.eqps
        self.app.criarDF(a, b)
        self.app.estruturaTabela(a, b)
        self.app.gradeTable()
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
    def criarDF(self, a = 0, b = 0):
        """
        Cria um dataframe com a biblioteca pandas
        """
        self.a, self.b = a, b
        COLUNAS = ['INÍCIO']
        for i in range(1, self.a+1):
            COLUNAS.append('CHECK%d'%i)
        COLUNAS.append('FINAL')
        df = pd.DataFrame(columns = COLUNAS, index = b)
        print(df)
    def estruturaTabela(self, a, b):
        """
        Método responsável por montar a estrutura da tabela baseado no número de competidores registrados
        e número de checkpoints dispostos na pista
        """
        self.txtClass = tk.Label (self.frameTema, text = "CLASSIFICAÇÃO", bg = "dark orange")
        self.txtClass.grid(row = 0, sticky = "nsew")
        for i in range(1, a+1):
            """
            Laço que cria a linha das colunas 
            """
            self.frameTsub = tk.Frame(self.frameTema2, relief = tk.RAISED, borderwidth = 1)
            self.frameTsub.grid(row = 0, column = i)
            self.txtCheck = tk.Label (self.frameTsub, text = i, bg = "orange")
            self.txtCheck.grid(row = 0, column = i)
        for i, j in zip(b, range(len(b))):
            """
            Laço que cria a coluna das linhas 
            """
            self.frameOrd = tk.Frame(self.frameCorpo, relief = tk.RAISED, borderwidth = 1)
            self.frameOrd.grid(row = j, column = 0)
            self.tx = tk.Label (self.frameOrd, text = i, bg = "pink")
            self.tx.grid(row = j, column = 0)      
##    def criarTabela(self):
##        pass
##        """
##        Nesse método será criada as linhas e colunas que conterão os registros de tempo dos competidores
##        """
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
        self.frame1 = tk.Frame(self.master, relief = tk.RAISED) # Lado esquerdo da tela
        self.frame2 = tk.Frame(self.master, relief = tk.RAISED) # Lado Direito da tela
        self.frameTema = tk.Frame(self.frame1, relief = tk.RAISED, borderwidth = 1) # Texto 'CLASSIFICAÇÃO' no topo
        self.frameTema2 = tk.Frame(self.frameTema, relief = tk.RAISED, borderwidth = 1) # 
        self.frameCorpo = tk.Frame(self.frameTema, relief = tk.RAISED, borderwidth = 1) # 
        self.frameValor = tk.Frame(self.frameCorpo, relief = tk.RAISED, borderwidth = 1) # 
        self.frameFila = tk.Frame(self.frame2) # Frame que vai conter a fila de competidores
    def gradeTable(self):
        """
        
        """
        self.frame1.grid(row = 0, column = 0)
        self.frame2.grid(row = 0, column = 1)
        self.frameTema.grid(row = 0, sticky = "nsew")
        self.frameTema2.grid(row = 1)
        self.frameCorpo.grid(row = 2)
        self.frameValor.grid(row = 0, column = 1)
        self.frameFila.grid()
        self.fila = tk.Label(self.frame2, text = "Fila").grid(row=0)
    def fila (self):
        pass
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
