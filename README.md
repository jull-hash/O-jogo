README - JJJACKSPOT
Introdução
Este projeto consiste em um jogo, onde dois jogadores batalham e o jogador que digitar o maior número vence.
O projeto foi desenvolvido inteiramente em linguagem Python. O jogo é executado no terminal e oferece uma experiência interativa e divertida. O objetivo é apresentar um processo de CRUD completo.
Propósito
O principal propósito do JJJOGO é funcionar como um jogo simples de duelo entre dois jogadores, utilizando Redis como meio de comunicação entre as máquinas.
 Ele serve como um projeto de entretenimento e também como um exercício prático de programação, explorando conceitos como, comunicação entre processos usando Redis, manipulação de entrada do usuário,lógica de comparação e exibição de resultados.

Funcionalidades
O script, desenvolvido em Python, simula um duelo numérico entre dois jogadores com as seguintes funcionalidades principais:
🎮 Sistema de Salas
O jogador pode criar uma sala ou entrar em uma sala existente.


Cada sala utiliza um registro no Redis para armazenar as jogadas (p1 e p2).


⚔️ Mecânica de Jogo
Cada jogador escolhe um número (apenas valores numéricos).


Assim que ambos enviam suas jogadas, o programa simula uma “animação de batalha” com números aleatórios.


O número maior vence.


🔄 Sincronização via Redis
O Player 1 envia sua jogada e espera até que Player 2 jogue.


O Player 2 faz o mesmo.


O Redis armazena temporariamente ambas as jogadas e permite que o resultado seja calculado.


🏆 Resultado
Se o número do Player 1 for maior, ele vence.


Se o número do Player 2 for maior, ele vence.


Se forem iguais, o resultado é empate.


Após o duelo, a sala é limpa do Redis.


🎬 Interface Animada
O jogo exibe breves animações de texto ao abrir.


Durante a espera pela jogada do outro jogador, um mini “relógio animado” fica alternando no terminal.


Ao calcular o resultado, a tela mostra uma sequência rápida de números simulando a batalha.



Como Usar
Pré-requisitos
Antes de executar o jogo, certifique-se de:
Ter o Python instalado.


Ter o Redis instalado e em execução na máquina.


O código espera o Redis em:


host: 127.0.0.1


porta: 6379


Instalar a biblioteca Python necessária:


pip install redis

Executando o Jogo
Salve o código em um arquivo, por exemplo:
 jjjogo.py


Abra o terminal e navegue até a pasta onde o arquivo foi salvo.


Execute o script:


python jjjogo.py

No menu inicial, escolha:


1 para criar uma sala


2 para entrar em uma sala existente


Após entrar na sala:


Digite um número para fazer sua jogada.


Aguarde a jogada do outro jogador.


O jogo mostrará a animação e calculará o vencedor.



Créditos
Este projeto foi desenvolvido por:
Jailine Coelho Santos


Juliana Laura Silva Leite


Julio Da Cruz Neto

Matheus Mafra Mianes




