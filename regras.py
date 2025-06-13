#--------Imports
import main as mn

#--------Regras
def regras():
    regras = """"
----------Regras----------
> O jogo de damas é praticado em um tabuleiro de 64 casas, claras e escuras. 
> A grande diagonal (escura), deve ficar sempre à esquerda de cada jogador. 
> O objetivo do jogo é imobilizar ou capturar todas as peças do adversário.  
>
> O jogo de damas é praticado entre dois parceiros, com 12 pedras brancas de um lado e com 12 pedras pretas de outro lado.
> O lance inicial cabe sempre a quem estiver com as peças brancas.
>
> A pedra anda só para frente, uma casa de cada vez. 
> Quando a pedra branca/preta atinge a primeira/oitava linha do tabuleiro ela é promovida à dama.
> Exemplo: Jogador branco faz o movimento A2 -> B1 com uma pedra branca
>
>      A   B                  A   B 
>   ┌----┬┬┬┬┬┬            ┌----┬┬┬┬┬┬
> 1 |    ||⛀ ||        1   |    ||⛁ ||
>   ├┬┬┬┬┼┴┴┴┴┼  ->        ├┬┬┬┬┼┴┴┴┴┼           ✔ Lance válido!
> 2 ||||||    |         2  ||||||    |
>   ├┴┴┴┴┼----┼            ├┴┴┴┴┼----┼
>
> A dama é uma peça de movimentos mais amplos.
> Ela anda para frente e para trás, quantas casas quiser.
> A dama não pode saltar uma peça da mesma cor.
> Exemplo: Jogador branco faz o movimento B1 -> D3 com uma rainha branca 
>
>      A    B    C    D              A    B    C    D         
>   ┌----┬┬┬┬┬┬----┬┬┬┬┬┬         ┌----┬┬┬┬┬┬----┬┬┬┬┬┬
> 1 |    ||⛁ ||    ||||||      1  |    ||||||    ||||||   
>   ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼         ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼
> 2 ||||||    ||||||    |  ->   2 ||||||    ||||||    |       ✔ Lance válido!
>   ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼         ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼
> 3 |    ||||||    ||||||       3 |    ||||||    ||⛁ ||
>   ├----┼┴┴┴┴┼----┼┴┴┴┴┼         ├----┼┴┴┴┴┼----┼┴┴┴┴┼
>
>      A    B    C    D               A    B    C    D         
>   ┌----┬┬┬┬┬┬----┬┬┬┬┬┬          ┌----┬┬┬┬┬┬----┬┬┬┬┬┬
> 1 |    ||⛁ ||    ||||||       1  |    ||||||    ||||||   
>   ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼          ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼
> 2 ||||||    ||||||    |   ->   2 ||||||    ||⛀ ||    |       ✘ Lance inválido!
>   ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼          ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼
> 3 |    ||||||    ||||||        3 |    ||||||    ||⛁ ||
>   ├----┼┴┴┴┴┼----┼┴┴┴┴┼          ├----┼┴┴┴┴┼----┼┴┴┴┴┼
>
> A captura é obrigatória.
>
> Não existe sopro.
> (Regra do sopro: Se um jogador deixa de capturar uma peça do adversário quando tem a obrigação de fazê-lo, o adversário pode “soprar” (ou retirar) a peça que deveria ter feito a captura.)
>
> Duas ou mais peças juntas, na mesma diagonal, não podem ser capturadas.
> Exemplo: Jogador preto faz o movimennnto B1 -> E4 com uma pedra preta
>
>      A    B    C    D    E                A    B    C    D    E
>   ┌----┬┬┬┬┬┬----┬┬┬┬┬┬----┬          ┌----┬┬┬┬┬┬----┬┬┬┬┬┬----┬
> 1 |    ||⛂ ||    ||||||    |       1  |    ||||||    ||||||    |
>   ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼          ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼
> 2 ||||||    ||⛀ ||    ||||||       2  ||||||    ||||||    ||||||
>   ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼   ->     ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼      ✘ Lance inválido!
> 3 |    ||||||    ||⛀ ||    |       3  |    ||||||    ||||||    |
>   ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼          ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼
> 4 ||||||    ||||||    ||||||        4 ||||||    ||||||    ||⛂ ||
>   ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼          ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼
>
> A pedra captura a dama e a dama captura a pedra.
> Pedra e dama têm o mesmo valor para capturarem ou serem capturadas. 
>
> A dama podem capturar tanto para frente como para trás, uma ou mais peças.
> Exemplo:
>
>      A    B    C    D               A    B    C    D 
>   ┌----┬┬┬┬┬┬----┬┬┬┬┬┬          ┌----┬┬┬┬┬┬----┬┬┬┬┬┬
> 1 |    ||||||    ||||||        1 |    ||||||    ||||||
>   ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼          ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼
> 2 ||||||    ||⛀ ||    |       2  ||||||    ||⛀ ||    |
>   ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼          ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼      ✔ Lance válido!
> 3 |    ||⛁ ||    ||||||  ->   3  |    ||||||    ||||||
>   ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼          ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼
> 4 ||||||    ||⛀ ||            4  ||||||    ||||||    |
>   ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼          ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼
> 5 |    ||||||    ||||||        5 |    ||||||    ||⛁ ||    
>   ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼          ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼
>
>      A    B    C    D               A    B    C    D 
>   ┌----┬┬┬┬┬┬----┬┬┬┬┬┬          ┌----┬┬┬┬┬┬----┬┬┬┬┬┬
> 1 |    ||||||    ||||||        1 |    ||||||    ||⛁ ||
>   ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼          ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼
> 2 ||||||    ||⛀ ||    |       2  ||||||    ||||||    |
>   ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼          ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼      ✔ Lance válido!
> 3 |    ||⛁ ||    ||||||  ->   3  |    ||||||    ||||||
>   ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼          ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼
> 4 ||||||    ||⛀ ||            4  ||||||    ||⛀ ||    |
>   ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼          ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼
> 5 |    ||||||    ||||||        5 |    ||||||    ||||||    
>   ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼          ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼
>
> Se no mesmo lance se apresentar mais de um modo de capturar, é obrigatório executar o lance que capture o maior número de peças.
> 
>       A    B    C    D    E              A    B    C    D    E
>    ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼          ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼                                                                
> 2  ||||||    ||||||    ||||||       2  ||||||    ||||||    ||||||                                                                 
>    ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼          ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼                                                   
> 3  |    ||⛂ ||    ||||||    |       3  |    ||⛂ ||    ||||||    |                            
>    ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼          ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼                                                                         
> 4  ||||||    ||||||    ||||||   ->  4  ||⛀ ||    ||||||    ||||||     ✔ Lance válido!                      
>    ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼          ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼                                                    
> 5  |    ||⛂ ||    ||⛂ ||    |       5  |    ||||||    ||⛂ ||    |                                     
>    ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼          ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼                              
> 6  ||||||    ||⛀ ||    ||||||       6  ||||||    ||||||    ||||||                              
>    ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼          ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼                              
>
> A pedra que durante o lance de captura de várias peças, apenas passe por qualquer casa de coroação, sem aí parar, não será promovida à dama.
>
> Na execução do lance do lance de captura, é permitido passar mais de uma vez pela mesma casa vazia, não é permitido capturar duas vezes a mesma peça. 
>
> Na execução do lance de captura, não é permitido capturar a mesma peça mais de uma vez e as peças capturadas não podem ser retiradas do tabuleiro antes de completar o lance de captura. 
>
> Empate:
> Após 20 lances sucessivos de damas, sem captura ou deslocamento de pedra, a partida é declarada empatada.
> 
>                                      OU
>
> Finais de:
>     2 damas contra 2 damas;
>     2 damas contra uma;
>     2 damas contra uma dama e uma pedra;
>     uma dama contra uma dama e uma dama contra uma dama e uma pedra, são declarados empatados após 5 lances.

----------Fim----------
    """

    print(regras)
    
    jogar = input('Deseja jogar agora? (y/n)')

    if jogar == 'y':
        mn.comeca_jogo()

    else:
        print('> Até a próxima então!')