### Crie duas Pilhas com diferentes implementações:
### Uma usando collecƟons.deque, e a outra usando Lista Encadeadas.
### discuta qual das duas implementações aparenta ser mais eficiente e por que ?

from collections import deque

class Pilha_Deque:
    def __init__(self):
        self.fila = deque()
    def push(self,dado):
        self.fila.appendleft(dado)
    def pop(self):
        self.fila.popleft()
    def display(self):
        print(self.fila)
        


class Node:
    def __init__(self,dado):
        self.dado = dado
        self.next = None
        self.prev = None

class Pilha:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def vazia(self):
        return self.head == None

    def push(self,dado):
        novo = Node(dado)
        #quando ta vazio
        if  self.vazia():
            self.head = novo
            self.tail = novo
        else:
            novo.prev = self.tail
            self.tail.next = novo
            self.tail = novo

    def pop(self):
        if not self.vazia():
            if self.head == self.tail:
                return_node = self.tail
                self.head = None
                self.tail = None
                return return_node.dado

            return_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return return_node.dado
        else:
            return False
    
    def display(self):
        aux = Pilha()
        
        while not self.vazia():
            item = self.pop()
            print(item, end=" ")
            aux.push(item)
        
        print()
        
        while not aux.vazia():
            self.push(aux.pop())
    
    
        
pilhaD = Pilha_Deque()

pilhaD.push(1)
pilhaD.push(2)
pilhaD.push(3)

pilhaD.display()

pilhaD.pop()

pilhaD.display()


print("-----------------")


pilhaLL = Pilha()

pilhaLL.push(5)
pilhaLL.push(6)
pilhaLL.push(7)

pilhaLL.display()

pilhaLL.pop()

pilhaLL.display()