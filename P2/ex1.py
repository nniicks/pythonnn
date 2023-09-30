'''Escreva um programa que leia um valor n (n > 0) e, em seguida, leia um conjunto de n números inteiros.
O programa deve exibir a quantidade de números positivos (maiores que zero) e a quantidade de números negativos (menores que zero).
O programa também deve exibir a quantidade de números pares e a quantidade de números ímpares lidos. Considere que o valor zero é par.
A saída deve ter o formato que segue os exemplos abaixo.
Por exemplo:

Entrada	Resultado
4
8
7
2
0
Dos 4 números lidos, são 3 valores positivos e 0 valores negativos.
Dos 4 números lidos, são 3 valores pares, 1 valores impares.
5
1
2
3
4
5
Dos 5 números lidos, são 5 valores positivos e 0 valores negativos.
Dos 5 números lidos, são 2 valores pares, 3 valores impares.'''


n = int(input())
pos = 0
neg = 0
par = 0
impar = 0

for i in range(n):
    num = int(input())

    if num % 2 == 0 and num > 0:
        par += 1
        pos += 1

    elif num % 2 == 0 and num < 0:
        par += 1
        neg += 1

    elif num % 2 != 0 and num > 0:
        impar += 1
        pos += 1

    elif num %2 != 0 and num < 0:
        impar += 1
        neg += 1

    else:
        par += 1

print(f"Dos {n} números lidos, são {pos} valores positivos e {neg} negativos.")
print(f"Dos {n} números lidos, são {par} pares, {impar} valores impares.")