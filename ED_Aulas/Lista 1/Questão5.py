#### Lista encadeada circular de pacientes, ordenada por idade em forma crescente 
#### O nó adicionado deverá manter a ordem e deve ser colocado no lugar certo por idade
    #### Binary Search para aumentar a eficiencia da busca para onde colocar o novo nó

class Paciente:
    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome


class Node:
    def __init__(self, paciente):
        self.paciente = paciente
        self.next = None
        self.prev = None

class CLL:
    def __init__(self, paciente):
        self.paciente = paciente
        self.head = None
        self.tail = None
    
    def adicionar(self, paciente):
        novo = Node(paciente)
            
        if(self.head == None):
            novo.next = novo
            novo.prev = novo
            self.head = novo
            self.tail = novo
        
        #Idade mais baixa
        elif(novo.paciente.idade <= self.head.paciente.idade):
            atual = self.head
            novo.next = atual
            novo.prev = atual.prev
            self.head = novo
            self.head.prev = self.tail
        
        #Idade mais alta
        elif(novo.paciente.idade >= self.tail.paciente.idade):
            atual = self.tail
            novo.next = atual.next
            novo.prev = atual
            self.tail = novo
            self.tail.next = self.head
        
        #meio
        else:
            atual = self.head
            while novo.paciente.idade > atual.paciente.idade:
                atual = atual.next
            if atual == self.head:
                novo.next = self.head
                novo.prev = self.tail
                self.head.prev = novo
                self.tail.next = novo
                self.head = novo
            #item no meio da lista:
            else:
                novo.next = atual
                novo.prev = atual.prev
                atual.prev.next = novo
                atual.prev = novo