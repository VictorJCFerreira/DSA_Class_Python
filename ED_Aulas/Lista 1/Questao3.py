### Explicar a estratégia por trás da torre de hanoi

def torre_hanoi(n, origem, destino, auxiliar):
    
    if (n == 1):                                                        
        print("Disco 1 da haste", origem, "vai para para", destino)    
        return

    
    torre_hanoi(n-1, origem, auxiliar, destino)                         
    
    print("Disco", n, "da haste", origem, "vai para para", destino)   
    
    torre_hanoi(n-1, auxiliar, destino, origem)                         

discos = 3
torre_hanoi(discos, 'A', 'C', 'B')