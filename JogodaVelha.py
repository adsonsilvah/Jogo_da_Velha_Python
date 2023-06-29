import numpy as np
from tkinter import *

def troca_jogador(row, column):
     
     global jogadorAtual

     if tabuleiro[row][column]['text'] == "" and verifica_vitoria() is False:

        if jogadorAtual == jogadores[0]:

            tabuleiro[row][column]['text'] = jogadorAtual

            if verifica_vitoria() is False:
                jogadorAtual = jogadores[1]
                label.config(text=('Vez do jogador '+jogadores[1]))

            elif verifica_vitoria() is True:
                label.config(text=('Jogador '+jogadores[0]+ ' ganhou'))

            elif verifica_vitoria() == "velha":
                label.config(text="Deu velha!")

        else:

            tabuleiro[row][column]['text'] = jogadorAtual

            if verifica_vitoria() is False:
                jogadorAtual = jogadores[0]
                label.config(text=('Vez do jogador '+ jogadorAtual[0]))

            elif verifica_vitoria() is True:
                label.config(text=('Jogador '+jogadores[1]+' ganhou'))

            elif verifica_vitoria() == "velha":
                label.config(text="Deu velha!")

def verifica_vitoria():
    for row in range(3):
        if tabuleiro[row][0]['text'] == tabuleiro[row][1]['text'] == tabuleiro[row][2]['text'] != "":
            tabuleiro[row][0]
            tabuleiro[row][1]
            tabuleiro[row][2]
            return True

    for column in range(3):
        if tabuleiro[0][column]['text'] == tabuleiro[1][column]['text'] == tabuleiro[2][column]['text'] != "":
            tabuleiro[0][column]
            tabuleiro[1][column]
            tabuleiro[2][column]
            return True

    if tabuleiro[0][0]['text'] == tabuleiro[1][1]['text'] == tabuleiro[2][2]['text'] != "":
        tabuleiro[0][0]
        tabuleiro[1][1]
        tabuleiro[2][2]
        return True

    elif tabuleiro[0][2]['text'] == tabuleiro[1][1]['text'] == tabuleiro[2][0]['text'] != "":
        tabuleiro[0][2]
        tabuleiro[1][1]
        tabuleiro[2][0]
        return True

    elif verifica_velha() is False:

        for row in range(3):
            for column in range(3):
                tabuleiro[row][column]
        return "velha"

    else:
        return False

def verifica_velha():
     espacos = 9

     for rows in range(3):
          for columns in range(3):
               if tabuleiro[rows][columns]['text'] != "":
                    espacos-=1

     if espacos == 0:
            return False
     else:
            return True

def novo_jogo():
    global jogadorAtual
    jogadorAtual = jogadores[0]
    label.config(text='Vez do jogador ' + jogadores[0])
    for row in range(3):
        for column in range(3):
            tabuleiro[row][column].config(text="")

janela = Tk()
janela.title('Jogo da Velha')
jogadores = ["X","O"]
jogadorAtual = jogadores[0]
janela.config(bg='white')

tabuleiro = np.empty((3, 3), dtype=object)

label = Label(text='Vez do jogador '+ jogadores[0], bg='yellow', fg='black')
label.pack(side='top', pady= 10)

reset_button = Button(text="Novo jogo", command=novo_jogo, bg='black',fg='white', border=5)
reset_button.pack(side="bottom",pady= 10)

frame = Frame(janela)
frame.pack()

for row in range(3):
    for column in range(3):
        tabuleiro[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,bg='blue',
                                      command= lambda row=row, column=column: troca_jogador(row,column))
        tabuleiro[row][column].grid(row=row,column=column)
        
janela.mainloop()