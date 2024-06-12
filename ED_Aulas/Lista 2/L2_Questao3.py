### Implemente uma fila circular utilizando um deque.
### A fila circular possui um tamanho máximo
### o próximo elemento a ser inserido substui o elemento mais antigo da fila.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDeque:
    def __init__(self, capacidade):
        self.head = None
        self.tail = None
        self.size = 0
        self.capacidade = capacidade

    def vazia(self):
        return self.size == 0

    def cheio(self):
        return self.size == self.capacidade

    def enqueue(self, data):
        novo = Node(data)
        if self.vazia():
            self.head = self.tail = novo
            novo.next = novo.prev = novo
        elif self.cheio():
            novo.next = self.head.next
            novo.prev = self.tail
            self.tail.next = novo
            self.head.next.prev = novo
            self.head = novo.next
            self.tail = novo
        else:
            novo.prev = self.tail
            novo.next = self.head
            self.tail.next = novo
            self.head.prev = novo
            self.tail = novo
        if not self.cheio():
            self.size += 1

    def dequeue(self):
        if self.vazia():
            raise IndexError("Fila Vazia")

        data = self.head.data
        if self.size == 1:
            self.head = self.tail = None
        else:
            new_head = self.head.next
            new_head.prev = self.tail
            self.tail.next = new_head
            self.head = new_head
        self.size -= 1
        return data

    def print_queue(self):
        if self.vazia():
            print("Fila Vazia")
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

capacidade = 5
circular_queue = CircularDeque(capacidade)

circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
circular_queue.enqueue(4)
circular_queue.enqueue(5)

circular_queue.print_queue()  

circular_queue.enqueue(6)
circular_queue.enqueue(7)

circular_queue.print_queue() 

circular_queue.dequeue()
circular_queue.dequeue()

circular_queue.print_queue() 
