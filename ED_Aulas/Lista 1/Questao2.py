# Comparar a eficiência da serie de Collatz por iteração x recursão

# Série de Collatz = todo numero positivo regride ao numero 1

# Comparar a eficiência dos 2 métodos. (Para a série de collatz o tempo foi praticamente identico)

import time

n = 77031

def collatz_ite(n):
    print(n, end=" ")
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n, end=" ")

start_time = time.time()
collatz_ite = collatz_ite(n)
end_time = time.time()
iterative_time = end_time - start_time
print("\n",iterative_time)



print("\n")

def collatz_rec(n):
    print(n, end=" ")
    
    if n == 1:
        return
    
    elif n % 2 == 0:
        collatz_rec(n // 2)
    
    else:
        collatz_rec(3 * n + 1)
        
start_time = time.time()
collatz_rec = collatz_rec(n)
end_time = time.time()
recursive_time = end_time - start_time
print("\n",recursive_time)





## A recursão da série de collatz é uma função de complexidade n.log(n)
## Se comparado a recursão de fibonacci, que é uma complexidade de (n)^2
## A diferença é notavel, pois após um certo numero de operações em collatz, a série tende a se estabilizar
## Já em fibonacci, ela so cresce cada vez mais, podendo gerear um estouro de pilha