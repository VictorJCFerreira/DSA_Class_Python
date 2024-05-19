### Escreva uma função em Python que recebe uma pilha como entrada e inverte a
### ordem dos elementos utilizando apenas uma pilha adicional.

class Pilha:
    def __init__(self):
        self.pilha = []

    def vazia(self):
        return len(self.pilha) == 0

    def push(self, item):
        self.pilha.append(item)

    def pop(self):
        if self.vazia():
            raise IndexError("Pilha Vazia")
        return self.pilha.pop()

    def top(self):
        if self.vazia():
            raise IndexError("Pilha Vazia")
        return self.pilha[-1]

    def size(self):
        return len(self.pilha)

    def display(self):
        aux = Pilha()
        
        while not self.vazia():
            item = self.pop()
            print(item, end=" ")
            aux.push(item)
        
        print()
        
        while not aux.vazia():
            self.push(aux.pop())
            
def inverter(pilha):
    if not pilha.vazia():
        inversa = Pilha()
        while not pilha.vazia():
            inversa.push(pilha.pop())
        return inversa

# Exemplo de uso
pilha = Pilha()
pilha.push(7)
pilha.push(12)
pilha.push(234)
pilha.push(46)

pilha.display() 

pilha = inverter(pilha)

pilha.display()





