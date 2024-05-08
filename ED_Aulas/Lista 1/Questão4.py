#### Explicar papel da pilha de chamadas no contexto de funções recursivas

# Na questão de recursão, as pilhas fazem um papel importante pois após a cada chamada recursiva,
# uma nova instância da função é chamada, e elas continuam empilhando até chegar no caso base.
# O papel da pilha é manter a ordem de execução seja retomada corretamente após as chamadas recursivas.

# EXEMPLO COM A FUNÇÃO RECURIVA DE FATORIAL

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
numero=5 
fatorial(numero)
    
#PILHA DE CHAMADA
#fatorial(1) : Caso base e retorna
    #fatorial(2)
        #fatorial(3)
            #fatorial(4)
                #fatorial(5)
                

#### Como a manipulação da pilha afeta o desempenho e uso de memória em algorítimos recursivos ?

# Na questão do desempenho do algoritimo e do uso de memória, acaba que a recursão juntamente com as Call Stacks
# pode afetar o desempenho devido ao tamanho da pilha, e até gerar um estouro caso ela seja muito grande.
# O uso de memória para suportar uma Call Stack grande é considerável. Então, tomar cuidado com isso.
 