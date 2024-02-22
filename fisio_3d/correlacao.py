
#função que calcula a correlação entre dados que estão presentes em duas listas

def calcular_correlao(lista_1, lista_2):
    
    soma_x = 0.0
    soma_y = 0.0
    soma_quadrado_x = 0.0
    soma_quadrado_y = 0.0
    soma_x_y = 0.0

    #i é o numero de pares ordenados. as listas devem possuir o mesmo tamanho!!

    for i in range(len(lista_1)):
        soma_x += lista_1[i]
        soma_y += lista_2[i]
        soma_quadrado_x += lista_1[i] ** 2
        soma_quadrado_y += lista_2[i] ** 2
        soma_x_y += lista_1[i] * lista_2[i]

    #calculados os termos necessarios, agr é só aplicar esses numeros da expressao matematica que calcula a correlaçao

    n = len(lista_1)    
    aux_1 = ((n * soma_quadrado_x - soma_x**2)**0.5)
    aux_2 = ((n * soma_quadrado_y - soma_y**2 )**0.5)

    correlacao = ((n * soma_x_y) - soma_x * soma_y ) / (aux_1 * aux_2)

    return correlacao


dados_1 = [3, 2, -1, 4]
dados_2 = [7, 5, -1, 0]

resultado = calcular_correlao(dados_1, dados_2)
print(f"A correlação entre os dados é: {resultado}")
