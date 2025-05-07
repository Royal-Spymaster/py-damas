#----------Variáveis Globais
tabuleiro = []
letras = ['A','B','C','D','E','F','G','H']
numeros = ['1','2','3','4','5','6','7','8']

#----------Apoio
def constroi_linha(num,primeiro_tile,peca = 'Vazio',primeira_peca = 0):
    tiles = ['Quadrado Branco', 'Quadrado Preto']
    pecas = ['Vazio',peca]
    linha = []

    for letra in range(8):
            if letra % 2 == 0:
                linha.append([letras[letra] + num,tiles[primeiro_tile],pecas[primeira_peca]])
            else:
                linha.append([letras[letra] + num,tiles[primeiro_tile-1],pecas[primeira_peca-1]])
    
    return linha

#----------Tabuleiro
def faz_tabuleiro():

    for num in numeros:
        if numeros.index(num) < 3:
            if numeros.index(num) % 2 == 0:
                tabuleiro.append(constroi_linha(num,0,'Peça Preta',0))
            else:
                tabuleiro.append(constroi_linha(num,1,'Peça Preta',1))

        elif numeros.index(num) >= 5:
            if numeros.index(num) % 2 == 0:
                tabuleiro.append(constroi_linha(num,0,'Peça Branca',0))
            else:
                tabuleiro.append(constroi_linha(num,1,'Peça Branca',1))

        else:
            if numeros.index(num) % 2 == 0:
                tabuleiro.append(constroi_linha(num,0))
            else:
                tabuleiro.append(constroi_linha(num,1))
                      
    return tabuleiro

def imprime_tabuleiro():
    pecas_imagem = [' ⛀ ',' ⛁ ', ' ⛂ ' , ' ⛃ ','   ']
    pecas_texto = ['Peça Branca', 'Rainha Branca','Peça Preta','Rainha Preta','Vazio']
    linhas = []

    print('> ')
    print('>      A    B    C    D    E    F    G    H')
    print('>     _______________________________________')

    for coluna in range(8):
        for linha in range(8):
            for item in pecas_texto:
                if tabuleiro[coluna][linha][2] == item:
                    linhas.append(pecas_imagem[pecas_texto.index(item)])
        linhas_prontas = ' |'.join(linhas)
        linhas = []
        print('> ',coluna + 1,'  ','|', linhas_prontas,' |','  ', coluna + 1, sep='')

    print('>     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('>      A    B    C    D    E    F    G    H')
    print('> ')

#----------Chamada de Funções

faz_tabuleiro()
imprime_tabuleiro()