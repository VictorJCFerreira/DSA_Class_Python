# Continuação da questão 5

#### implementar um código que mescle 2 listas encadeadas de pessoas, mantendo a ordem por idade
    #### Merge sort funcionaria, eu acho
    
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
        self.count = 0
        
    def vazia(self):
        return self.head == None

    def posicao_do_index(self):
        return self.count
    
    def tamanho(self):
        return (self.count + 1)
    
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
            novo.prev = self.tail
            self.tail.next = novo 
            self.head.prev = novo
            self.head = novo
            self.count += 1
        
        #Idade mais alta
        elif(self.tail.paciente.idade <= novo.paciente.idade):
            novo.next = self.head
            novo.prev = self.tail
            self.tail.next = novo
            self.tail = novo
            self.head.prev = self.tail
            self.count += 1
        
        # No Meio
        else:
            atual = self.head
            while (novo.paciente.idade > atual.paciente.idade):
                atual = atual.next
            if (atual == self.head):
                novo.next = self.head
                novo.prev = self.tail
                self.head.prev = novo
                self.tail.next = novo
                self.head = novo
                self.count += 1
            else:
                novo.next = atual
                novo.prev = atual.prev
                atual.prev.next = novo
                atual.prev = novo
                self.count += 1
    
    def adicionar_primeiro(self):
        if (not self.vazia()):
            
            primeiro = self.head
            
            if (self.head == self.tail):
                self.head = self.tail = None
                return primeiro
            
            else:
                self.head.next.prev = self.tail
                self.tail.next = self.head.next
                self.head = self.head.next
                return primeiro
            
        else:
            return False
                
    def display(self):
        atual = self.head
        print(atual.paciente.idade, ":",atual.paciente.nome)
        while atual.next is not self.head:
            atual = atual.next
            print(atual.paciente.idade, ":",atual.paciente.nome)
            


def mescla_ordenada(consultorio, clinica):
    
    hospital = consultorio
    
    while not clinica.vazia():
        hospital.entrada(clinica.adicionar_primeiro().paciente)
    return hospital




consultorio = DCLL()
consultorio.entrada(Paciente(22,"O"))
consultorio.entrada(Paciente(25,"S"))
consultorio.entrada(Paciente(30,"P"))
consultorio.entrada(Paciente(89,"L"))


clinica = DCLL()
clinica.entrada(Paciente(78,"A"))
clinica.entrada(Paciente(42,"I"))
clinica.entrada(Paciente(55,"T"))
clinica.entrada(Paciente(10,"H"))


hospital = mescla_ordenada(consultorio,clinica)

hospital.display()