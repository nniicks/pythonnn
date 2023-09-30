'''Lucas é um alpinista experiente e está planejando uma expedição a uma cordilheira desconhecida.
Antes de embarcar nessa aventura, ele está usando um sistema de informações geográficas computadorizado para analisar o perfil das montanhas que
encontrará pelo caminho.

O sistema de informações geográficas representa o perfil de cada montanha como uma sequência de números inteiros, onde cada número representa a altitude em
determinada posição. Lucas percebeu que, para determinar a complexidade das trilhas e a quantidade de picos que encontrará, é importante analisar essa sequência.

Ele observou que, nessa região específica, se existirem três altitudes consecutivas na sequência em que a altura do meio é menor do que as alturas adjacentes,
isso indica a presença de mais de um pico na montanha. Caso contrário, se não houver nenhuma sequência desse tipo, significa que a montanha possui apenas um pico.

Lucas precisa dessa informação para planejar corretamente a expedição. Ele pede a sua ajuda para desenvolver um programa que,
dado o perfil da montanha, determine se ela possui mais de um pico ou apenas um pico.

A entrada consistirá em duas linhas. A primeira linha contém um número inteiro N, representando o tamanho da sequência de altitudes.
A segunda linha contém N inteiros Ai, onde 1 ≤ i ≤ N, representando as altitudes ao longo da montanha.

Seu programa deve imprimir uma linha contendo o caractere "Altos e baixos" se a montanha possuir mais de um pico, ou o caractere "Sobe e desce" se a
montanha tiver apenas um pico.

Por exemplo:

Entrada	Resultado
9
1 2 3 4 6 7 6 5 4
Sobe e desce
8
1 2 1 3 4 2 1 5
Altos e baixos'''

n = int(input())
a = [int(i) for i in input().split()]
#a = list(map(int, input().split()))
flag = False


for i in range(1, len(a)-1):
    if a[i] < a[i-1] and a[i] < a[i+1]:
        print("Altos e baixos")
        flag = True
        break

    
if flag == False:
    print("Sobe e desce")