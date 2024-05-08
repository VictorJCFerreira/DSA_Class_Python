### Explicar a estratégia por trás da torre de hanoi

# n = numero de discos a serem movidos
def torre_hanoi(n, origem, destino, auxiliar):
    
    if (n == 1):                                                        # Caso base: Um disco na haste de origem
        print("Mova disco 1 da haste", origem, "para haste", destino)   # Movemos diretamente o disco da origem para o destino 
        return

    
    torre_hanoi(n-1, origem, auxiliar, destino)                         # 1. Movemos uma pilha de n-1 discos da haste de origem para a haste auxiliar
    
    print("Mova disco", n, "da haste", origem, "para haste", destino)   # 2. Movemos o último disco da haste de origem para a haste de destino
    
    
    torre_hanoi(n-1, auxiliar, destino, origem)                         # 3. Movemos a pilha de n-1 discos da haste auxiliar para a haste de destino

num_discos = 3
torre_hanoi(num_discos, 'A', 'C', 'B')