'''Escreva um programa que leia um número inteiro (de 1 a 12) que representa um mês do ano.
O programa deve exibir uma mensagem indicando se o mês está no primeiro trimestre, no segundo trimestre, no terceiro trimestre ou no quarto trimestre do ano.

A seguir estão os orientações:

Se for lido 1, 2 ou 3, o programa deve imprimir "Primeiro trimestre".
Se for lido um número de 4 a 6, deve ser impresso "Segundo trimestre".
Se o número for 7, 8 ou 9, deve ser impresso "Terceiro trimestre".
Se o número for 10, 11 ou 12, deve ser impresso "Quarto trimestre".
Se o número não estiver entre 1 e 12, o programa deve exibir uma mensagem de erro: "Mês inválido".
Por exemplo:

Entrada	Resultado
2
Primeiro trimestre
15
Mês inválido'''

n = int(input())

if n < 1 or n > 12:
    print("Mês inválido")

elif n >= 1 and n <= 3:
    print("Primeiros semestre")

elif n >= 4 and n <= 6:
    print("Segundo semestre")

elif n >= 7 and n <= 9:
    print("Terceiro trimestre")

elif n >= 10 and n <= 12:
    print("Quarto trimestre")
    