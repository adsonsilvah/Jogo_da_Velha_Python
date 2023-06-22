import numpy as np

jogadorO = ''
jogadorX = ''

tabuleiro = np.array([['', '', ''],
                      ['', '', ''],
                      ['', '', '']])

print(tabuleiro)
print()

while True:
   
   for i in range(1, 10):
    jogadorO = [int(o) for o in input("Vez do jogador O: ").split()]

    tabuleiro[jogadorO[0], jogadorO[1]] = 'O'

    print(tabuleiro)

    if(jogadorO != ''):
        jogadorX = [int(x) for x in input("Vez do jogador X: ").split()]

        tabuleiro[jogadorX[0], jogadorX[1]] = 'X'
        print(tabuleiro)
