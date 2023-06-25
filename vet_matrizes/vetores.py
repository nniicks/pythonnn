#insertion sort
def insertion(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i -1

        while j>= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j -= 1
            lista[j+1] = chave
    return lista

#selection sort
def selection(lista):
    for i in range(len(lista)-1):
        min_Index = i

        for j in range(i, len(lista)):
            if lista[j] < lista[min_Index]:
                min_Index = j
        
        if lista[i] > lista[min_Index]:
            aux = lista[i]
            lista[i] = lista[min_Index]
            lista[min_Index] = lista[i]      
    
    return lista

#bubble sort
def bubble(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista

#algoritmo simples de busca
def search(lista, valor):
    for i in range(len(lista)):
        if valor == lista[i]:
            return i
    return None

#busca binaria
def binary_search(lista, valor, begin=0, end=None):
    if end == None:
        end = len(lista)-1
    
    if begin <= end:
        medio = (begin + end)//2

        if valor == lista[medio]:
            return medio
        if valor < lista[medio]:
            return binary_search(lista, valor, begin, medio-1)
        else:
            return binary_search(lista, valor, medio+1, end)
    return None

#inverter um vetor
def reverse_list(lista):
    vet_inv = []
    for i in range(-1,len(lista)-1,-1):
        vet_inv.append(lista[i])
    return vet_inv

#copia uma lista
def copy_list(lista):
    copia = []
    for i in range(len(lista)):
        copia.append(lista[i])
    return copia