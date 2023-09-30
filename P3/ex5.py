'''Com a chegada das festividades de fim de ano, uma famosa loja de brinquedos está repleta de clientes em busca dos presentes perfeitos para seus filhos.
As filas nos caixas estão cada vez maiores, e as pessoas esperam ansiosamente para realizar suas compras.

Para garantir um atendimento eficiente, a loja adotou um sistema de controle de filas. Quando alguém desiste de esperar na fila,
as pessoas que estavam atrás dela avançam uma posição, preenchendo o espaço vago. Dessa forma, a fila sempre se mantém contínua, sem espaços vazios entre os clientes.

Pedro é um dos funcionários da loja e está curioso para saber como a fila se reorganiza quando alguém desiste.
Ele observa atentamente a dinâmica das filas e decide criar um programa em Python para simular esse comportamento.

O programa desenvolvido por Pedro recebe como entrada o número inicial de pessoas na fila, a lista dos identificadores das pessoas na ordem de chegada,
o número de pessoas que deixaram a fila e a lista dos identificadores das pessoas que desistiram, na ordem em que saíram.

A sua tarefa é ajudar Pedro a desenvolver esse programa. Ele precisa determinar o estado final da fila, ou seja, a lista dos identificadores das pessoas
que permaneceram na fila após as desistências, mantendo a ordem de chegada.

Escreva um programa em Python que realize essa tarefa. O programa deve receber como entrada o número inicial de pessoas na fila, seguido pelos identificadores
das pessoas na ordem de chegada. Em seguida, deve ler o número de pessoas que desistiram e, por fim, os identificadores das pessoas que desistiram,
na ordem em que saíram.

O programa deve imprimir na tela a lista dos identificadores das pessoas que permaneceram na fila, em ordem de chegada.

A entrada do seu programa tem 4 linhas. A primeira linha contém um número inteiro N, representando a quantidade inicial de pessoas na fila.
A segunda linha contém N inteiros, representando os identificadores das pessoas na fila em ordem de chegada. A terceira linha contém um número inteiro M,
representando a quantidade de pessoas que desistiram da fila. A quarta linha contém M inteiros, representando os identificadores das pessoas que
desistiram da fila na ordem em que saíram.

O programa deve imprimir, como saída, uma linha contendo N - M inteiros, representando os identificadores das pessoas que permaneceram na fila, em ordem de chegada.

OBS: Você não pode usar a função remove do Python para resolver esse problema.

Por exemplo:

Entrada	Resultado
6
50 60 70 80 90 100
1
100
50 60 70 80 90
6
10 20 30 40 50 60
3
20 30 60
10 40 50'''


n = int(input())
pessoas = input().split()
resposta = []

for i in range(len(pessoas)):
    pessoas[i] = int(pessoas[i])

qs = int(input())
saidas = input().split()

for i in range(len(saidas)):
    saidas[i] = int(saidas[i])

for j in range(len(pessoas)):
    if pessoas[j] not in saidas:
        resposta.append(pessoas[j])

for k in range(len(resposta)):
    print(resposta[k], end=" ")