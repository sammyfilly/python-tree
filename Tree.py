from collections import deque

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
        elif data > node.data:
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
            print(root.data)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
            

    def postorder_traversal(self, root):
        if root is not None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data)

    def breadth_first_traversal(self, root):
        q = deque([])
        q.append(root)
        while len(q) != 0:
            node = q.popleft()
            print(node.data)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    def tree_height(self, root):
        if root is None:
            return 0
        l_height = tree_height(root.left)
        r_height = tree_height(root.right)
        return (l_height+1) if l_height > r_height else (r_height+1)

#    def pretty_print(self, root, depth):
#        if root is not None:
            

