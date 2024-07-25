class Node:
    def __init__(self, dado):
        self.dado = dado
        self.left = None
        self.right = None

    def is_folha(self):
        if self.right is None and self.left is None:
            return True
        else:
            return False

    def is_bambo(self):
        return self.left is None or self.right is None


class Arvore_binaria:
    def __init__(self, dado):
        self.raiz = Node(dado)
        self.altura = 1

    def adicionar(self, dado):
        current_node = self.raiz
        contador = 1
        while True:
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
            if dado < current_node.dado:
                current_node.left = new_node
            elif dado > current_node.dado:
                current_node.right = new_node
            contador += 1
            if self.altura < contador:
                self.altura = contador

    def adicionar_node(self, node):
        current_node = self.raiz
        while True:
            if node.dado > current_node.dado:
                if current_node.right is None:
                    break
                current_node = current_node.right
            elif node.dado < current_node.dado:
                if current_node.left is None:
                    break
                current_node = current_node.left
        if node.dado != current_node.dado:
            if node.dado < current_node.dado:
                current_node.left = node
            elif node.dado > current_node.dado:
                current_node.right = node
        self.altura = self.calcular_altura(self.raiz)

    def calcular_altura(self, node):
        if node is None:
            return 0
        else:
            altura_esquerda = self.calcular_altura(node.left)
            altura_direita = self.calcular_altura(node.right)
            return 1 + max(altura_esquerda, altura_direita)

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

        self.altura = self.calcular_altura(self.raiz)
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

    def remover(self, dado):
        if dado == self.raiz.dado:
            filho_esquerdo = self.raiz.left
            filho_direito = self.raiz.right
            self.raiz = filho_direito
            self.adicionar_node(filho_esquerdo)
        
        #procura onde o dado deve estar:
        current_node = self.raiz
        pai = None
        filho_esquerdo = None
        filho_direito = None
        processo = None #processo 0 = filho esquerdo, processo 1 = filho direito
        
        #procura o nó onde o dado deve estar:
        while True:
            if dado == current_node.dado:
                break
            if current_node.is_folha():
                print("a arvore não possui o dado informado!")
                return -1
            elif dado > current_node.dado:
                if current_node.right == None:
                    break
                pai = current_node
                filho_direito = current_node.right
                current_node = current_node.right
                processo = 1
            elif dado < current_node.dado:
                if dado < current_node.dado:
                    if current_node.left == None:
                        break
                pai = current_node
                filho_esquerdo = current_node.left
                current_node = current_node.left
                processo = 0

        #caso o nó seja folha:
        if current_node.is_folha():
            if processo == 0:
                pai.left = None
            if processo == 1:
                pai.right = None
        #caso o nó seja galho:
        else:
            esquerdo = current_node.left
            direito = current_node.right
            if processo == 0:
                pai.left = None
            elif processo == 1:
                pai.right = None
            if esquerdo is not None:
                self.adicionar_node(esquerdo)
            if direito is not None:
                self.adicionar_node(direito)


# Exemplo de uso:
arvore = Arvore_binaria(7)
arvore.adicionar(3)
arvore.adicionar(0)
arvore.adicionar(4)
arvore.adicionar(1)
arvore.adicionar(15)
arvore.adicionar(12)
arvore.adicionar(11)
arvore.adicionar(13)
arvore.adicionar(20)
arvore.adicionar(17)
arvore.adicionar(22)

arvore.display()
print("--------------------------------")
arvore.remover(15)
arvore.display()



