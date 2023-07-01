def prod_escalar(x, y):
    resultado = 0

    for i in range(len(x)):
        resultado += x[i] * y[i]

    return resultado

n = int(input("Digite o tamanho dos vetores em questão: "))
vet1 = [0]*n
vet2 = [0]*n

for i in range(n):
    vet1[i] = int(input(f"Digite a {i+1}o coordenada do primeiro vetor: "))

for j in range(n):
    vet2[j] = int(input(f"Digite a {j+1}o coordenada do segundo vetor: "))

#resposta = prod_escalar(vet1, vet2)
print(f"O produto escalar entre os vetores {vet1} e {vet2} é {prod_escalar(vet1, vet2)}")
