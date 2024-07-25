class Node:
    def __init__(self, dado):
        self.dado = dado
        self.left = None
        self.right = None

    def is_folha(self):
        return self.left is None and self.right is None

    def is_bambo(self):
        return self.left is None or self.right is None

class Arvore_binaria:
    def __init__(self, dado):
        self.raiz = Node(dado)
        self.quantidade_nos = 1
        self.altura = 1

    def adicionar(self, dado):
        current_node = self.raiz
        contador = 1
        while True:
            if dado == current_node.dado:
                return 0

            if dado > current_node.dado:
                if current_node.right is None:
                    break
                current_node = current_node.right
                contador += 1
            elif dado < current_node.dado:
                if current_node.left is None:
                    break
                current_node = current_node.left
                contador += 1

        if dado != current_node.dado:
            new_node = Node(dado)
            self.quantidade_nos += 1
            if dado < current_node.dado:
                current_node.left = new_node
            elif dado > current_node.dado:
                current_node.right = new_node
            contador += 1
            if self.altura < contador:
                self.altura = contador

    def obter_nos_do_nivel(self, node, nivel):
        if nivel == 1:
            return [node] if node else [None]
        elif nivel > 1:
            left = self.obter_nos_do_nivel(node.left if node else None, nivel - 1)
            right = self.obter_nos_do_nivel(node.right if node else None, nivel - 1)
            return left + right

    def display(self):
        if self.raiz is None:
            return

        # Calcula a largura máxima necessária
        max_width = 2 ** (self.altura - 1) - 1
        linhas = []

        for i in range(1, self.altura + 1):
            linha = self.obter_nos_do_nivel(self.raiz, i)
            linhas.append(linha)

        for i, linha in enumerate(linhas):
            # Calcula o espaçamento para centralizar
            spaces = max_width // (2 ** i)
            output = []
            for node in linha:
                if node is None:
                    output.append(" " * (len(str(self.raiz.dado)) + spaces))
                else:
                    output.append(str(node.dado).center(len(str(self.raiz.dado)) + spaces))
            print("".join(output).center(max_width * 2))

    def contar_nos_binarios(self, node):
        if node is None:
            return 0
        else :
            return 1 + self.contar_nos_binarios(node.left) + self.contar_nos_binarios(node.right)
            
    def is_binaria(self):
        if self.quantidade_nos == self.contar_nos_binarios(self.raiz):
            return True
        else:
            return False


# Exemplo de uso:
arvore = Arvore_binaria(7)
arvore.adicionar(8)
arvore.adicionar(3)
arvore.adicionar(1)
arvore.adicionar(2)
arvore.adicionar(9)

arvore.display()
print(arvore.is_binaria())
