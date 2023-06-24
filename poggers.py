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
        print(f"O número {aux} número não é palíndromo!")


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