## Selection Sort
## Analisa o array do menor numero para o maior
## Colocando os menores primeiro no array, contrário ao Bubble Sort
## Pode ocorrer problema de Shifting, então tomar cuidado
## Realizar Swap (troca) 
## Complexidade O({n^2}/2) = O(n^2)

selecao = [8,12,9,3,7]

tamanho = len(selecao)

for i in range(tamanho):
    indicie_valor_min = i                               ##Começa com o valor 0
    for j in range(i+1, tamanho):                       ## j começa a ler apartir do 2 valor e comparando com o indicio do valor minimo encontrado
        if selecao[j] < selecao[indicie_valor_min]:
            indicie_valor_min = j   
    selecao[i], selecao[indicie_valor_min] = selecao[indicie_valor_min], selecao[i]    ##SWAP
    
print("Sorted array:", selecao)