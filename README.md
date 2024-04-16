# Projeto A3 em Modelos, métodos e técnicas da engenharia de software (2024.1) - Snake Game

## Conceito

---

O projeto trata de uma versão de um dos vídeo-games _arcade_ mais populares, ainda que simples, do mundo.
Nele, o jogador deve controlar uma personagem que se assemelha a uma cobra e "manobrá-la" com as setas do teclado na
direção de um objeto que representa a comida.

Nessa versão do programa escrita em Python, a cobra é estendida em um segmento a cada vez que interage com um objeto comida, que logo assume
uma outra posição aleatória no cenário definido por paredes, aumentando a dificuldade do jogo.

O objetivo do jogo é atingir o maior _score_ possível. O placar é apontado no topo da tela. Ele registra a pontuação
do jogo atual, bem como a pontuação máxima já atingida pelo usuário em jogos anteriores (o arquivo `data.txt` é carregado
a cada execução do programa e ele guarda essa informação).

## Como jogar

---

Ao executar o programa, selecione, no menu principal, dentre as opções:

- Pressione a tecla `R` para visualizar as regras;
- Pressione a tecla `Enter` para iniciar um novo jogo;
- Pressione a tecla `Esc` para sair do jogo;

Ao iniciar o jogo:

- Use as setas do teclado `←`, `↑`, `→`, `↓` para controlar a cobra em direção à comida.
- Evite colidir com as paredes e com o corpo/cauda da própria cobra.

## Recursos utilizados

---

### Módulos

- [random](https://docs.python.org/3/library/random.html#module-random)
- [turtle graphics](https://docs.python.org/3/library/turtle.html#module-turtle)
- [time](https://docs.python.org/3/library/time.html)
