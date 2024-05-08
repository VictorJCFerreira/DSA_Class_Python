# Fila de prioridade

# Cada elemento é associado a uma prioridade.
# Quanto mais alta a prioridade, mais rapido é retirado o elemento da fila.
# Normalmente usa-se HEAP para fazer uma fila de prioridade
# No HEAP cada nó de prioridade é maior ou igual ao seus filhos 

class PriorityQueue:
    def __init__(self, informacao, prioridade):
        self.informacao = informacao
        self.prioridade = prioridade
        self.head = None
        self.tail = None
    
    def vazia():                  # Verificaria se a Fila de prioridade está vazia
        return
    
    def inserir(informacao, prioridade):     # Adicionaria um elemento e atribuiria uma prioridade a ele
        return
    
    def topo():                     # Mostraria o primeiro elemento da Fila, no caso, o com maior prioridade
        return
    
    def remover():                   # Retiraria o elemento de maior prioridade
        return
    
    def display():                  # Mostraria a Fila com os elementos e suas respectivas prioridades
        return
    

# São amplamente utilizados em algoritmos de busca, algoritmos de caminho mais curto.
# Utilizações práticas : 
# Filas de Hospitais; Pacientes mais graves possuem maior prioridade.
# Trafego de redes; Os pacotes podem ter niveis de prioridades diferentes.
# Processos de um SO.