'''Os gestores da Fazenda Verde Vida planejam criar uma nova plantação de alface, no formato retangular.
Eles querem escolher o melhor lugar para a nova horta e, para isso, têm vários locais possíveis, com diferentes dimensões de comprimento e largura.
Para os gestores, o ideal é escolher o local que possua a maior área. Eles gostariam de ter um programa de computador que,
dadas as dimensões das prováveis áreas, determina o que tem maior área. Você foi contatado pela fazenda para prestar esse serviço.

A entrada do seu programa consiste de uma linha contendo um valor inteiro N, que representa o número de áreas prováveis para a plantação de alfaces. Em seguida, se programa deve ler N linhas, cada uma contendo dois números inteiros que indicam as dimensões (comprimento e largura) de cada um dos possíveis locais. As dimensões são dadas em metros. Os valores de comprimento e largura estão entre 1 e 100, incluindo esses valores (ou seja, 1 ≤ comprimento ≤ 100 e 1 ≤ largura ≤ 100).

A saída do seu programa deve ser uma linha contendo informando a área, em metros quadrados, do melhor local escolhido para a plantação de alface, conforme exemplos abaixo.

Por exemplo:

Entrada	Resultado
5
5 4
3 7
13 17
2 1
9 8
A maior área encontrada tem 221 metros quadrados.
4
1 2
3 4
5 6
6 8
A maior área encontrada tem 48 metros quadrados.'''


n = int(input())
comp,larg = map(int,input().split())
maior_area = comp * larg

for i in range(n-1):
    comp,larg = map(int,input().split())

    aux = comp * larg

    if aux > maior_area:
        maior_area = aux

print(f"A maior área encontrada tem {maior_area} metros quadrados.")