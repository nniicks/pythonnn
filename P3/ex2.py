'''A empresa "Produtividade Eficiente" é conhecida por sua busca incessante em melhorar o desempenho de seus funcionários.
Eles monitoram a produção de cada colaborador em determinado período e analisam os resultados para identificar oportunidades de crescimento.

Para aprimorar essa análise, a empresa contratou uma especialista em matemática chamada Carla.
Sua missão é desenvolver um programa que leia a sequência de valores inteiros correspondente à produção de cada funcionário em um único dia.
Com base nesses dados, Carla precisa calcular a média da produção, determinar a quantidade de funcionários cuja produção é menor do que a média e identificar
a maior e menor produção do dia.

Carla decidiu utilizar um vetor para armazenar os dados de entrada e implementar suas próprias funções, sem utilizar as funções pré-existentes como min, max, sum ou
average, a fim de aprimorar ainda mais suas habilidades matemáticas.

Sua tarefa é ajudar Carla a desenvolver esse programa em Python. Ele deve ler a sequência de valores inteiros correspondentes à produção de cada
funcionário em um único dia, calcular a média da produção, determinar a quantidade de funcionários cuja produção é menor do que a média e identificar o
funcionário com a maior e menor produção.

Ao final, o programa deve imprimir a média da produção (com uma casa decimal), a quantidade de funcionários cuja produção é menor do que a média, a
maior produção e a menor produção do dia, conforme o modelo apresentado nos exemplos abaixo.

Considere que a sequência de entrada terá pelo menos um valor.

Por exemplo:

Entrada	Resultado
20 18 25
Média de produção: 21.0
Quantidade de funcionários com produção abaixo da média: 2
Funcionário com maior produção: 25
Funcionário com menor produção: 18
10 12 8 15 9
Média de produção: 10.8
Quantidade de funcionários com produção abaixo da média: 3
Funcionário com maior produção: 15
Funcionário com menor produção: 8'''

producao = [int(i) for i in input().split()]
total = 0
func_abaixo = 0
func_maior = producao[0]
func_menor = producao[0]

for i in range(len(producao)):
    total += producao[i]

media = total / len(producao) 

for j in range(len(producao)):
    if producao[j] < media:
        func_abaixo += 1

for k in range(len(producao)):
    if producao[k] > func_maior:
        func_maior = producao[k]

for n in range(len(producao)):
    if producao[n] < func_menor:
        func_menor = producao[n]

print(f"Média de produção: {media:.1f}")
print(f"Quantidade de funcionários com produção abaixo da média: {func_abaixo}")
print(f"Funcionário com maior produção: {func_maior}")
print(f"Funcionário com menor produção: {func_menor}")