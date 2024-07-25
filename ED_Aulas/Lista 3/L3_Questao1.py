
def Quick_sort(lista , inicial=0, final=None):
    
    if final is None:
        final = len(lista) - 1
    
    pivot = lista[0]
    pesquerda = inicial
    pdireita = final
    
    if inicial < final:
        p = partir(lista, inicial, final)
        Quick_sort(lista, inicial, p-1)
        Quick_sort(lista, p+1, final)

def partir(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    
    for j in range(inicio, fim):
        if lista[j] <= pivot : 
            lista[j], lista[i] = lista[i], lista[j]    
            i = i+1

    lista[i], lista[fim] = lista[fim], lista[i]
    return i



j = [4,7,2,6,9,0,8,5]

print(j)

Quick_sort(j)

print(j)