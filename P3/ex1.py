'''João e Maria tinham suas explorações matemáticas e encontraram um novo desafio envolvendo números perfeitos.
Um número perfeito é aquele cuja soma dos seus divisores próprios (excluindo o próprio número) é igual ao próprio número.

Os amigos decidiram criar um programa para verificar se um número é perfeito.
Para isso, eles escreveram uma função chamada calcula_divisores que recebe um valor inteiro e retorna um vetor contendo todos os divisores do número.
Em seguida, eles implementaram uma função chamada eh_perfeito que recebe um número inteiro como argumento e retorna o valor lógico VERDADEIRO se o número for perfeito,
ou FALSO caso contrário. Observe que a função eh_perfeito usa a função calcula_divisores como parte dessa análise.

Sua tarefa é construir as funções calcula_divisores e eh_perfeito em Python e um programa que leia um valor n, seguido por n números inteiros.
Usando as funções construídas por você, imprima uma mensagem para cada número lido, dizendo se é um número perfeito ou não,
conforme o modelo apresentado nos exemplos abaixo.

Por exemplo:

Entrada	Resultado
4
2
13
19
31
O número 2 não é perfeito.
O número 13 não é perfeito.
O número 19 não é perfeito.
O número 31 não é perfeito.
3
12
28
9
O número 12 não é perfeito.
O número 28 é perfeito.
O número 9 não é perfeito.'''

def divisores(n):
    div = []

    if n >= 0:
        for i in range(1, n//2 + 1):
            if n % i == 0:
                div.append(i)

    '''else:
        for i in range(n, abs(n)+1):
            if i == 0:
                continue
            if n % i == 0:
                div.append(i)'''

    return div

def eh_perfeito(N):
    dividers = divisores(N)
    soma = 0

    for i in range(len(dividers)):
        soma += dividers[i]

    if soma == N:
        return print(f"O número {N} é perfeito.")
    else:
        return print(f"O número {N} não é perfeito.")

n = int(input())

for i in range(n):
    numero = int(input())
    eh_perfeito(numero)
