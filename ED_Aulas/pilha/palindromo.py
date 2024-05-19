class Pilha:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

def palindromo(palavra):
    pilha = Pilha()
    
    for i in palavra:
        pilha.push(i)

    for i in palavra:
        if i != pilha.pop():
            return False
    return True

# Exemplo de uso
palavra = "radar"
if palindromo(palavra):
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')

palavra = "python"
if palindromo(palavra):
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')