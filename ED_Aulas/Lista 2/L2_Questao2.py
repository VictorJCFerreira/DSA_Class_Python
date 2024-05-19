### Ajuste o código anterior para criar uma função remover_duplicatas(fila)

class No:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_frente(self, data):
        novo = No(data)
        if (self.vazio()):
            self.head = self.tail = novo
        else:
            novo.next = self.head
            self.head.prev = novo
            self.head = novo

    def add_final(self, data):
        novo = No(data)
        if (self.vazio()):
            self.head = self.tail = novo
        else:
            novo.prev = self.tail
            self.tail.next = novo
            self.tail = novo

    def remover_frente(self):
        if (self.vazio()):
            raise IndexError("Deque Vazio")
        temp = self.head
        if (self.head == self.tail):
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return temp.data

    def remover_final(self):
        if (self.vazio()):
            raise IndexError("Deque Vazio")
        temp = self.tail
        if (self.head == self.tail):
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return temp.data
    
    def vazio(self):
        return self.head is None
    
    def tamanho(self):
        count = 0
        atual = self.head
        while atual:
            count += 1
            atual = atual.next
        return count

    def display(self):
        atual = self.head
        while atual:
            print(atual.data, end=" ")
            atual = atual.next
        print()

def remove_duplicatas(deque):
    if deque.vazio():
        return

    atual = deque.head
    visto = set()
    sem_Duplicatas = Deque()

    while atual:
        if atual.data not in visto:
            sem_Duplicatas.add_final(atual.data)
            visto.add(atual.data)
        atual = atual.next

    deque.head = sem_Duplicatas.head
    deque.tail = sem_Duplicatas.tail
    
deque = Deque()
deque.add_final(1)
deque.add_final(2)
deque.add_frente(2)
deque.add_final(3)
deque.add_frente(1)
deque.add_final(4)

deque.display()  # Saída esperada: 1 2 2 3 1 4 

remove_duplicatas(deque)

deque.display() 

