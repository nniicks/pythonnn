def matriz_nula(lin, cols):
    M = []

    for i in range(lin):
        linha = [0]*cols
        M.append(linha)

    return M
def cria_matriz1(linhas ,colunas ,lista):
    m = matriz_nula(linhas, colunas)

    for i in range(colunas):
        for j in range(linhas):
            m[j][i] = lista[linhas*i + j]

    return m
a = [457,0,-78,347,1,2]
b = cria_matriz1(3,2,a)

for i in range(len(b)):
    print(b[i])