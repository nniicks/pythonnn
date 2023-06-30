def matriz_nula(lin, cols):
    M = []

    for i in range(lin):
        linha = []
        for j in range(cols):
            linha.append(0)
        M.append(linha)

    return M    

def cria_matriz1(linhas ,colunas ,lista):
    m = matriz_nula(linhas, colunas)

    for i in range(colunas):
        for j in range(linhas):
            m[j][i] = lista[colunas*i + j]

    return m
a = [123,440,33,50]
b = cria_matriz1(2,2,a)

for i in range(len(b)):
    print(b[i])