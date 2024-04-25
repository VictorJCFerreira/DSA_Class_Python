class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)                       #Cria um novo Nó
        if self.head is None:                       #Define o Inicio da Lista, nesse caso (1)
            self.head = new_node                    #Após o primeiro Nó, todos serão o ultimo Nó
            return
        last_node = self.head                       #Começa a Ler a partir do primeiro nó
        while last_node.next is not None:           # Percorre a lista até encontrar o último nó, cujo 'next' é None
            last_node = last_node.next  
        last_node.next = new_node                   # Definimos o 'next' desse ultimo nó como o novo nó

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    # Criando a lista encadeada
    lista = LinkedList()

    lista.append(8)
    lista.append(12)
    lista.append(25)
    lista.append(17)

    print("Lista encadeada:")
    lista.display()