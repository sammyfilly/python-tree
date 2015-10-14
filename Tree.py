class Node:
    """
    Node for binary tree.
    """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
    def __repr__(self):
        return str(self.data)

class Tree:
    """
    Constructs tree. Provides utility functions.
    """
    def create_node(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.create_node(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.daat:
            node.right = self.insert(node.right, data)
        return node

    def search(self, node, data):
        if node is None or node.data == data:
            return node
        if node.data < data:
            return self.search(node.right, data)
        if node.data > data:
            return self.search(node.left, data)

    def inorder_traversal(self, root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)
    
    def preorder_traversal(self, root):
        if root is not None:
            print(self)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
            

    def postorder_traversal(self, root):
        if root is not None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(self)

    def breadth_first_traversal(self, root):
        q = Queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            print(node.data)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
