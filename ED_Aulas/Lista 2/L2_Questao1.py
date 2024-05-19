### Implemente uma estrutura de Dados tipo Deque usando Listas Encadeadas.
### Comente sobre o tipo de Lista Encadeada escolhida para implementação.

class No:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:                                    # Feito a Base de uma Lista Duplamente Encadeada (DLL)
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_frente(self, data):                  # adicionar início do deque
        novo = No(data)
        if self.vazio():
            self.head = self.tail = novo
        else:
            novo.next = self.head
            self.head.prev = novo
            self.head = novo

    def add_final(self, data):                   # adicionar final do deque
        novo = No(data)
        if self.vazio():
            self.head = self.tail = novo
        else:
            novo.prev = self.tail
            self.tail.next = novo
            self.tail = novo

    def remover_frente(self):                     # retirar da frente do deque
        if self.vazio():
            raise IndexError("Deque Vazio")
        temp = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return temp.data

    def remover_final(self):                      # remover do final do deque
        if self.vazio():
            raise IndexError("Deque Vazio")
        temp = self.tail
        if self.head == self.tail:
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