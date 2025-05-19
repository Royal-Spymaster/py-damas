# Damas em py

Damas fodas por Pedro Foda (2 de 4 jogo no roadmap dos jogos):

A adaptação visual que queria antes vai ficar para o xadrez, estipulando uma lógica mental basica parece mais fácil com POO(?) e com alguma biblioteca, coisas que me privei de usar ao programar as damas. POO não me pareceu muito útil e as bibliotecas eu teria que ficar pesquisando, parece que eu ia perder muito tempo para montar um frankenstein.

## Update #1

uhhhhh eu não upei meu progresso anterior no git, então eu vou listar os problemas que eu tive (i.e. problemas que eu demorei mais de dia para resolver) até aqui e as soluções que eu encontrei (vou tentar fazer em ordem cronológica).

### Montagem do tabuleiro

Tecnicamente, eu tive um problema no começo, que por algum motivo eu decidi usar um dicionário invés de listas dentro de listas (sei la). Depois de tentar fazer os dicionarios funcionarem com alguns algoritmos e funções, eu desisti e recomecei.

### Problemas com diagonais

No começo, eu queria fazer uma validação de jogadas baseada no cálculo de diagonais. Acontece que o código ficou muito confuso e por mais que eu tenha até que chego num código simples no final, uma parte das diagonais não parava de dar problemas. Eu resolvi esse problema mudando o algoritmo para calcular distâncias, definindo condicionais de contorno, para evitar out of range causado por operações na acessa_tile().

### Algum problema estranho com variáveis

Eu tenho algum problema atribuindo variáveis globais nas funções, especificamente, as que envolvem o jogador. É algo simples, mas eu não sei se a solução que eu encontrei é de fato a certa (parece ser pelas páginas do stack q eu li). Esse é um problema mais teórico do que prático e na verdade mesmo, está mais para um incomo do que um problema de verdade.

### constroi_"linha"()

Só por causa de uma inversão no resultado da come_mais() eu percebi que a constroi_linha() construia colunas. Não foi nada de mais, mas o problema é que como essa foi a PRIMEIRA FUNÇÃO que eu fiz (até porque eu preciso do tabuleiro antes de tudo), talvez nem mude muita coisa, mas vou ter que revisar tudo e fazer os ajustes necessários (aproveitei para finalmente upar tudo no git e abrir uma branch para isso).

## Update #2

Problemas concertador até aqui, o jogo roda normalmente, sem promover peças. Agora eu vou começar a desenvolver as ações da rainha. A minha ideia é inicial se baseia em ver até onde vão as 4 diagonais e o que tem nelas, quase como eu faço com a analisa jogada. Talvez seja bom modularizar mais o código para fazer com que as funções funcionem com ambas as peças.

## Update #3

Agora que eu tenho o jogo em git, eu consigo escrever uma "documentação" mais detalhada, mesmo já próximo (espero eu) da conclusão do jogo. Além dessa parte mecânica, eu gostaria de estruturar a parte das regras com imagens do tabuleiro - que não deve ser algo muito complexo, apenas trabalhoso.

### Desenvolvimento teórico inicial das interações da rainha com o tabuleiro

A rainha tem interações únicas para tanto para movimentação quanto para comer peças. Resumidamente, a Rainha pode se movimentar livremente pelas diagonais delimitadas por peças da mesma cor, ou por diagonais com somente uma peça da cor oposta. Depois caso a rainha coma uma peça da cor oposta, é preciso analisar se há outras oportunidades de comer outras peças
