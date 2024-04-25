## Quick Sort
## Escolhe um valor como pivot
## Elementos menores que o pivot vao para esquerda e maiores para a direita
## Usa recursão
## Complexidade : Pior caso O(n^2) e  Média : O(n log(n))

def partir(array, menor, maior):
    pivot = array[maior]                                    ## Define o numero pivot
    i = menor - 1                                           ## Index para onde o pivot deve ir

    for j in range(menor, maior):                           ## Iterar o Array do menor index recebido ao maior
        if array[j] <= pivot:                               ## Se o numero do array n index J for menor ou igual ao pivot
            i += 1                                          ## Se adiciona 1 no index
            array[i], array[j] = array[j], array[i]         ## E faz o SWAP (Caso e i e j sejam diferentes)

    array[i+1], array[maior] = array[maior], array[i+1]     ##Inverte o index do pivot com o maior numero
    return i+1                                              ## Retorna o index de onde partir o array

def quicksort(array, menor=0, maior=None):
    if maior is None:
        maior = len(array) - 1                      # Indicie do array

    if menor < maior:
        pivot_index = partir(array, menor, maior)
        quicksort(array, menor, pivot_index-1)      ## Recursao do pivot para Esquerda (maior - 1)
        quicksort(array, pivot_index+1, maior)      ## Recursao do pivot para Direita (menor + 1)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]          # 8 Numeros

quicksort(my_array)
print("Sorted array:", my_array)