#----------Imports----------
import tabuleiro as tb

#----------Variáveis Globais
jogador = 0

#----------Apoio----------
def acessa_tile(tile, i_coluna = 0, j_linha = 0, index = 0):

    for coluna in range(8):
        for linha in range(8):

            if tb.tabuleiro[coluna][linha][0] == tile:
                if index != 0:
                    return coluna,linha

                elif coluna + i_coluna > 7 or coluna + i_coluna < -7:
                    if linha + j_linha > 7 or linha + j_linha < -7:
                        return tb.tabuleiro[coluna][linha]
                    else:
                        return tb.tabuleiro[coluna][linha + j_linha]
                else:
                    if linha + j_linha > 7 or linha + j_linha < -7:
                        return tb.tabuleiro[coluna + i_coluna][j_linha]
                    else:
                        return tb.tabuleiro[coluna + i_coluna][linha + j_linha]
        
def calc_dist(q1,q2):
    return [acessa_tile(q1,0,0,1)[0] - acessa_tile(q2,0,0,1)[0],acessa_tile(q1,0,0,1)[1] - acessa_tile(q2,0,0,1)[1]]

def e_vazio(tile,i_coluna = 0, j_linha = 0):
    booleano = False
    if acessa_tile(tile, i_coluna, j_linha)[2] == 'Vazio':
        booleano = True
    return booleano

def e_branco(tile,i_coluna = 0, j_linha = 0):
    booleano = False
    if acessa_tile(tile, i_coluna, j_linha)[2] == 'Peça Branca' or acessa_tile(tile)[2] == 'Rainha Branca':
        booleano = True
    return booleano

def e_preto(tile,i_coluna = 0, j_linha = 0):
    booleano = False
    if acessa_tile(tile, i_coluna, j_linha)[2] == 'Peça Preta' or acessa_tile(tile)[2] == 'Rainha Preta':
        booleano = True
    return booleano

def e_dama(tile):
    booleano = False
    if acessa_tile(tile)[2] == 'Rainha Branca' or acessa_tile(tile)[2] == 'Rainha Preta':
        booleano = True
    return booleano

def come_mais(tile):
    distancias = [[2,-2,1,-1],[2,2,1,1],[-2,-2,-1,-1],[-2,2,-1,1]]
    booleano = False

    for coluna2,linha2,coluna1,linha1 in distancias:
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
            if e_branco(origem) == True and e_vazio(destino) == True:   #Movimentação Peça Branca
                if dist == [1,-1] or dist == [1,1]:
                    move_peca(origem,destino)
                    #promove(destino)
                    jogador = 1

                elif dist == [-2,-2] or dist == [-2,2] or dist == [2,-2] or dist == [2,2]:                 #Ação de comer da Peça Branca
                    if e_preto(origem,dist[0]//2,dist[1]//2) == True:
                        come_peca(origem,destino)
                    
                        if come_mais(destino) == True:
                                jogador = 0
                        else:
                                jogador = 1
                    #promove(destino)
    
    elif jogador == 1:   
        if e_dama(origem) == False:
            if e_preto(origem) == True and e_vazio(destino) == True:
                if dist == [-1,-1] or dist == [-1,1]:
                    move_peca(origem,destino)
                    #promove(destino)
                    jogador = 0

                elif dist == [-2,-2] or dist == [-2,2] or dist == [2,-2] or dist == [2,2]:
                    if e_branco(origem,dist[0]//2,dist[1]//2) == True:
                        come_peca(origem,destino)
                    
                        if come_mais(destino) == True:
                            jogador = 1
                        else:
                            jogador = 0
                    
                    #promove(destino)
    
#----------Jogadas----------
def move_peca(origem,destino):
    acessa_tile(destino)[2] = acessa_tile(origem)[2]
    acessa_tile(origem)[2] = 'Vazio'

def come_peca(origem,destino):
    dist = calc_dist(origem,destino)
    acessa_tile(destino,dist[0]//2,dist[1]//2)[2] = 'Vazio'
    move_peca(origem,destino)

#--------Inputs


tb.faz_tabuleiro()
acessa_tile('D5',1,-1)
#analisa_jogada('C6,D5')
#tb.imprime_tabuleiro()
#analisa_jogada('F3,E4')
#tb.imprime_tabuleiro()
#analisa_jogada('D5,F3')
