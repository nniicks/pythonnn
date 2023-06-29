import random

def freq(lista, valor):
    ocorrencia = 0

    for i in range(len(lista)):
        if valor == lista[i]:
            ocorrencia += 1

    return ocorrencia        

def lancamentos(n):
    vetor = [0]*n
    faces = [0]*6

    for i in range(n):
        vetor[i] = random.randint(1,6)

    for j in range(1, 7):
        faces[j-1] = freq(vetor, j)

    return faces

n = int(input())
aux = lancamentos(n)
print(aux)

for i in range(len(aux)):
    ocorrencia = aux[i]/n * 100
    print(f"O número de ocorrências da face {i+1} é {ocorrencia:.0f}%")