class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("Lista vazia")
            return
        current = self.head
        print("Elementos da lista:")
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()


# Exemplo de uso da lista encadeada circular
if __name__ == "__main__":
    lista = CircularLinkedList()
    lista.append(1)
    lista.append(2)
    lista.append(3)
    lista.append(4)

    lista.display()