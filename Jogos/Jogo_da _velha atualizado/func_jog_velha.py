from random import randint


def validar(*args):
    args = list(args)
    lc = ['Linha', 'Coluna']
    for ind, i in enumerate(args):
        while not i.isnumeric():
            if ind == 0:
                print(f'\n voce digitou {i} na linha')
                i = input('Digite a linha, nao digite letras : ')
            elif ind == 1:
                print(f'\n voce digitou {i} na coluna')
                i = input('Digite a coluna, nao digite letras : ')
        else:
            args[ind] = int(i)
            while args[ind] > 2:

                x = input(f'digite um valor da {lc[ind]} entre 0 e 2 :')
                if x.isnumeric():
                    args[ind] = int(x)
                    print('linha = ', args[0])
                    print('coluna = ', args[1])

    return args


def jogar(matriz, x, y, jogador):
    matriz = list(matriz)
    if matriz[x][y] == ' ':
        matriz[x][y] = jogador

    else:

        while True:
            if jogador == 'x':
                print('\n escolha outra posicão')
                x = input('Digite a linha entre 0 e 2 :')
                y = input('Digite a coluna entre 0 e 2 :')
                x, y = validar(x, y)
                if matriz[x][y] == ' ':
                    matriz[x][y] = jogador
                    break
            else:

                x = randint(0, 2)
                y = randint(0, 2)
                if matriz[x][y] == ' ':
                    matriz[x][y] = jogador

                    break


def imprimir(matriz):
    lin = len(matriz)
    col = 0
    for i in matriz:
        for j in i:
            col += 1
    col = int(col / lin)
    sinal = '-' * col
    for l in range(0, lin):
        if l == 1:
            print(f'--|-{sinal}|--')
        elif l == lin - 1:
            print(f'--|-{sinal}|--')
        for c in range(0, col):
            if c == 1:
                print(' |', matriz[l][c], end='')
            elif c == (col - 1):
                print('  |', matriz[l][c], end='')
            else:
                print(matriz[l][c], end='')

        print()

def matriz_transposta(matriz):
    matriz = list(matriz)
    matriz_transposta = []
    for indice, i in enumerate(matriz):
        matriz_vazia = []
        for indice2 in range(0, 3):
            matriz_vazia.append(matriz[indice2][indice])
        matriz_transposta.append(matriz_vazia)

    return matriz_transposta


