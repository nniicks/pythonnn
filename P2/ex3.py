'''Escreva um programa em Python que faça uso de laços aninhados para imprimir o padrão abaixo.
Devem ser lidos um valor inteiro N (N >= 0) que representa a quantidade de caracteres da primeira linha.
Observe que, a cada linha é impresso um caractere a menos do padrão.
Por exemplo:

Entrada	Resultado
7
*******
******
*****
****
***
**
*
4
****
***
**
*'''

'''N = int(input())
aux = "*" * N

for i in range(N):
    print(aux)

    N -= 1

    aux = "*" * N'''

char = "*"
n = int(input())

for i in range(n):

    for j in range(n, i, -1):
        print(char, end="")

    print()    

        