##  Radix Sort 
##  Organiza digitos do algarismo menos significativo para o maior
## Organiza em ordem crescente
## Complexidade Max : O(n^2) ; Média : O(n log(n)) ; Melhor : O(n.k)

array = [170, 45, 75, 90, 802, 24, 2, 66]
print(array)
numero_maior = max(array)
expoente = 1

radixArray = [ [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ] ]

while (numero_maior // expoente > 0):
    while (len(array)>0):
        valor = array.pop()
        radixIndex = (val // expoente) % 10
        radixArray[radixIndex].append(val)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            array.append(val)

    expoente *= 10

print("Sorted array:", array)