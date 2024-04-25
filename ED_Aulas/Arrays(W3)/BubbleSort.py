## Bubble Sort
## O array é re-arranjado de forma crescente
## Organiza analisando o maior numero e colocando no ultimo indicie
## O indicie 0 sendo o menor e o indicie n o maior
## Compara numero a numero dentro do array
## Complexidade O(n^2) 

bolha = [11,4,7,9,15,14,2]

tamanho = len(bolha) ## tamanho = 6

for i in range(tamanho - 1):                                ## i está servindo como INDICIE do array (0 até 5{tamanho - 1})
    for j in range(tamanho-i-1):                            ## j servirá para analisar os numeros dentro do array, e assim que a ultima posição do array for ocupada, o laço se repete para o proximo numero 
        if bolha[j] > bolha[j+1]:                           ## j verifica se o proximo numero é maior que o atual
            bolha[j], bolha[j+1] = bolha[j+1], bolha[j]     ## caso seja, troca eles de psocição

print("Array:", bolha)


## Se o algoritimo percorrer o array sem fazer uma troca, ele acaba
my_array = [12,7,4,15,22,78,19,3,7]

n = len(my_array)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break

print("Sorted array:", my_array)