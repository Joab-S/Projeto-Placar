"""
* Código para criação da Tabela de Ranking e regitro de tempo da competição Line Follower
* RAITec / DTec
* Feito por: Joab Silva (Joab-S)

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
try:
    import tkinter as tk
    from tkinter import scrolledtext as sc
    import tkinter.font as tkFont
except:
    import Tkinter as tk
    from Tkinter import scrolledtext as sc
    import Tkinter.font as tkFont 
import pandas as pd
import random as rd
import serial
import threading
import time

#ser = serial.Serial('COM17', 9600)
ser = serial.Serial('/dev/rfcomm0', 9600)
root = tk.Tk()
            
class Configurar:
    def __init__ (self, master):
        self.master = master
        self.checks = tk.StringVar()
        self.eqps = []
        self.res, self.clique = False, False
        self.contClique, self.posicao = 0, -1
    def iniciaTabela(self):
        self.tabela = tk.Toplevel(self.master)
        self.checkpts, self.equipes, self.resultadoIniciar = int(self.checks.get()), self.eqps, self.res
        self.app2 = Tabela(self.tabela, self.checkpts, self.equipes)
        self.app2.telaTable()
    def telaConf(self):
        # Método que reúne todos os outros da classe Configurar 
        self.frames_tela()
        self.master.title("Configurações")
        self.n_checkpoints()
        self.nomear_equipes()
        self.exibir_nomes()
        self.botoes()
        self.controleArduino()
        self.gradeConf()
    def botoes(self):
        self.botao1 = tk.Button(self.frameB, text = "Iniciar Tabela", width = 20, command = self.iniciaTabela)
        self.botao2 = tk.Button(self.frameC, text = "Add", width = 7, command = self.add)
        self.botao3 = tk.Button(self.frameC, text = "Del", width = 7, command = self.delete)
        self.botaoIniciarCorrida = tk.Button(self.frameMasterDireito, text = "Iniciar Corrida", width = 20, command = self.cliqueB)
   
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
        self.frameMasterEsquerdo = tk.Frame(self.master)
        self.frameMasterDireito = tk.Frame(self.master)
        self.frameA = tk.Frame(self.frameMasterEsquerdo)
        self.frameB = tk.Frame(self.frameMasterEsquerdo)
        self.frameC = tk.Frame(self.frameA)
        self.frameD = tk.Frame(self.frameA)
        self.frameIniciaCorrida = tk.Frame(self.frameMasterDireito)
    def gradeConf(self):
        """
        Método onde é definida a posição de cada elemento visível na tela de configurações 
        """
        self.frameMasterEsquerdo.grid(row = 0, column = 0)
        self.frameMasterDireito.grid(row = 0, column = 1)
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
        self.TXT_INICIA_CORRIDA.grid(row = 0)
        self.botaoIniciarCorrida.grid(row = 1)
        self.cliques.grid(row = 2)

    def controleArduino(self):
        self.TXT_INICIA_CORRIDA = tk.Label (self.frameMasterDireito, text = 'Iniciar corrida?')
        self.cliques = tk.Label(self.frameMasterDireito, text = self.contClique)
        
    def resultado(self):
        self.res = True
        if self.res == True:
            self.contClique += 1
            self.posicao += 1
            self.cliques['text'] = self.contClique
            sim = ser.write(b'Sim')
            self.app2.depoisDaOrdemArduino(self.posicao)

    def cliqueB(self):
        txt = str(ser.readline())[2:-3]
        if txt == 'Iniciar corrida?':
            print('res: ', self.res)
            self.resultado()
            print('res: ', self.res, 'clique: ', self.clique)
            self.clique = False

    def podeIniciar(self):
        return self.res

class Tabela(Configurar):
    def __init__(self, master2, nCHECK, nEQP):
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=15)
        self.fontCLASS = tkFont.Font(family="Lucida Grande", size=30)
        self.master2 = master2
        self.n_checkpts, self.nome_equipes = nCHECK, nEQP
        self.dfR = self.criarDF(self.n_checkpts, self.nome_equipes)
        self.tempo, self.tempoMarcado = 0, 500
        self.NOME_COLUNAS = self.dfR.columns
        self.NOME_EQUIPES = self.dfR.index
        super().__init__(master2)
        self.iniciaCorrida = self.podeIniciar()
        
    def telaTable(self):
        self.master2.title("Raking Dtec")
        self.framesTable()
        self.estruturaTabela(self.dfR, self.NOME_COLUNAS, self.NOME_EQUIPES)
        self.gradeTable()
        self.master2.after(0, self.repete)
        #self.master.minsize(width = 1000, height = 600)
        
    def criarDF(self, check, equipes):
        """
        Cria um dataframe com a biblioteca pandas
        """
        COLUNAS = []
        for i in range(1, check+1):
            COLUNAS.append('Check %d'%i)
        COLUNAS.append('Final  ')
        COLUNAS.append('Total  ')
        df = pd.DataFrame(columns = COLUNAS, index = equipes)'
                
        return df

    def colunas_equipes(self, df):
        """
        Retorna duas listas que mudam de acordo com a columns e index
        do dataframe, contendo o nome das colunas e o nome das linhas 
        """
        self.NOME_COLUNAS = df.columns
        self.NOME_EQUIPES = df.index
        
    def estruturaTabela(self, df, col, lin):
        """
        Método responsável por montar a estrutura da tabela baseado no número de competidores registrados
        e número de checkpoints dispostos na pista
        """
        t = 8
        self.txtClass = tk.Label (
            self.frameTema,
            text = "CLASSIFICAÇÃO",
            bg = "dark orange",
        font = self.fontCLASS)
        self.txtClass.pack()
        self.listEQP, self.listPONTOS = [], []
        for m, n in zip (lin, range(len(lin))):
            frameTsu = tk.Frame(self.frameTema2, relief = tk.RAISED, borderwidth = 1)
            frameTsu.grid(row = n+1, column = 0)
            self.txtEQP = tk.Label (frameTsu, text = '', width = t, bg = "dark orange", font=self.fontStyle)
            self.txtEQP.pack()
            self.listEQP.append(self.txtEQP)
            for i, j in zip (col, range(len(col))):
                frameTsub = tk.Frame(self.frameTema2, relief = tk.RAISED, borderwidth = 1)
                frameTsub2 = tk.Frame(self.frameTema2, relief = tk.RAISED, borderwidth = 1)
                tx = tk.Label (frameTsub2, text = i, width = t, bg = "dark orange", font=self.fontStyle)
                self.txtCheck = tk.Label (frameTsub, text = '', width = t, bg = "pink", font=self.fontStyle)
                frameTsub.grid(row = n+1, column = j+1)
                frameTsub2.grid(row = 0, column = j+1)
                tx.pack()
                self.listPONTOS.append(self.txtCheck)
                self.txtCheck.pack()

    def registrarRodada(self, df, check, equipe, tempo):
        """
        Registra o valor do tempo dentro da celula do dataframe referente ao
        nome da linha e coluna responsável
        """
        df.loc[equipe, check] = tempo
        df.sort_values(check)

    def ordenarDataframe(self, df, coluna):
        """
        Ordena o dataframe por ordem crescente
        """
        dfrOrganizado = df.sort_values(coluna)
        
        for m in (dfrOrganizado.index):
            for n in (dfrOrganizado.columns):
                if type(dfrOrganizado.loc[m, n]) == float:
                    dfrOrganizado.loc[m, n] = ''
        
        return dfrOrganizado
    
    def atualizarTabela(self, df, col, lin):
        cont = 0
        for m, n in zip (lin, range(len(lin))):
            self.listEQP[n]['text'] = m
            for i, j in zip (col, range(len(col))):
                self.listPONTOS[cont]['text'] = df.loc[m, i]
                cont += 1

    def chegadaTempo(self):
        """o tempo vem do arduino com o formato CHECK01 tempo, usa split() e separa entre check1 e tempo"""
        registro = str(ser.readline()).split("->")
        self.tempo = registro[1][0:-5]
        self.marcador = registro[0][2:9]

    def framesTable(self):
        """Os frames são usados para criar 'quadros' separados na tela, para melhor organizar a tabela"""
        self.frame1 = tk.Frame(self.master2, relief = tk.RAISED, bg = "dark orange", borderwidth = 1) # Lado esquerdo da tela
        self.frame2 = tk.Frame(self.master2, relief = tk.RAISED, bg = "dark orange", borderwidth = 1) # Lado Direito da tela
        self.frameTema = tk.Frame(self.frame1) # Texto 'CLASSIFICAÇÃO' no topo
        self.frameTema2 = tk.Frame(self.frame1, relief = tk.RAISED) # 
        #self.frameFila = tk.Frame(self.frame2) # Frame que vai conter a fila de competidores

    def gradeTable(self):
        """
        
        """
        self.frame1.grid(row = 0, column = 0)
        self.frame2.grid(row = 0, column = 1)
        self.frameTema.grid(row = 0)
        self.frameTema2.grid(row = 1, column = 0)
        #self.frameFila.grid() 
 
    def competidorAtual (self, primeiro, i):
        return primeiro[i]
    
    def reiniciarContagem(self):
        while ser.readline() != b'START\r\n':
            ser.readline()

    def depoisDaOrdemArduino(self, numeroPosicao):
            self.numPos = numeroPosicao
            if ser.readline() == b'\r\r\n':
                print('')
                if ser.readline() == b'Sim\r\n':
                    print('Sim')
                    if ser.readline() == b'Esperando o carrinho.\r\n':
                        print('Esperando o carrinho.')
                        if ser.readline() == b'START\r\n':
                            print('START')
                            n = 0
                            for n in range(len(self.NOME_COLUNAS)):#while n < len(self.NOME_COLUNAS):
                                self.chegadaTempo()
                                self.tempoMarcado = self.tempo
                                posicaoCH = self.marcador
                                corredorAtual = self.competidorAtual(self.nome_equipes, self.numPos)
                                self.registrarRodada(self.dfR, posicaoCH, corredorAtual, self.tempoMarcado)
                                dfrOrg = self.ordenarDataframe(self.dfR, posicaoCH)
                                self.colunas_equipes(dfrOrg)
                                #print(dfrOrg)
                                self.atualizarTabela(dfrOrg, self.NOME_COLUNAS, self.NOME_EQUIPES)
                                root.update()
            # if ser.readline() == b'Final de percurso!\r\n':
            #    print('Final de percurso!')
            #    if str(ser.readline())[2:13] == 'Tempo final':
            #        print('Tempo final')
                    self.res = False
                    pode = False

    def repete(self):
        #print('AGUARDANDO...')
        self.master2.after(self.tempoMarcado, self.repete)

def main():

    app = Configurar(root)
    app.telaConf()
    while True:
        root.update_idletasks()
        root.update()
    #root.mainloop()
    
    
if __name__ == '__main__':
    main()
