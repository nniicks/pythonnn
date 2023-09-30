'''Para determinar se uma cadeia de caracteres é formada apenas por dígitos numéricos, utilizamos o método isnumeric().
Projete e implemente um programa em python que leia uma cadeia de caracteres e, em seguida,
determine se a cadeia lida é formada apenas por dígitos numéricos sem utilizar a função isnumeric(str).

A entrada é dada por uma cadeia de caracteres.

A saída consiste em escrever VERDADEIRO se a palavra é formada apenas por dígitos numéricos e FALSO, caso contrário.

Use os exemplos abaixo como padrão.

Por exemplo:

Entrada	Resultado
teste
FALSO
13354
VERDADEIRO'''

'''aux = input()
flag = True

for i in range(len(aux)):
    if ord(aux[i]) < 48 or ord(aux[i]) > 57:
        flag = False
        break

if flag == True:
    print("VERDADEIRO")

else:
    print("FALSO")'''

aux = input()

try:
    aux = int(aux)
    print("VERDADEIRO")

except:
    print("FALSO")