# Реализация Стека через списки

class Stack:
    def __init__(self):
        self.items = []

    def if_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


stack = Stack()

print(stack.if_empty())

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.if_empty())
print(stack.peek())


# Реализация Очереди через списки

class Queue:
    def __init__(self):
        self.items = []

    def if_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


queue = Queue()

print(queue.if_empty())

queue.enqueue("Элемент 1")
queue.enqueue("Элемент 2")
queue.enqueue("Элемент 3")
queue.enqueue("Элемент 4")
queue.enqueue("Элемент 5")

print(queue.if_empty())
print(queue.size())
print(queue.dequeue())  # Метод pop возвращает то, что он удалил
print(queue.size())



# Так делается Дерево:

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)

    return root

# Функция для печати дерева
def print_tree(node, level=0):
    if node != None:
        print_tree(node.right, level + 1)
        print('  ' * 4 * level + f'-> {node.value}')
        print_tree(node.left, level + 1)


root = Node(70)

root = insert(root, 30)
root = insert(root, 56)
root = insert(root, 89)
root = insert(root, 45)
root = insert(root, 60)
root = insert(root, 73)
root = insert(root, 98)
root = insert(root, 84)

# Вывод дерева
print("Визуализация дерева:")
print_tree(root)



# Так делается Граф:

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        # {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]}
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()