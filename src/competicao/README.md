# Connect4 PopOut

## Integrantes

- Bruno Freitas de Nascimento Rodrigues
- Guilherme Ricchetti
- Nicolas Byung Kwan Cho

---

## O jogo

O projeto implementa uma versão de [Connect4 (Lig4)](https://en.wikipedia.org/wiki/Connect_Four) em que é possível que um jogador, durante sua jogada, retire alguma peça 
**sua** do tabuleiro desde que esta se encontre na última linha (mais inferior). No caso, será usado um tabuleiro 7 x 6 que será representado por uma matriz. 
Cada jogador será identificado por um número, 1 ou 2, e as peças no tabuleiro serão codificadas pelo número de seu respectivo jogador. Uma casa sem peça de nenhum jogador
será representada por 0. Logo, o tabuleiro de início é dado por:

```
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
```
Supondo que o jogador 1 coloque na coluna central:

```
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 1 0 0 0
```
E, em seguida, o jogador 2 também coloque na mesma coluna:

```
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 2 0 0 0
    0 0 0 1 0 0 0
```

E o jogo segue até que pelo menos 4 peças consecutivas de um jogador estejam presentes.

---

## Desenvolvendo um agente

A ideia para desenvolver um agente autônomo que consiga jogar Connect4 parte do algoritmo de Min-Max. Como essa versão do jogo envolve a possibilidade de retirar peças
da última linha, não estamos limitados apenas a eventualmente preencher todos as casas do tabuleiro. Logo, o espaço de busca do Min-Max é consideravelmente maior do que a 
versão mais simples do jogo. 

Assim, para que seja possível fazer jogadas em menos de 5 segundos o agente deve ter uma limitação em relação a profundidade da árvore de busca. Além disso, para evitar de 
explorar por caminhos não promissores (desnecessários) na árvore, utilizamos uma poda Alpha-Beta que compensa em um aumento na profundidade possível a ser explorada. No caso,
é utilizada uma **profundidade de 5** camadas.

---

## Base de conhecimento

Como o agente não é capaz de resolver o jogo no tempo e recursos disponíveis, precisamos atribuir uma função utilidade que classifica os estados na camada mais profunda 
do Min-Max. Para determinar se um tabuleiro é desejável ao agente, utiliza-se uma diferença da contagem de trincas e duplas de peças no tabuleiro para cada jogador. Assim, 
se em determinado estado apresenta muitas trincas de peças do agente e poucas do oponente, então é um estado muito desejado para o agente.

Além disso, o agente tende a estados que possui maiores quantidades de peças na região central. Devido ao fato de dominar o centro ser uma estragtégia 
aparentemente vantajosa, pois permite mais possibilidades de conectar 4, estados com esta característica recebem um adicional ao atribuir um valor na função de utilidade, 
se comparado aos estados com menos peças nas colunas centrais.

Como não foi utilizada uma base de conhecimento tão complexa para determinar os valores de tabuleiro, nem uma poda mais elaborada para otimizar tempo de processamento e 
profundidade, espera-se que o agente tenha um desempenho razoável. Caso outros agentes desenvolvidos para competição possuam conhecimentos melhores e o algoritmo Min-Max tenha 
sido otimizado, nosso agente não performará tão bem na competição. 

Em relação a outros jogadores (jogadores manuais e aleatórios), o agente performa bem, tendo obtido vitória constante contra o jogador aleatório e ainda nenhuma derrota
contra jogadores manuais.

---
## Diferenças entre o jogo clássico e PopOut

Em relação a árvore de busca, a versão PopOut do jogo deve apresentar uma árvore consideravelmente maior do que a versão clássica, uma vez que a clássica é limitada pelo 
preenchimento de todos os espaços no tabuleiro, enquanto o comando de popout da outra versão cria novas possibilidades de ações, tornando o jogo possivelmente infinito.
Em termos de função de avaliação não deve haver muita diferença para versão clássica, uma vez que trincas e domínio do centro permanecem sendo condições desejadas ao
agente. 

Sendo assim, seria possível utilizar o jogador da versão PopOut na versão clássica apenas modificando as ações válidas a cada jogada.

---

## Referências para implementação

Como referência para implementação do agente foram utilizados os conteúdos disponíveis em:

* http://blog.gamesolver.org/solving-connect-four/01-introduction/
* http://fbarth.net.br/Connect4-Python/

Além da base do código estar disponível em:

* https://github.com/Insper/ai_code/blob/main/src/games/fourinrow/BarthPlayer.py

que implementa um agente para o jogo Connect4 clássico.
