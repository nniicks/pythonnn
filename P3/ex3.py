'''Alice é uma jovem estudante de linguística e está bastante interessada nas propriedades das palavras e nos sons das letras.
Recentemente, ela começou a se envolver em um projeto de pesquisa sobre a frequência das vogais em palavras do idioma português.

Como parte desse projeto, Alice decidiu desenvolver um programa em Python que permita analisar a quantidade de cada vogal presente em uma palavra.
Ela acredita que compreender a distribuição das vogais pode revelar informações interessantes sobre a estrutura das palavras.

O programa desenvolvido por Alice lê uma palavra digitada pelo usuário e, em seguida, determina a quantidade de ocorrências de cada vogal (a, e, i, o, u)
nessa palavra. Alice assume que a palavra digitada estará escrita apenas em letras minúsculas e que palavras acentuadas não serão informadas.

Com base nessas informações, Alice espera obter resultados significativos para suas análises linguísticas.
Ela está animada para ver os resultados de diferentes palavras e observar como as vogais são distribuídas em cada uma delas.

Agora, sua tarefa é ajudar Alice a desenvolver esse programa em Python. Ele deve ler uma palavra digitada pelo usuário,
determinar a quantidade de ocorrências de cada vogal na palavra e imprimir esses valores na tela, seguindo o formato apresentado no exemplo abaixo.

Por exemplo:

Entrada	Resultado
ana
Quantidade de 'a' = 2
Quantidade de 'e' = 0
Quantidade de 'i' = 0
Quantidade de 'o' = 0
Quantidade de 'u' = 0
universidade
Quantidade de 'a' = 1
Quantidade de 'e' = 2
Quantidade de 'i' = 2
Quantidade de 'o' = 0
Quantidade de 'u' = 1'''

def vogal(palavra):
    vogais = ["a", "e", "i", "o", "u"]
    freq = [0]*5

    for i in range(len(palavra)):
        for j in range(len(vogais)):
            if palavra[i] == vogais[j]:
                freq[j] += 1


    for k in range(len(freq)):
        print(f"A vogal '{vogais[k]}' aparece {freq[k]} vezes na(o) palavra/texto '{palavra}'.")

aux = input()
vogal(aux)