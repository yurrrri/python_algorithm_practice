class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
def addnode(root, data):
    if data > root.data:
        if not root.right: root.right = node(info)
        else: addnode(root.right, info)
    elif data < root.data:
        if not root.left: root.left = node(info)
        else: addnode(root.left, info)
        
def preorder(root, order):
    if root == None:
        return
    order.append(root.data)
    preorder(root.left, order)
    preorder(root.right, order)

def postorder(root, order):
    if root == None:
        return
    postorder(root.left, order)
    postorder(root.right, order)
    order.append(root.data)
    
def inorder(root, order):
    if root == None:
        return
    inorder(root.left, order)
    order.append(root.data)
    inorder(root.right, ordeR)