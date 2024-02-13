import math

# Função que calcula o comprimento de um vetor
def modulo_vetor(x, y, z):
    
    v = (x**2 + y**2 + z**2)**0.5
    
    return v
 
'''Função que retorna um vetor normalizado, ou seja, um vetor na mesma direção mas com norma igual a 1'''
def normaliza_vetor(x, y, z):
    
    aux = modulo_vetor(x, y, z)
    
    v = [x/aux, y/aux, z/aux]
    
    return v

'''Função que recebe como parâmetro as coordenadas de dois pontos, que são os extremos das duas retas, ou seja, 
esses dois pontos definem essa reta. Ela retorna a direção da reta no espaço'''
def calcula_inclinacao(x1, y1, z1, x2, y2, z2):
    
    vetor_diretor = [(x2 - x1), (y2 - y1), (z2 - z1)]
    
    return normaliza_vetor(*vetor_diretor)
    
'''Função que recebe as coordenadas de 4 pontos, sendo 2 de uma reta e 2 da outra, 
e devolve o angulo de flexão entre as duas'''
def angulo_de_flexao(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    
    inclinacao_reta1 = calcula_inclinacao(x1, y1, z1, x2, y2, z2)
    inclinacao_reta2 = calcula_inclinacao(x3, y3, z3, x4, y4, z4)
    
    produto_escalar = 0.0
    
    for v1, v2 in zip(inclinacao_reta1, inclinacao_reta2):
        produto_escalar += v1 * v2
    
    # Printando apenas para fins de testes   
    print(f'Produto escalar {produto_escalar}')
    angulo = math.acos(produto_escalar)

    return math.degrees(angulo)   

# Teste
x1, y1, z1 = 1, 2, 3
x2, y2, z2 = -1, -2, -3
x3, y3, z3 = 0, 0, 0
x4, y4, z4 = 2, 4, 6

aux = angulo_de_flexao(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4)
print(f'O ângulo de flexão entre as retas é: {aux} graus')