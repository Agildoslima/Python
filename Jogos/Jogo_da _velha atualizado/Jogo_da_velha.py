from func_jog_velha import validar, jogar, imprimir, matriz_transposta
from random import randint
jogador = ['x', '0']
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
imprimir(matriz)
contador = 0
while contador < 9:
    x = input('Digite a linha entre 0 e 2 :')
    y = input('Digite a coluna entre 0 e 2 :')
    x, y = validar(x, y)
    jogar(matriz, x, y, 'x')
    contador += 1
    if contador == 9:
        imprimir(matriz)
        break

    jogar(matriz, randint(0, 2), randint(0, 2), '0')
    contador += 1
    imprimir(matriz)
    diagonal = [[matriz[0][0], matriz[1][1], matriz[2][2]], [matriz[2][0], matriz[1][1], matriz[0][2]]]

    for ind, i in enumerate(diagonal):
        for j in range(0, 2):
            if diagonal[ind].count(jogador[j]) == 3:
                print(jogador[j], 'Venceu')
                contador = 9
    transposta = matriz_transposta(matriz)
    for i in range(0, 3):
        for j in range(0, 2):
            if matriz[i].count(jogador[j]) == 3:
                print(jogador[j], 'Venceu')
                contador = 9
                break
            elif transposta[i].count(jogador[j]) == 3:
                print(jogador[j], 'Venceu')
                contador = 9
                break
print('Fim de Jogo')
