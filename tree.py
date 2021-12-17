# Depth First Traversals: 
# (a) Inorder (Left, Root, Right) : 4 2 5 1 3 
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3 
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1
# Breadth-First or Level Order Traversal: 1 2 3 4 5 

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)
    
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)

def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)
 
print("\nPostorder traversal of binary tree is")
printPostorder(root)