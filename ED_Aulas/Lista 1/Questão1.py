# Fila de prioridade

# Cada elemento é associado a uma prioridade.
# Quanto mais alta a prioridade, mais rapido é retirado o elemento da fila.
# Normalmente usa-se HEAP para fazer uma fila de prioridade
# Cada nó tem uma prioridade
# No HEAP cada nó de prioridade é maior ou igual ao seus filhos 

# São amplamente utilizados em algoritmos de busca, algoritmos de caminho mais curto.
# Utilizações práticas : 
# Filas de Hospitais; Pacientes mais graves possuem maior prioridade.
# Trafego de redes; Os pacotes podem ter niveis de prioridades diferentes.
# Processos de um SO.

class PriorityQueue:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
        self.prev = None
    
    def isEmpty():                  # Verificaria se a Fila de prioridade está vazia
        return
    
    def insert(data, priority):     # Adicionaria um elemento e atribuiria uma prioridade a ele
        return
    
    def peak():                     # Mostraria o primeiro elemento da Fila, no caso, o com maior prioridade
        return
    
    def remove():                   # Retiraria o elemento de maior prioridade
        return
    
    def display():                  # Mostraria a Fila com os elementos e suas respectivas prioridades
        return
    