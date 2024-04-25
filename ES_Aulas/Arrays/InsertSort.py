## Insertion Sort
## Ograniza um Array, de forma crescente
## Porém, analiza um array desordenado, e ordena em um novo array
## Complexidade O({n^2}/2) = O(n^2)

array = [64, 34, 25, 12, 22, 11, 90, 5]

tamanho = len(array)
for i in range(1,tamanho):                  # Pula o primeiro valor
    insert_index = i
    current_value = array[i]                # o valor atual analisado
    for j in range(i-1, -1, -1):            # Analisa o valor atual sobre os numeros do indicie j
        if array[j] > current_value:        # Se o numero do indicie j é > que o valor atual
            array[j+1]=array[j]             # O indicie j+1 recebe o numero do indicie j
            insert_index = j                # o novo insert-index vai ser o valor do indicie j
        else:
            break
    array[insert_index] = current_value     #substitui o valor atual no indicie j

print("Sorted array:", array)