class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def rotate_right(self, node):
        if node is None or node.left is None:
            return node

        # Realiza a primeira rotação simples à direita entre B e C
        node.left = self._rotate_right(node.left)

        # Realiza a segunda rotação simples à direita entre A e B
        return self._rotate_left(node)

    def _rotate_left(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def _rotate_right(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def inorder_traversal(self):
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.key, end=' ')
            self._inorder_recursive(node.right)

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, depth):
        if node is not None:
            self._print_tree_recursive(node.right, depth + 1)
            print("   " * depth + "->", node.key)
            self._print_tree_recursive(node.left, depth + 1)

# Exemplo de uso:
if __name__ == "__main__":
    bst = BinarySearchTree()
    keys = [30, 20, 40, 10, 25, 35, 50, 5, 15]

    for key in keys:
        bst.insert(key)

    print("Árvore original:")
    bst.print_tree()

    # Realiza a rotação dupla à direita no nó com chave 30
    bst.root = bst.rotate_right(bst.root)

    print("\nÁrvore após a rotação dupla à direita:")
    bst.print_tree()

    print("\nInorder traversal da árvore após a rotação:")
    bst.inorder_traversal()
