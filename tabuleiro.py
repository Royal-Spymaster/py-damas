estado = {
        
        'tile_branco':      'Branco',
        'tile_preto':       'Preto',
        
        'peca_branca':      'Peca Branca',
        'peca_preta':       'Peca Preta',
        
        'rainha_branca':    'Rainha Branca',
        'rainha_preta':     'Rainha Preta',
        
        'sem_peca':         'Vazio',
        }

#coord = faz_coordenadas()

def faz_tabuleiro():
    letras = ['A','B','C','D','E','F','G','H']
    numeros = ['1','2','3','4','5','6','7','8']
    
    lista_local= []
    tabuleiro = []
    

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
                        lista_local.append([letras[letras.index(coluna)] + numeros[numeros.index(linha)], estado.get('tile_branco'), estado.get('sem_peca')])
                    else:
                        lista_local.append([letras[letras.index(coluna)] + numeros[numeros.index(linha)], estado.get('tile_preto'), estado.get('peca_preta')])
            else:
                for linha in numeros:
                    if epar(numeros.index(linha)) == True:
                        lista_local.append([letras[letras.index(coluna)] + numeros[numeros.index(linha)], estado.get('tile_preto'), estado.get('peca_preta')])
                    else:
                        lista_local.append([letras[letras.index(coluna)] + numeros[numeros.index(linha)], estado.get('tile_branco'), estado.get('sem_peca')])

        elif letras.index(coluna) >= 5:
            'coluna F, G e H comecam com pecas brancas.'
            if epar(letras.index(coluna)) == True:
                for linha in numeros:
                        if epar(numeros.index(linha)) == True:
                            lista_local.append([letras[letras.index(coluna)] + numeros[numeros.index(linha)], estado.get('tile_branco'), estado.get('sem_peca')])
                        else:
                            lista_local.append([letras[letras.index(coluna)] + numeros[numeros.index(linha)], estado.get('tile_preto'), estado.get('peca_branca')])
            else:
                for linha in numeros:
                        if epar(numeros.index(linha)) == True:
                            lista_local.append([letras[letras.index(coluna)] + numeros[numeros.index(linha)], estado.get('tile_preto'), estado.get('peca_branca')])
                        else:
                            lista_local.append([letras[letras.index(coluna)] + numeros[numeros.index(linha)], estado.get('tile_branco'), estado.get('sem_peca')])
        else:
            'tiles sem pecas no comeco'
            if epar(letras.index(coluna)) == True:
                for linha in numeros:
                    if epar(numeros.index(linha)) == True:
                        lista_local.append([letras[letras.index(coluna)] + numeros[numeros.index(linha)], estado.get('tile_branco'), estado.get('sem_peca')])
                    else:
                        lista_local.append([letras[letras.index(coluna)] + numeros[numeros.index(linha)], estado.get('tile_preto'), estado.get('sem_peca')])
            else:
                for linha in numeros:
                    if epar(numeros.index(linha)) == True:
                        lista_local.append([letras[letras.index(coluna)] + numeros[numeros.index(linha)], estado.get('tile_preto'), estado.get('sem_peca')])
                    else:
                        lista_local.append([letras[letras.index(coluna)] + numeros[numeros.index(linha)], estado.get('tile_branco'), estado.get('sem_peca')])
        tabuleiro.append(lista_local)
        lista_local = []

        return tabuleiro

def epar(num):
    'Retorna se número é par ou não.'
    if num % 2 == 0:
       return True
    else:
        return False



tabuleiro_feito = faz_tabuleiro()
print(tabuleiro_feito)
