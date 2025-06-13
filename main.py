#----------Imports
import tabuleiro as tb
import jogadas as jd
import regras as r

#----------Variáveis Globais
jogador_branco = ''
jogador_preto = ''
partida_encerrada = False
vencedor = ''

#----------Apoio
def comeca_jogo():
    global jogador_branco
    global jogador_preto
    jogador_branco = input('> Jogador Branco (⛀ ), insira o nome que deseja usar: ')
    jogador_preto = input('> Jogador Preto (⛂ ), insira o nome que deseja usar: ')
    print(f'> O jogo vai começar! {jogador_branco}, você joga primeiro!')
    print('> ')
        
    tb.faz_tabuleiro()
    tb.imprime_tabuleiro()
    controla_jogo()

#----------Controle do Jogo
def inicia_programa():
    print('> ')
    print('> Bem Vindo ao Jogo de Damas')
    print('> ')
    print('> 1 - Começar Partida')
    print('> 2 - Ver Regras')
    print('> 3 - Sair')
    print('> ')

    resposta = int(input('> Insira o número desejado para navegar pelo menu: '))

    if resposta == 1:
        print('> ')
        print('> A partida vai começar, preparem-se!')
        comeca_jogo()

    elif resposta == 2:
        print('> ')
        r.regras()
            
    elif resposta == 3:
        print('> ')
        print('> Até a próxima!')
    
    else:
        raise Exception('Somente inputs de 1 a 3.')

def controla_jogo():

    while partida_encerrada != True:
        if jd.jogador == 0:
            print('> ')
            print(f'> {jogador_branco}, é a sua vez!')
            jogada = input('> Informe seu movimento. (Ex. C6,D5)')
            jd.define_jogada(jogada)
            conta_pecas()
            
            if jd.come_mais(jd.destino):
                tb.imprime_tabuleiro()
            
            else:
                jd.procura_promo(0)
                tb.imprime_tabuleiro()
        
        elif jd.jogador == 1:
            print('> ')
            print(f'> {jogador_preto}, é a sua vez!')
            jogada = input('> Informe seu movimento. (Ex. D3,C4)')
            jd.define_jogada(jogada)
            conta_pecas()

            if jd.come_mais(jd.destino):
                tb.imprime_tabuleiro()
            
            else:
                jd.procura_promo(1)
                tb.imprime_tabuleiro()
    
    print(f'> Fim de partida!, o vencedor é o {vencedor}!')
    print('> Alexa, toque Sweet Victory do David Glen!')

def conta_pecas():
    pecas_pretas = 0
    pecas_brancas = 0

    for coluna in range(8):
        for linha in range(8):
            if tb.tabuleiro[coluna][linha][2] == 'Peça Preta' or tb.tabuleiro[coluna][linha][2] == 'Rainha Preta':
                pecas_pretas += 1

            elif tb.tabuleiro[coluna][linha][2] == 'Peça Branca' or tb.tabuleiro[coluna][linha][2] == 'Rainha Branca':
                pecas_brancas += 1

    if pecas_brancas == 0:
        partida_encerrada == True
        vencedor = jogador_branco
    
    elif pecas_pretas == 0:
        partida_encerrada == True
        vencedor = jogador_preto
    
    else:
        partida_encerrada == False

inicia_programa()