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
from flask import Flask , render_template
from threading import Thread as Th
import pandas as pd
import numpy as np
import random as rd
import serial
import sys 
import trace
import time

#ser = serial.Serial('COM17', 9600)
ser = serial.Serial('/dev/ttyACM0', 9600)

# inicio site -------------
site=Flask(__name__)

@site.route ('/')  
def table ():
    headings = COLUNAS
    data = lista_das_listas
    return render_template("tabela.html" , headings = headings , data = data)

#def compilar():
    #site.run()
thread_SiteRun = Th(target = site.run)
# fim site -------------

app = tk.Tk()

num_checks = tk.StringVar()
equipes    = []
contClique, posicao = 0, -1
data_frame, lista_das_listas = '', []
COLUNAS = []

def criarDF(check, equipes):
    """
    Cria um dataframe com a biblioteca pandas
    """
    global COLUNAS
    for i in range(1, check+1):
        COLUNAS.append('Check %d'%i)
    COLUNAS.append('Final  ')
    df = pd.DataFrame(columns = COLUNAS, index = equipes)

    return df

def registrarRodada(df, check, equipe, tempo):
    """
    Registra o valor do tempo dentro da celula do dataframe referente ao
    nome da linha e coluna responsável
    """
    df.loc[equipe, check] = tempo
    df.sort_values(check)

def ordenarDataframe(df, coluna):
    """
    Ordena o dataframe por ordem crescente
    """
    dfrOrganizado = df.sort_values(coluna)
        
    for m in (dfrOrganizado.index):
        for n in (dfrOrganizado.columns):
            if type(dfrOrganizado.loc[m, n]) == float:
                dfrOrganizado.loc[m, n] = ''
        
    return dfrOrganizado

def preencheTabela(posicao):
    if ser.readline() == b'\r\r\n':
        print('')
        if ser.readline() == b'Sim\r\n':
            print('Sim')
            if ser.readline() == b'Esperando o carrinho.\r\n':
                print('Esperando o carrinho.')
                if ser.readline() == b'START\r\n':
                    print('START')
                    n = 0
                    for n in range(len(COLUNAS)):#while n < len(self.NOME_COLUNAS):
                        registro = str(ser.readline()).split("->")
                        tempo = registro[1][0:-5]
                        marcador = registro[0][2:9]
                        corredorAtual = equipes[posicao]
                        registrarRodada(data_frame, marcador, corredorAtual, tempo)
                        dfrOrg = ordenarDataframe(data_frame, marcador)
                        NOME_COLUNAS = dfrOrg.columns
                        NOME_EQUIPES = dfrOrg.index
                        print(dfrOrg)
                        global lista_das_listas
                        lista_das_listas = dfrOrg.reset_index().values.tolist()
# Frames ------------------------------------

frameMasterEsquerdo = tk.Frame(master = app)
frameMasterDireito  = tk.Frame(master = app)
frameA = tk.Frame(master = frameMasterEsquerdo)
frameB = tk.Frame(master = frameMasterEsquerdo)
frameC = tk.Frame(master = frameA)
frameD = tk.Frame(master = frameA)

app.title("Configurações")

#Labels ------------------------------------
txt_check = tk.Label(master = frameC,
                     text = "N° de Checkpoints: ")

n_check = tk.Entry(master = frameC,
                   textvariable = num_checks, width = 7)

txt_equipe = tk.Label(master = frameC,
                      text = 'Nomes das Equipes')

nomes = tk.Entry(master = frameC)

list_equipes = tk.Listbox(master = frameD, bg = "white")
scroll = tk.Scrollbar(master = frameD,
                      orient = tk.VERTICAL,
                      command = list_equipes.yview)

list_equipes.configure(yscrollcommand = scroll)

TXT_INICIA_CORRIDA = tk.Label (master = frameMasterDireito,
                               text = 'Iniciar corrida?')

cliques = tk.Label(master = frameMasterDireito, text = contClique)
        
#funções ------------------------------------
def adicionar():
    global nomes
    nome = nomes.get()
    equipes.append(nome)
    list_equipes.insert(tk.END, nome)
    nomes.delete(0, tk.END)

def delete ():
    del(equipes[-1])
    list_equipes.delete(tk.END)

def iniciarCorrida():
    global contClique, posicao
    txt = str(ser.readline())[2:-3]
    if txt == 'Iniciar corrida?':
        contClique += 1
        posicao += 1
        cliques['text'] = contClique
        ser.write(b'Sim')
        preencheTabela(posicao)

def iniciarTabela():
    global num_checks, data_frame, equipes
    c = int(num_checks.get())
    data_frame = criarDF(c, equipes)
    thread_SiteRun.start()
    
#Botões ------------------------------------
botao1 = tk.Button(master = frameB,
                   text   = "Iniciar Tabela",
                   width  = 20,
                   command = iniciarTabela
                   #command = compilar
                   #command = thread_SiteRun.start
                   )

botao2 = tk.Button(master = frameC, text = "Add",
                   width = 7, command = adicionar)

botao3 = tk.Button(master = frameC, text = "Del",
                   width = 7, command = delete)

botaoIniciarCorrida = tk.Button(master = frameMasterDireito,
                                text = "Iniciar Corrida",
                                width = 20,
                                command = iniciarCorrida)

# Renderização ------------------------------------
frameMasterEsquerdo.grid(row = 0, column = 0)
frameMasterDireito.grid(row = 0, column = 1)
frameA.grid(row = 0)
frameB.grid(row = 1)
frameC.grid(row = 0, column = 0)
frameD.grid(row = 0, column = 1)
botao1.grid(row = 1)
botao2.grid(row = 5, column = 1)
botao3.grid(row = 6, column = 1)
txt_check.grid(row = 1, column=0)
n_check.grid(row = 1, column=1)
txt_equipe.grid(row = 4, column = 0)
nomes.grid(row = 5, column = 0)
list_equipes.grid(row = 0, column = 0)
scroll.grid(row = 0, column = 1, sticky = "NS")
TXT_INICIA_CORRIDA.grid(row = 0)
botaoIniciarCorrida.grid(row = 1)
cliques.grid(row = 2)

while True:
    app.update_idletasks()
    app.update()   
