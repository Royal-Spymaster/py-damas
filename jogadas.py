import tabuleiro as tb

tabuleiro = tb.tabuleiro()

def valida_input(jogador):
    jogada = input('Defina qual peça você quer mover: ')
    validas = []
    indice_input = devolve_index(jogada)

    if jogador == 'Preto':
        validas.append(tabuleiro[indice_input[0]+1][indice_input[1]-1][0])
        validas.append(tabuleiro[indice_input[0]+1][indice_input[1]+1][0])

    else:
        validas.append(tabuleiro[indice_input[0]-1][indice_input[1]-1])
        validas.append(tabuleiro[indice_input[0]-1][indice_input[1]+1])
 
    return 'As jogadas válidas são: ' + ','.join(validas)

def move_peca(atual =str, destino =str):
    'Movimento de pecas livremente, retorna tabuleiro atualizado.'
    for coluna in tabuleiro:
        for linha in tabuleiro:
            if tabuleiro[tabuleiro.index(coluna)][tabuleiro.index(linha)][0] == atual:
                if evazio(destino) == True:
                    tabuleiro[devolve_index(destino)[0]][devolve_index(destino)[1]][2] = tabuleiro[tabuleiro.index(coluna)][tabuleiro.index(linha)][2]
                    tabuleiro[tabuleiro.index(coluna)][tabuleiro.index(linha)][2] = tb.estado.get('sem_peca')
                    
    return tabuleiro
                    
                    
def devolve_index(tile):
    'busca tile inputado no tabuleiro, retornando os indices'
    'ex. A1 -> [0,0,0]'
    for coluna in tabuleiro:
        for linha in tabuleiro:
            if tabuleiro[tabuleiro.index(coluna)][tabuleiro.index(linha)][0] == tile:
                return [tabuleiro.index(coluna),tabuleiro.index(linha)]

def evazio(tile =str):
    'Condicional para determinar tiles sem pecas. Retorna True se o tile estiver vazio.'
    
    for coluna in tabuleiro:
        for linha in tabuleiro:
            if tabuleiro[tabuleiro.index(coluna)][tabuleiro.index(linha)][0] == tile:
                if tabuleiro[tabuleiro.index(coluna)][tabuleiro.index(linha)][2] == 'Vazio':
                    return True
                else:
                    return False


                
    
