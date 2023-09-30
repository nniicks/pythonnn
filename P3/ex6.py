'''Inspirado e determinado, Ethan decidiu estudar o tabuleiro e desvendar seus segredos.
Ele percebeu que cada quadrado representava um número inteiro e que, quando organizados em uma matriz quadrada de tamanho N × N, poderiam formar um quadrado mágico.

Ethan aprendeu que a verdadeira magia de um quadrado mágico estava em sua propriedade única: a soma de todas as linhas, colunas e diagonais era sempre a mesma.

Animado com a descoberta, Ethan decidiu desenvolver um programa em Python capaz de identificar se um determinado quadrado era mágico ou não,
além de calcular a soma mágica desse quadrado.

Agora, sua tarefa é ajudar Ethan a desenvolver esse programa. Ele precisa ler um conjunto de testes contendo um número N (2 < N < 10) na primeira linha,
seguido por N linhas contendo N inteiros cada. Esses inteiros representam os elementos do quadrado. Seu programa deve imprimir, na saída padrão,
uma única linha com um inteiro representando a soma mágica do quadrado ou -1 caso o quadrado não seja mágico.

Ethan está ansioso para testar seu programa com diferentes quadrados e desvendar mais segredos dos quadrados mágicos da Ilha das Maravilhas.

Por exemplo:

Entrada	Resultado
3
2 9 6
5 1 7
4 3 8
-1
3
2 7 6
9 5 1
4 3 8
15

def verificar_quadrado_magico(quadrado):
    n = len(quadrado)
    soma_magica = sum(quadrado[0])  # Calcula a soma mágica baseando-se na primeira linha

    # Verifica a soma das linhas
    for linha in quadrado:
        if sum(linha) != soma_magica:
            return -1

    # Verifica a soma das colunas
    for coluna in range(n):
        soma_coluna = 0
        for linha in quadrado:
            soma_coluna += linha[coluna]
        if soma_coluna != soma_magica:
            return -1

    # Verifica a soma da diagonal principal
    soma_diagonal_principal = 0
    for i in range(n):
        soma_diagonal_principal += quadrado[i][i]
    if soma_diagonal_principal != soma_magica:
        return -1

    # Verifica a soma da diagonal secundária
    soma_diagonal_secundaria = 0
    for i in range(n):
        soma_diagonal_secundaria += quadrado[i][n - 1 - i]
    if soma_diagonal_secundaria != soma_magica:
        return -1

    return soma_magica


# Leitura do quadrado
n = int(input())
quadrado = []
for _ in range(n):
    linha = list(map(int, input().split()))
    quadrado.append(linha)

# Verifica se é um quadrado mágico e calcula a soma mágica
soma_magica = verificar_quadrado_magico(quadrado)

# Imprime o resultado
print(soma_magica)'''