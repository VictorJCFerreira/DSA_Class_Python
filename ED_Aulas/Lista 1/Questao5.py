#### Lista encadeada circular de pessoas, ordenada por idade em forma crescente 
#### O nó adicionado deverá manter a ordem e deve ser colocado no lugar certo por idade
    #### Binary Search para aumentar a eficiencia da busca para onde colocar o novo nó

class Paciente:
    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome

class No:
    def __init__(self, paciente):
        self.paciente = paciente
        self.next = None
        self.prev = None

class DCLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def vazia(self):
        return self.head == None
    
    def entrada(self, paciente):
        
        novo = No(paciente)
            
        if (self.vazia()):
            novo.next = novo
            novo.prev = novo
            self.head = novo
            self.tail = novo
        
        #Idade mais baixa
        elif(self.head.paciente.idade >= novo.paciente.idade):
            novo.next = self.head
            novo.prev = self.head.prev
            self.head.prev.next = novo 
            self.head.prev = novo
            self.head = novo
        
        #Idade mais alta
        elif(self.tail.paciente.idade <= novo.paciente.idade):
            novo.next = self.head
            novo.prev = self.tail
            self.tail.next = novo
            self.tail = novo
            self.head.prev = self.tail
        
        # No Meio
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
            else:
                novo.next = atual
                novo.prev = atual.prev
                atual.prev.next = novo
                atual.prev = novo
                
    def print(self):
        atual = self.head
        print(atual.paciente.idade, ":",atual.paciente.nome)
        while atual.next is not self.head:
            atual = atual.next
            print(atual.paciente.idade, ":",atual.paciente.nome)
            
    
hospital = DCLL()

hospital.entrada(Paciente(22,"L"))
hospital.entrada(Paciente(25,"M"))
hospital.entrada(Paciente(30,"N"))
hospital.entrada(Paciente(89,"O"))
hospital.entrada(Paciente(12,"P"))
hospital.entrada(Paciente(22,"Q"))

hospital.print()