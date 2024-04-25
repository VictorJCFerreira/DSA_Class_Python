## Counting Sort
## Complexidade Max : O(n^2) ; Média : O(n+k) ; Melhor : O(n)

def countingSort(array):
    valor_maximo = max(array)           ## Reconhece o valor máximo do array
    count = [0] * (valor_maximo + 1)    ## Criar um array que irá reservar a contagem de 0 ao valor máximo do array

    while len(array) > 0:
        num = array.pop(0)              ## Retira o numero de indicie 0 do array 
        count[num] += 1                 ## Aciona a contagem no array contador 
    

    for i in range(len(count)):         ## Laço de repetição for de i até o tamanho de count
        while count[i] > 0:             ## Enquanto o index do contador nao for 0
            array.append(i)             ## Adiciona o numero i ao array normal
            count[i] -= 1               ## e Subtrai 1 no numero do indice do contador

    return array

unsortedarray = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3,0,1,1,7,0]
sortedarray = countingSort(unsortedarray)
print("Sorted arrayay:", sortedarray)