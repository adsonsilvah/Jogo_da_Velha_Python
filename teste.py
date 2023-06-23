import numpy as np
from tkinter import *
import random

def verifica_espaco_vazio():
     
     espacos = 9

     for linhas in range(3):
          for colunas in range(3):
               if tabuleiro[linhas][colunas]['text'] != '':
                    espacos-=1

     if espacos == 0:
            return False
     else:
            return True

def troca_jogador(linha, coluna):
    pass
def verifica_vitoria():
     pass
def novo_jogo():
    pass
def revache():
     pass

janela = Tk()
janela.title('Jogo da Velha')
jogadores = ["Jogador X"," jogador O"]
alternajogador = random.choice(jogadores)

tabuleiro = np.empty((3, 3), dtype=object)

label = Label(text='Vez do '+ alternajogador)
label.pack(side='top')

reset_button = Button(text="Revache", command=revache)
reset_button.pack(side="bottom")

reset_button = Button(text="Novo jogo", command=novo_jogo)
reset_button.pack(side="bottom")

frame = Frame(janela)
frame.pack()

for linha in range(3):
    for coluna in range(3):
        tabuleiro[linha][coluna] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=linha, column=coluna: troca_jogador(row,column))
        tabuleiro[linha][coluna].grid(row=linha,column=coluna)
        
janela.mainloop()
