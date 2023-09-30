'''O Serviço de Meteorologia Capivara registra a temperatura na cidade de Cachorro Sentado em três locais distintos e quatro vezes ao dia.
O programador Codificador Bom da Silva foi convidado para fazer um programa para computar a temperatura média em cada um dos horários que a temperatura foi medida.
Para isso ele usou um arranjo bidimensional 4 × 3 chamado tabTemp. Em cada uma das linhas ele registrou a temperatura obtidas nos três locais a cada vez que
a temperatura foi registrada. Ajude o programador Codificador Bom da Silva a finalizar a tarefa.

Para isso, projete e implemente um programa que leia as 3 temperaturas nos respectivos locais, 4 vezes ao dia (seis horas, meio dia, dezoito horas e meia noite),
calcule a temperatura média em cada um dos horários em que temperatura foi registrada, e imprima os resultados.
Utilize um vetor tempMed para armazenar a temperatura média em cada uma das vezes que ela foi coletada.
Os valores das temperaturas são medidos com pelo menos uma casa decimal.

Abaixo uma sugestão de estrutura de dados para resolver o problema.

# Passo 1.1. Estruturas para armazenar a tabela e as médias
tabtemp = [[0.0]*3 for i in range(4)]
media = [0.0]*4

A entrada é dada por uma matriz (4 x 3) de números reais, representando a tabela com as temperaturas.
A matriz representa as temperaturas da cidade em um dado dia e cada linha da matriz representa as temperaturas de três locais distintos da cidade onde as medidas
foram efetuadas. A saída deve usar o formato abaixo:

 

# Passo 3. Imprima a Temperatura média em cada horário
saida = [round(item,1) for item in media]
print(saida)

Por exemplo:

Entrada	Resultado
25.5 28.7 22.2 
28.8 28.9 24.5 
30.4 29.4 26.3
28.5 29.1 25.8
[25.5, 27.4, 28.7, 27.8]
15.5 18.7 22.2
18.8 18.9 24.5
20.4 19.4 22.3
18.5 19.1 15.8
[18.8, 20.7, 20.7, 17.8]'''



m = [[0.0]*3 for i in range(4)]

for i in range(4):
    linha = input().split()

    for j in range(len(linha)):
        linha[j] = float(linha[j])
    m[i] = linha

saida = []
media = []

for i in range(len(m)):
    soma = 0
    for j in range(len(m[0])):
        soma += m[i][j]
    saida.append(soma)

for k in range(len(saida)):
    a = saida[k] / 3
    media.append(round(a,1))

print(media)