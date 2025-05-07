#----------Imports
import tabuleiro as tb
import jogadas as jd

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

def regras():
    regras = """"
        ----------Regras----------
        > O jogo de damas é praticado em um tabuleiro de 64 casas, claras e escuras. A grande diagonal (escura), deve ficar sempre à esquerda de cada jogador. O objetivo do jogo é imobilizar ou capturar todas as peças do adversário.  
        > O jogo de damas é praticado entre dois parceiros, com 12 pedras brancas de um lado e com 12 pedras pretas de outro lado. O lance inicial cabe sempre a quem estiver com as peças brancas.
        > A pedra anda só para frente, uma casa de cada vez. Quando a pedra atinge a oitava linha do tabuleiro ela é promovida à dama.
        > A dama é uma peça de movimentos mais amplos. Ela anda para frente e para trás, quantas casas quiser. A dama não pode saltar uma peça da mesma cor.
        > A captura é obrigatória.
        > Não existe sopro. (Regra do sopro: Se um jogador deixa de capturar uma peça do adversário quando tem a obrigação de fazê-lo, o adversário pode “soprar” (ou retirar) a peça que deveria ter feito a captura.)
        > Duas ou mais peças juntas, na mesma diagonal, não podem ser capturadas.
        > A pedra captura a dama e a dama captura a pedra. Pedra e dama têm o mesmo valor para capturarem ou serem capturadas. 
        > A pedra e a dama podem capturar tanto para frente como para trás, uma ou mais peças.
        > Se no mesmo lance se apresentar mais de um modo de capturar, é obrigatório executar o lance que capture o maior número de peças.
        > A pedra que durante o lance de captura de várias peças, apenas passe por qualquer casa de coroação, sem aí parar, não será promovida à dama.
        > Na execução do lance do lance de captura, é permitido passar mais de uma vez pela mesma casa vazia, não é permitido capturar duas vezes a mesma peça. 
        > Na execução do lance de captura, não é permitido capturar a mesma peça mais de uma vez e as peças capturadas não podem ser retiradas do tabuleiro antes de completar o lance de captura. 
        >Empate:
        Após 20 lances sucessivos de damas, sem captura ou deslocamento de pedra, a partida é declarada empatada.
        
        Finais de:
            2 damas contra 2 damas;
            2 damas contra uma;
            2 damas contra uma dama e uma pedra;
            uma dama contra uma dama e uma dama contra uma dama e uma pedra, são declarados empatados após 5 lances.
        
        ----------Fim----------
        """

    print(regras)
    
    jogar = input('Deseja jogar agora? (y/n)')

    if jogar == 'y':
        comeca_jogo()

    else:
        print('> Até a próxima então!')

#----------Controle do Jogo
def inicia_programa():
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
        regras()
            
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
            jd.analisa_jogada(jogada)
            conta_pecas()
            tb.imprime_tabuleiro()
        
        elif jd.jogador == 1:
            print('> ')
            print(f'> {jogador_preto}, é a sua vez!')
            jogada = input('> Informe seu movimento. (Ex. D3,C4)')
            jd.analisa_jogada(jogada)
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