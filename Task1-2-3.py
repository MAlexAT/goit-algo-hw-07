class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(value, node.right)

    # Завдання 1: Знаходження найбільшого значення
    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.value

    # Завдання 2: Знаходження найменшого значення
    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.value

    # Завдання 3: Знаходження суми всіх значень
    def sum_values(self):
        return self._sum_values(self.root)

    def _sum_values(self, node):
        if node is None:
            return 0
        return node.value + self._sum_values(node.left) + self._sum_values(node.right)

# Приклад використання
bst = BinarySearchTree()
values = [10, 5, 15, 2, 7, 12, 20]

for value in values:
    bst.insert(value)

# Виконання завдань
print("Найбільше значення в дереві:", bst.find_max())  # Очікується: 20
print("Найменше значення в дереві:", bst.find_min())  # Очікується: 2
print("Сума всіх значень у дереві:", bst.sum_values())  # Очікується: 71


''' ** Пояснення функцій **

find_max: для пошуку найбільшого значення обходимо дерево до крайнього правого вузла, 
оскільки в BST найбільше значення завжди знаходиться праворуч.

find_min: для пошуку найменшого значення обходимо дерево до крайнього лівого вузла, 
оскільки найменше значення завжди знаходиться ліворуч.

sum_values: ця функція використовує рекурсію для підсумовування значень усіх вузлів у дереві, 
включаючи ліве і праве піддерева для кожного вузла.

Ці функції реалізують усі три завдання для роботи з BST. 
Можна адаптувати їх для AVL-дерева, якщо це необхідно, 
оскільки логіка для знаходження найбільшого, найменшого та суми значень залишається однаковою. '''