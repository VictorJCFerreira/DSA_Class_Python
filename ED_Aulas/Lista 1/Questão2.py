# Comparar a eficiência da serie de Collatz por iteração x recursão
# Série de Collatz = todo numero positivo regride ao numero 1

# Comparar a eficiência dos 2 métodos. (Para a série de collatz o tempo foi praticamente identico)

##### Como a recursão afeta a complexidade do algoritmo ?

#### Se fosse a recursividade em Fibonacci averia algum impacto ? Sim, um impacto consideravel


import time

n = 77031

def collatz_ite(n):
    #print(n, end=" ")
    
    while n != 1:                       # Se o número atingiu 1, encerra a recursão
        
        if n % 2 == 0:                  # Par, chama a função recursiva e retorna n/2
            n = n // 2
        else:                           # Ímpar, chama a função recursiva com 3*n + 1
            n = 3 * n + 1
        #print(n, end=" ")

start_time = time.time()
collatz_ite = collatz_ite(n)
end_time = time.time()
iterative_time = end_time - start_time
print(iterative_time)


print("\n")

def collatz_rec(n):
    #print(n, end=" ")
    
    if n == 1:                          # Se o número atingiu 1, encerra a recursão
        return
    
    elif n % 2 == 0:                    # Se o número for par, chama a função recursiva com n/2
        collatz_rec(n // 2)
    
    else:                               # Se o número for ímpar, chama a função recursiva com 3*n + 1
        collatz_rec(3 * n + 1)
        
start_time = time.time()
collatz_rec = collatz_rec(n)
end_time = time.time()
recursive_time = end_time - start_time
print(recursive_time)