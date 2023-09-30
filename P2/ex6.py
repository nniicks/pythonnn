'''Um número inteiro N (N > 1) cuja soma dos seus divisores, menores que ele, é menor que próprio número são chamados de números deficientes.
Por exemplo, o número 8 é dito deficiente porque 8 > 1 + 2 + 4. No entanto, o número 18 não é deficiente, pois 18 <= 1 + 2 + 3 + 6 + 9.

Escreva um programa em Python que leia um número inteiro e imprima uma mensagem dizendo se ele é um número deficiente ou não, conforme exemplos abaixo.

Por exemplo:

Entrada	Resultado
18
18 não é deficiente
8
8 é deficiente'''

n = int(input())
div = 0

for i in range(1, n//2 +1):
    if n % i == 0:
        div += i

if n > div:
    print(f"{n} é deficiente")

else:
    print(f"{n} não é deficiente")