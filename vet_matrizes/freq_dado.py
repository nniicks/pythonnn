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

'''-------------frequencia tbm---------'''  

import random

def roleta(n):
	vetor = [0]*n
	
	for i in range(len(vetor)):
		vetor[i] = random.randint(0,36)
		
	return vetor

def freq(lista, valor):
	ocorrencia = 0

	for i in range(len(lista)):
		if lista[i] == valor:
			ocorrencia +=  1
	
	return ocorrencia
	
valores = [0]*37

aux = roleta(int(input()))
print(aux)

for i in range(len(valores)):
	valores[i] = freq(aux, i)
	
for j in range(len(valores)):
	frequencia = valores[j]/len(valores) * 100
	print(f"A frequência do valor {j} foi {frequencia:.0f}%")