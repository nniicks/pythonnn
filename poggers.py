def palindromo(N):
    aux = N
    inverso = 0

    while N > 0:
        
        resto = N % 10
        inverso = inverso * 10 + resto
        N = N // 10

    if inverso == aux:
        print(f"O número {aux} número é palíndromo!")

    else:
        print(f"O número {aux} número NÃO é palíndromo!")


def raiz_exata(N):
    aux = int(N**0.5)

    if aux*aux == N:
        print(f"O número {N} possuí raíz exata!")

    else:
        print(f"O número {N} NÃO possuí raiz exata!")
    

def superquadrado(N):
    aux = str(N)
    vezes = len(aux)
    quadr_perf = False

    for i in range(vezes - 1):
        numero = int(aux[i])*10 + int(aux[i+1])
        raiz = int(numero**0.5)

        if raiz**2 != numero:
            quadr_perf = False
            break

        else:
            quadr_perf = True

    if quadr_perf == True:
        return print(f"O número {N} é superquadrado!")

    else:
        return print(f"O número {N} NÃO é superquadrado!")


def eh_primo(N):

    for i in range(2, N//2 + 1):
        if N % i == 0:
            return print(f"O número {N} NÃO é primo!")

    return print(f"O número {N} é primo!")

def divisores(n):
    div = []

    if n >= 0:
        for i in range(1, n//2 + 1):
            if n % i == 0:
                div.append(i)

    else:
        for i in range(n, abs(n)+1):
            if i == 0:
                continue
            if n % i == 0:
                div.append(i)

    return div

def eh_perfeito(N):
    dividers = divisores(N)
    soma = 0

    for i in range(len(dividers)):
        soma += dividers[i]

    if soma == N:
        return True
    else:
        return False
