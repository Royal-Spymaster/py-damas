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
    
    pecas_imagem = {'0': ' ⛀ ',    #Peça Branca no Quadrado Branco
                     '1': ' ⛃ ',   #Rainha Branca no Quadrado Branco
                     '2': ' ⛂ ',   #Peça Preta no Quadrado Branco
                     '3': ' ⛃ ',   #Rainha Preta no Quadrado Branco
                     '4': '    ',   #Quadrado Branco Vazio
                     '10':'|⛀ |',  #Peça Branca no Quadrado Preto
                     '11':'|⛁ |',  #Rainha Branca no Quadrado Preto
                     '12':'|⛂ |',  #Peça Preta no Quadrado Preto
                     '13':'|⛃ |',  #Rainha Preta no Quadrado Preto
                     '14':'||||'    #Quadrado Branco Preto
    }

    pecas_texto = ['Peça Branca', 'Rainha Branca','Peça Preta','Rainha Preta','Vazio'] #0,1,2,3,4
    pecas_tile = ['Quadrado Branco', 'Quadrado Preto'] #0,10
    linhas = []

    for coluna in range(8):
        for linha in range(8):
            codigo = 0
            linhas_prontas = []
            for item in pecas_texto:
                if tabuleiro[coluna][linha][2] == item:
                    codigo += pecas_texto.index(item)
            
            for item2 in pecas_tile:
                if tabuleiro[coluna][linha][1] == item2:
                    codigo += pecas_tile.index(item2)*10

            str_codigo = str(codigo)
            for chave in pecas_imagem:
                if str_codigo == chave:
                    linhas.append(pecas_imagem.get(str_codigo))

        linhas_prontas = '|'.join(linhas)
        linhas = []

        if coluna == 0:
            print('> ')
            print('>       A    B    C    D    E    F    G    H')
            print('>    ┌----┬┬┬┬┬┬----┬┬┬┬┬┬----┬┬┬┬┬┬----┬┬┬┬┬┐')
            print('> ',coluna + 1,'  ','|', linhas_prontas,'|','  ', coluna + 1, sep='')
            print('> ',' ','├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┤') 

        elif coluna == 7:
            print('> ',coluna + 1,'  ','|', linhas_prontas,'|','  ', coluna + 1, sep='')
            print('>    └┴┴┴┴┴----┴┴┴┴┴┴----┴┴┴┴┴┴----┴┴┴┴┴┴----┘')
            print('>       A    B    C    D    E    F    G    H')
            print('> ')

        elif coluna % 2 == 0:
            print('> ',coluna + 1,'  ','|', linhas_prontas,'|','  ', coluna + 1, sep='')
            print('> ',' ','├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┤')     

        else:
            print('> ',coluna + 1,'  ','|', linhas_prontas,'|','  ', coluna + 1, sep='')
            print('> ',' ','├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┤')            

#----------Chamada de Funções
