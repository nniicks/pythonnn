def matriz(lin,col):
    m = [[0]]*lin
    linha = [0]*col
    
    for i in range(lin):
        m[i] = linha

    for l in range(lin):
        aux = [int(i) for i in input().split()]
        m[l] = aux
    
    print(m)
    return m

def mult(M,vetor):
    saida = [0]*len(M)

    for i in range(len(M)):
        soma = 0
        for j in range(len(M[0])):
            soma += M[i][j] * vetor[j]
            saida[i] = soma
    return saida

linhas = int(input())
colunas = int(input())
vet = [int(i) for i in input().split()]
mat = matriz(linhas,colunas)
print(mult(mat,vet))

