#------------variáveis globais---------------
estado = {
        
        'tile_branco':      'Branco',
        'tile_preto':       'Preto',
        
        'peca_branca':      'Peca Branca',
        'peca_preta':       'Peca Preta',
        
        'rainha_branca':    'Rainha Branca',
        'rainha_preta':     'Rainha Preta',
        
        'sem_peca':         'Vazio',
        }

diagonais = {}

tiles = {}

#------------funções de apoio-----------------

def epar(num):
    'Retorna se número é par ou não.'
    if num % 2 == 0:
       return True
    else:
        return False

def evazio(destino):
    if tiles.get(destino)[1] == estado.get('sem_peca'):
        return True
    else:
        return False

def ediagonal(atual,destino):
    'Função que checa se o tile atual e o tile de destino são diagonais.'
    return True

def geradiagonais():
    'Função que gera as diagonais de cada coordenada'

    valor_texto = ''
    i = 0
    j = 1
    k = 0
    lista_chaves = []
    lista_diag = []

    'Gera lista com todas as posições possíveis: 1 a 64 (0 a 63).'
    for key in tiles.items():
        lista_chaves.append(key[0])


    """
    while i < 63:
        while j < (9 - k):

            if (lista_chaves.index(lista_chaves[i]) + 9*j) < len(lista_chaves):
                #if (lista_chaves.index(lista_chaves[i]) - 9*j) > 0:
                    #lista_diag.append(lista_chaves[lista_chaves.index(lista_chaves[i]) - 9*j])
                lista_diag.append(lista_chaves[lista_chaves.index(lista_chaves[i]) + 9*j])
            
            j += 1
        
        k += 1

        if k > 8:
            k = 0
        
        diagonais.update({lista_chaves[i]:lista_diag})
        lista_diag = []
        
        j = 0
        i += 1

    """
    
    for item in lista_chaves:
        for mult in range (1,9):
            
            if (lista_chaves.index(item) + 9*mult) < len(lista_chaves):

                if (lista_chaves.index(item) - 9*mult) > 0:
                    lista_diag.append(lista_chaves[lista_chaves.index(item) - 9*mult])
                lista_diag.append(lista_chaves[lista_chaves.index(item) + 9*mult])
            lista_diag.sort()
            diagonais.update({item:lista_diag})
        lista_diag = []
    
    return diagonais

#---------------tabuleiro--------------

def faz_tabuleiro():
    letras = ['A','B','C','D','E','F','G','H']
    numeros = ['1','2','3','4','5','6','7','8']

    'Estrutura do tabuleiro: tabuleiro com 8 colunas e 8 linhas, totalizando 64 tiles.'
    'Cada tile tem um valor de coluna, linha e estado atual do tile atribuído. ex. [A1, bV].'
    
    for coluna in letras:
        'tabuleiro gerado baseando se nas linhas e colunas.'
        'linhas impares tem colunas tem colunas impares brancas. ex. A1 -> Coluna 1, linha 1 -> tile preto.'
        'linhas pares tem colunas brancas pares. ex. B2 -> Coluna 2, linha 2 -> tile branco.'
        'linhas <= 3 (index <= 2) inicialmente tem pecas pretas em tiles pretos. ex. A2 -> Coluna 2, linha 1 -> tile preto peca preta.'
        'linhas >= 6 (index >= 5) inicialmente tem pecas brancas em tiles pretos. ex. F1 -> Coluna 6, linha 1 -> tile preto peca branca.'

        if letras.index(coluna) <= 2:
            'colunas A, B e C comecam com pecas pretas.'
            if epar(letras.index(coluna)) == True:
                for linha in numeros:
                    if epar(numeros.index(linha)) == True:
                        tiles.update({letras[letras.index(coluna)] + numeros[numeros.index(linha)]: [estado.get('tile_branco'), estado.get('sem_peca')]})
                    else:
                        tiles.update({letras[letras.index(coluna)] + numeros[numeros.index(linha)]: [estado.get('tile_preto'), estado.get('peca_preta')]})
            else:
                for linha in numeros:
                    if epar(numeros.index(linha)) == True:
                        tiles.update({letras[letras.index(coluna)] + numeros[numeros.index(linha)]: [estado.get('tile_preto'), estado.get('peca_preta')]})
                    else:
                        tiles.update({letras[letras.index(coluna)] + numeros[numeros.index(linha)]: [estado.get('tile_branco'), estado.get('sem_peca')]})

        elif letras.index(coluna) >= 5:
            'coluna F, G e H comecam com pecas brancas.'
            if epar(letras.index(coluna)) == True:
                for linha in numeros:
                        if epar(numeros.index(linha)) == True:
                            tiles.update({letras[letras.index(coluna)] + numeros[numeros.index(linha)]: [estado.get('tile_branco'), estado.get('sem_peca')]})
                        else:
                            tiles.update({letras[letras.index(coluna)] + numeros[numeros.index(linha)]: [estado.get('tile_preto'), estado.get('peca_branca')]})
            else:
                for linha in numeros:
                        if epar(numeros.index(linha)) == True:
                            tiles.update({letras[letras.index(coluna)] + numeros[numeros.index(linha)]: [estado.get('tile_preto'), estado.get('peca_branca')]})
                        else:
                            tiles.update({letras[letras.index(coluna)] + numeros[numeros.index(linha)]: [estado.get('tile_branco'), estado.get('sem_peca')]})
        else:
            'tiles sem pecas no comeco'
            if epar(letras.index(coluna)) == True:
                for linha in numeros:
                    if epar(numeros.index(linha)) == True:
                        tiles.update({letras[letras.index(coluna)] + numeros[numeros.index(linha)]: [estado.get('tile_branco'), estado.get('sem_peca')]})
                    else:
                        tiles.update({letras[letras.index(coluna)] + numeros[numeros.index(linha)]: [estado.get('tile_preto'), estado.get('sem_peca')]})
            else:
                for linha in numeros:
                    if epar(numeros.index(linha)) == True:
                        tiles.update({letras[letras.index(coluna)] + numeros[numeros.index(linha)]: [estado.get('tile_preto'), estado.get('sem_peca')]})
                    else:
                        tiles.update({letras[letras.index(coluna)] + numeros[numeros.index(linha)]: [estado.get('tile_branco'), estado.get('sem_peca')]})

    return tiles

#-------------------jogadas------------------

def move_peca(atual =str, destino =str):
    'Movimento de pecas livremente, retorna tabuleiro atualizado.'
    if evazio(destino) == True:
        tiles.update({destino:[tiles.get(destino)[0], tiles.get(atual)[1]]})
        tiles.update({atual:[tiles.get(atual)[0], estado.get('sem_peca')]}) 

    #elif evazio(destino) == False and ediagonal(destino) == True:
    else:
        return 'Jogada inválida'

    promove_peca()

    return tiles

def promove_peca():
    for chave in tiles:
        if len(tiles[chave]) <=8 and tiles.get(chave)[1] == estado.get('peca_branca'):
            tiles.update({chave:[tiles.get(chave)[0], estado.get('rainha_branca')]})
        
        elif len(tiles[chave]) >= 56 and tiles.get(chave)[1] == estado.get('peca_preta'):
            tiles.update({chave:[tiles.get(chave)[0], estado.get('rainha_preta')]})


#-------------------chamadas de funções------------------------
tabuleiro = faz_tabuleiro()
diagonais = geradiagonais()
print(diagonais)
"""print(tabuleiro)
print('')
print(move_peca('F3','A1'))
print('')"""