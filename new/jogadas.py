#----------Imports----------
import tabuleiro as tb
#----------Variáveis Globais----------
jogador = 0
#----------Apoio----------
def acessa_tile(tile, i_linha = 0, j_coluna = 0, index = 0):

    for linha_i in range(8):
        for coluna_j in range(8):
            if tb.tabuleiro[linha_i][coluna_j][0] == tile:
                    
                    if index != 0:
                        return linha_i,coluna_j     
                    
                    #Contorno do tabuleiro
                    elif linha_i + i_linha > 7 or linha_i + i_linha < -7:
                        if coluna_j + j_coluna > 7 or coluna_j + j_coluna < -7:
                            return tb.tabuleiro[linha_i][coluna_j]
                        else:
                            return tb.tabuleiro[linha_i][coluna_j + j_coluna]
                    else:
                        if coluna_j + j_coluna > 7 or coluna_j + j_coluna < -7:
                            return tb.tabuleiro[linha_i + i_linha][j_coluna]
                        else:
                            return tb.tabuleiro[linha_i + i_linha][coluna_j + j_coluna]
        
def calc_dist(q1,q2): 
    return [acessa_tile(q2,0,0,1)[0] - acessa_tile(q1,0,0,1)[0],acessa_tile(q2,0,0,1)[1] - acessa_tile(q1,0,0,1)[1]]

def e_vazio(tile,i_linha = 0, j_coluna = 0):
    booleano = False
    if acessa_tile(tile, i_linha, j_coluna)[2] == 'Vazio':
        booleano = True
    return booleano

def e_branco(tile,i_linha = 0, j_coluna = 0):
    booleano = False
    if acessa_tile(tile, i_linha, j_coluna)[2] == 'Peça Branca' or acessa_tile(tile)[2] == 'Rainha Branca':
        booleano = True
    return booleano

def e_preto(tile,i_linha = 0, j_coluna = 0):
    booleano = False
    if acessa_tile(tile, i_linha, j_coluna)[2] == 'Peça Preta' or acessa_tile(tile)[2] == 'Rainha Preta':
        booleano = True
    return booleano

def e_dama(tile):
    booleano = False
    if acessa_tile(tile)[2] == 'Rainha Branca' or acessa_tile(tile)[2] == 'Rainha Preta':
        booleano = True
    return booleano

def come_mais(tile):
    distancias_pecas = [[2,-2,1,-1],[2,2,1,1],[-2,-2,-1,-1],[-2,2,-1,1]]
    booleano = False

    for coluna2,linha2,coluna1,linha1 in distancias_pecas:
        if jogador == 0 and e_vazio(tile,coluna2,linha2) == True and e_preto(tile,coluna1,linha1) == True:
            booleano = True
        elif jogador == 1 and e_vazio(tile,coluna2,linha2) == True and e_branco(tile,coluna1,linha1) == True:
            booleano = True
    
    return booleano

def analisa_jogada(jogada):
    origem = jogada[:2]
    destino = jogada[3:]
    dist = calc_dist(origem,destino)

    global jogador

    if jogador == 0:
        if e_dama(origem) == False:
            if e_branco(origem) == True and e_vazio(destino) == True:
                if dist == [-1,-1] or dist == [-1,1]:
                    move_peca(origem,destino)
                    jogador = 1

                elif dist == [-2,-2] or dist == [-2,2] or dist == [2,-2] or dist == [2,2]:
                    if e_preto(origem,dist[0]//2,dist[1]//2) == True:
                        come_peca(origem,destino)

                        if come_mais(destino) == True:
                                jogador = 0
                        else:
                                jogador = 1
    
    elif jogador == 1:   
        if e_dama(origem) == False:
            if e_preto(origem) == True and e_vazio(destino) == True:
                if dist == [1,-1] or dist == [1,1]:
                    move_peca(origem,destino)
                    jogador = 0

                elif dist == [-2,-2] or dist == [-2,2] or dist == [2,-2] or dist == [2,2]:
                    if e_branco(origem,dist[0]//2,dist[1]//2) == True:
                        come_peca(origem,destino)
                    
                        if come_mais(destino) == True:
                            jogador = 1
                        else:
                            jogador = 0

def define_jogada(jogada):
    origem = jogada[:2]
    destino = jogada[3:]

    if e_dama(origem) == False:
        jogada_peca(origem,destino)
    
    #elif e_dama(origem) == True:
    #    jogada_rainha(origem,destino)

def jogada_peca(origem,destino):
    global jogador
    raw_dist = calc_dist(origem,destino)
    distancia = abs(raw_dist[0])

    if e_vazio(destino) == True:
        if distancia == 1:
            if e_branco(origem) and jogador == 0 and (raw_dist == [-1,-1] or raw_dist == [-1,1]):
                move_peca(origem, destino)
                jogador = 1

            elif e_preto(origem) and jogador == 1 and (raw_dist == [1,-1] or raw_dist == [1,1]):
                move_peca(origem, destino)
                jogador = 0
        
        elif distancia == 2:
            if e_branco(origem) and jogador == 0 and e_preto(origem,raw_dist[0]//2,raw_dist[1]//2) == True:
                come_peca(origem, destino)
                if come_mais(destino) == True:
                    jogador = 0
                else:
                    jogador = 1

            elif e_preto(origem) and jogador == 1 and e_branco(origem,raw_dist[0]//2,raw_dist[1]//2) == True:
                come_peca(origem, destino)
                if come_mais(destino) == True:
                    jogador = 1
                else:
                    jogador = 0

def procura_promo(jogador):
    
    if jogador == 0:
        for coluna in range(8):
            if tb.tabuleiro[0][coluna][2] == 'Peça Branca':
                tb.tabuleiro[0][coluna][2] = 'Rainha Branca'

    elif jogador == 1:
        for coluna in range(8):
            if tb.tabuleiro[7][coluna][2] == 'Peça Preta':
                tb.tabuleiro[7][coluna][2] = 'Rainha Preta'

#----------Jogadas----------
def move_peca(origem,destino):
    acessa_tile(destino)[2] = acessa_tile(origem)[2]
    acessa_tile(origem)[2] = 'Vazio'

def come_peca(origem,destino):

    linha = calc_dist(origem,destino)[0]//2
    coluna = calc_dist(origem,destino)[1]//2
    acessa_tile(origem,linha,coluna)[2] = 'Vazio'
    move_peca(origem,destino)

#--------Inputs