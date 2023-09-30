'''Um coletor de mosquitos coleta mosquitos todos os dias durante N dias (0 < N < 1000).
Escreva um programa que leia o valor de N (quantidade de dias) e, em seguida, uma sequência de N linhas,
cada uma delas contendo o número de mosquitos coletados durante a cada dia.
O programa deve imprimir a quantidade e o dia em que foi coletado o menor número de mosquitos.

OBS: Os teste consideram que não haverá repetição de quantidade de mosquitos coletados em dias distintos.

Por exemplo:

Entrada	Resultado
3
5
6
7
Foram coletados 5 mosquitos no dia 1
10
45
3
23
67
5
8
56
9
3
2
Foram coletados 2 mosquitos no dia 10'''

n = int(input())
menor_quant = int(input())
dia = 1

for i in range(n-1):
    aux = int(input())

    if aux < menor_quant:
        menor_quant = aux
        dia = i + 2

print(f"Foram coletados {menor_quant} mosquitos no dia {dia}.")        