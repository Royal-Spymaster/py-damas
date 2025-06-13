#----------Imports----------
import tabuleiro as tb

#----------Variáveis Globais----------
jogador = 0
diagonais_direitas = []
diagonais_esquerdas = []
diagonais_fatiadas = []
diagonais_booleanas = ''
diagonal = []
origem = ''
destino = ''

#----------Manipulação do Tabuleiro----------
def acessa_tile(tile, i_linha = 0, j_coluna = 0, index = 0):

    for linha in range(8):
        for coluna in range(8):
            if tb.tabuleiro[linha][coluna][0] == tile:
                    
                    if index != 0:
                        return linha,coluna     
                    
                    #Contorno do tabuleiro
                    elif linha + i_linha > 7 or linha + i_linha < -7:
                        if coluna + j_coluna > 7 or coluna + j_coluna < -7:
                            return tb.tabuleiro[linha][coluna]
                        else:
                            return tb.tabuleiro[linha][coluna + j_coluna]
                    else:
                        if coluna + j_coluna > 7 or coluna + j_coluna < -7:
                            return tb.tabuleiro[linha + i_linha][j_coluna]
                        else:
                            return tb.tabuleiro[linha + i_linha][coluna + j_coluna]

def calc_dist(q1,q2): 
    return [acessa_tile(q2,0,0,1)[0] - acessa_tile(q1,0,0,1)[0],acessa_tile(q2,0,0,1)[1] - acessa_tile(q1,0,0,1)[1]]

#----------Condicionais----------

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

def e_quadrado(lista):
    booleano = False
    if abs(lista[0]) == abs(lista[1]):
        booleano = True
    return booleano

def esquerda_ou_direita(origem,destino):
    direcao = calc_dist(origem,destino)
    booleano = False

    if direcao[0] + direcao[1] == 0: #True = Esquerda, False = Direita
        booleano = True
    return booleano

def all_string_zero(lista):
    booleano = True

    for i in lista:
        if i != '0':
            booleano = False
    
    return booleano

#----------Diagonais----------
def cria_diagonais(tile):
    global diagonais_esquerdas        
    global diagonais_direitas
    global diagonais_fatiadas

    diagonais_direitas = []
    diagonais_esquerdas = []
    diagonais_fatiadas = []

    for linha in range(8):
        for coluna in range(8):
          direcao = calc_dist(tile, tb.tabuleiro[linha][coluna][0])
          if tb.tabuleiro[linha][coluna][0] == tile:
                  diagonais_esquerdas.append(tb.tabuleiro[linha][coluna][0])
                  diagonais_direitas.append(tb.tabuleiro[linha][coluna][0])

          elif e_quadrado(direcao):
              if esquerda_ou_direita(tile,tb.tabuleiro[linha][coluna][0]):
                  diagonais_esquerdas.append(tb.tabuleiro[linha][coluna][0])
              else:
                  diagonais_direitas.append(tb.tabuleiro[linha][coluna][0])

def bool_diagonal(lista):
    global diagonais_booleanas
    diagonais_booleanas = ''
    for tile in lista:
        if e_vazio(tile):
            diagonais_booleanas += '1'
        else:
            diagonais_booleanas += '0'

def direcao_diagonal(origem,destino):
    global diagonal
    if esquerda_ou_direita(origem,destino):
        diagonal = diagonais_esquerdas
    else:
        diagonal = diagonais_direitas
    
def tamanho_diagonal(origem,destino):
    global diagonal

    inicio = 0
    fim = 0 
    for item in diagonal:
        if item == origem:  
            inicio = diagonal.index(origem)
            break
    
    for item2 in diagonal:
        if item2 == destino:
            fim = diagonal.index(destino)
            break

    diagonal = diagonal[min(inicio,fim):max(inicio,fim)+1]

def fatia_diagonais(tile,lista):
    for item in range(len(lista)):
            if tile == lista[item]:
                diagonais_fatiadas.append(lista[item+1:])
                diagonais_fatiadas.append(lista[:item])


def molda_diagonal(origem,destino):
    global diagonal
    cria_diagonais(origem)
    direcao_diagonal(origem,destino)
    tamanho_diagonal(origem,destino)
    fatia_diagonais(origem,diagonais_direitas)
    fatia_diagonais(origem,diagonais_esquerdas)

#----------Definição das jogadas----------
def define_jogada(jogada):
    global origem
    global destino
    origem = jogada[:2]
    destino = jogada[3:]
    molda_diagonal(origem,destino)

    if e_dama(origem) == False:
        jogada_peca(origem,destino)
    
    elif e_dama(origem) == True:
        jogada_rainha(origem,destino)

def come_mais(tile):
    booleano = False
    jogada_valida = '10'
    fatia_diagonais(tile,diagonais_direitas)
    fatia_diagonais(tile,diagonais_esquerdas)

    #preciso transformar os dados que vem em uma "string booleana"
    #lista -> '10' ou lista -> '11010 por ex

    for lista in diagonais_fatiadas:
        bool_diagonal(lista)

        if diagonais_booleanas[:2] == jogada_valida:
            if e_branco(tile) and e_preto(lista[1]):
                booleano = True
            
            elif e_preto(tile) and e_branco(lista[1]):
                booleano = True
        
        elif e_dama(tile):
            for i in range(len(lista)):
                if jogada_valida in lista and all_string_zero(lista[:lista.index(jogada_valida)]):
                    if e_branco(tile) and e_preto(lista[lista.index(jogada_valida)]):
                        booleano = True

                    elif e_preto(tile) and e_branco(lista[lista.index(jogada_valida)]):
                        booleano = True

    return booleano

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
    acessa_tile(diagonal[-2])[2] = 'Vazio' 
    move_peca(origem,destino)

def jogada_rainha(origem, destino):
    global jogador
    jogada_valida = '10'
    bool_diagonal(diagonal)
    
    if jogada_valida in diagonais_booleanas and all_string_zero(diagonais_booleanas[:diagonais_booleanas.index(jogada_valida)]):
        if e_branco(origem) and e_preto(diagonal[diagonais_booleanas.index(jogada_valida)+1]):
            come_peca(origem,destino)
            if come_mais(destino):
                jogador = 0
            else:
                jogador = 1

        elif e_preto(origem) and e_branco(diagonais_booleanas[diagonais_booleanas.index(jogada_valida)]):
            come_peca(origem,destino)
            if come_mais(destino):
                jogador = 1
            else:
                jogador = 0
    
    elif not all(diagonal) and e_vazio(destino):
        if e_branco(origem):
            move_peca(origem,destino)
            jogador = 1

        elif e_preto(origem):
            move_peca(origem,destino)
            jogador = 0
        

def jogada_peca(origem,destino):
    global jogador
    raw_dist = calc_dist(origem,destino)
    distancia = len(diagonal)

    if e_vazio(destino):
        if distancia == 2:
            if e_branco(origem) and jogador == 0 and (raw_dist == [-1,-1] or raw_dist == [-1,1]):
                move_peca(origem, destino)
                jogador = 1

            elif e_preto(origem) and jogador == 1 and (raw_dist == [1,-1] or raw_dist == [1,1]):
                move_peca(origem, destino)
                jogador = 0
        
        elif distancia == 3: 
            #essa checagem está errada, não é possível pelas regras comer para trás como dama
            #acabei de perceber outro problema e como ele afeta a come mais
            #refatorar (ESSE É TRIVIAL)
            if e_branco(origem) and jogador == 0 and e_preto(origem,raw_dist[0]//2,raw_dist[1]//2):
                come_peca(origem, destino)
                if come_mais(destino):
                    jogador = 0
                else:
                    jogador = 1

            elif e_preto(origem) and jogador == 1 and e_branco(origem,raw_dist[0]//2,raw_dist[1]//2):
                come_peca(origem, destino)
                if come_mais(destino):
                    jogador = 1
                else:
                    jogador = 0
