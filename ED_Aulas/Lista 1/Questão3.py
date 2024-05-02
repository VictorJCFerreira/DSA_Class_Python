### Explicar a estratégia por trás da torre de hanoi



def torre_hanoi(n, origem, destino, auxiliar):
    # Caso base: Se houver apenas um disco na haste de origem
    if n == 1:
        # Movemos diretamente o disco da origem para o destino
        print("Mova disco 1 da haste", origem, "para haste", destino)
        return

    # Passo de recursão:
    # 1. Movemos uma pilha de n-1 discos da haste de origem para a haste auxiliar
    torre_hanoi(n-1, origem, auxiliar, destino)
    
    # 2. Movemos o último disco da haste de origem para a haste de destino
    print("Mova disco", n, "da haste", origem, "para haste", destino)
    
    # 3. Movemos a pilha de n-1 discos da haste auxiliar para a haste de destino
    torre_hanoi(n-1, auxiliar, destino, origem)

# Exemplo de uso
num_discos = 3
torre_hanoi(num_discos, 'A', 'C', 'B')