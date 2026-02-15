# ============================================
# 1. STACK (LIFO - Last In First Out)
# ============================================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(item, "pushed to stack")

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


# ============================================
# 2. QUEUE (FIFO - First In First Out)
# ============================================

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(item, "added to queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


# ============================================
# 3. LINKED LIST
# ============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ============================================
# 4. TREE (Binary Tree)
# ============================================

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)


# ============================================
# 5. GRAPH (Adjacency List)
# ============================================

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def display(self):
        for node in self.graph:
            print(node, "->", self.graph[node])


# ============================================
# TESTING ALL DATA STRUCTURES
# ============================================

if __name__ == "__main__":

    print("\n--- STACK ---")
    s = Stack()
    s.push(10)
    s.push(20)
    print("Popped:", s.pop())

    print("\n--- QUEUE ---")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("Dequeued:", q.dequeue())

    print("\n--- LINKED LIST ---")
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    ll.display()

    print("\n--- BINARY TREE ---")
    tree = BinaryTree(10)
    tree.root.left = TreeNode(5)
    tree.root.right = TreeNode(20)
    print("Inorder traversal:")
    tree.inorder(tree.root)

    print("\n\n--- GRAPH ---")
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.display()