'''def cria_matriz0, cria_matriz1 e cria_matriz2 recebe quant de linhas e colunas e tbm todos os elementos
que deverao compor a matriz na forma de uma lista(vetor), e cria uma matriz. a diferença mesmo esta  em como
cada uma delas faz isso. e tbm a cria_matriz2, dispoe os elementos de forma diferente'''

def cria_matriz1(linhas ,colunas ,lista):
    m = matriz_nula(linhas, colunas)

    for i in range(linhas):
        for j in range(colunas):
            m[i][j] = lista[colunas*i + j]

    return m       
 

def cria_matriz2(linhas, colunas, lista):#disponho os elementos da lista na vertical(ou seja, em colunas)
    m = matriz_nula(linhas, colunas)

    for i in range(colunas):
        for j in range(linhas):
            m[j][i] = lista[linhas*i + j]

    return m

def cria_matriz0(quantL, quantC, lista): 
    matriz = []

    for i in range(quantL):
        linha = []

        for j in range(quantC):
            linha.append(lista[j])

        matriz.append(linha)
        lista = lista[j+1:]

    return matriz

           
def soma(A, B):
    C = []

    #verificar se A e B tem a mesma ordem(daria pra usar um try except tbm)
    nlinA = len(A)
    ncolsA = len(A[0])
    nlinB = len(B)
    ncolsB = len(B[0])

    if nlinA == nlinB and ncolsA == ncolsB:

        for i in range(nlinA):
            
            linha = [0]*ncolsA
            C.append(linha)

            for j in range(ncolsA):
                C[i][j] = A[i][j] + B[i][j]
                #C[i][j] = A[i][j] - B[i][j] = subtração :D

    else:
        print("Matrizes não possuem a mesma ordem")

    return C

'''a subtraçao tem uma outra maneira de fazer. seria somar a matriz A com a oposta de B(negar
todos os seus elementos, ou seja, mudar o sinal de todo mundo)'''

def oposta(M):
    op = []

    for i in range(len(M)):
        linha = [0]*len(M[0])
        op.append(linha)
        for j in range(len(M[0])):
            op[i][j] = -M[i][j]

    return op        


def subtrair(A, B):
    return soma(A, oposta(B))


def matriz_nula(lin, cols):
    M = []

    for i in range(lin):
        linha = [0]*cols
        M.append(linha)

    return M

def transposta(M):
    nlinhas = len(M)
    ncols = len(M[0])

    T = matriz_nula(ncols, nlinhas)
    
    for i in range(nlinhas):
        for j in range(ncols):
           T[j][i] = M[i][j]


    return T       
                            
 
def igual(A,B):
    #se n possuirem a mesma ordem, elas n vao ser iguais
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        flag = True

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != B[i][j]:
                    flag = False

        if flag ==  True:
            print("são iguais!")
        else:
            print("possuem a mesma ordem, mas não são iguais!")

    else:
        print("não possuem a mesma ordem, logo não há possibilidade de serem iguais!")


def mul_matrizes(A, B):
    lA = len(A)
    cA = len(A[0])
    lB = len(B)
    cB = len(B[0])

    if cA == lB or cB == lA:
        C = []

        for linha in range(lA):
            C.append([])

            for coluna in range(cB):
                C[linha].append(0)

                for i in range(cA):
                    C[linha][coluna] += A[linha][i] * B[i][coluna]


        return C
    else:
        print("Não é possível multiplicar essas matrizes")
       
def le_matriz(nLinhas, nColunas):
    matriz = []

    for i in range(nLinhas):
        linha = []
        for j in range(nColunas):
            linha.append(float(input(f"Informe o elemento a{i+1}{j+1}: ")))

        matriz.append(linha)

    return matriz

def exibir_matriz(M):
    for linha in range(len(M)):
        print(M[linha])

    #for linha in M:
       # print(linha)

def Linhas_Colunas():
    num_linhas = int(input("Informe a quantidade de linhas da matriz: "))
    num_cols = int(input("Informe a quantidade de colunas da matriz: "))

    return le_matriz(num_linhas,num_cols)