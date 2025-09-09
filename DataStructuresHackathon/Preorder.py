class Node:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None

class Binarytree:
    def __init__(self):
        self.root = None

    def insertintree(self,root,key):
        if root is None:
            return Node(key)
        
        elif key<root.key:
            root.left = self.insertintree(root.left,key)

        elif key>root.key:
            root.right = self.insertintree(root.right,key)
        
        return root

    def preorder(self,root):
        if root:
            print(root.key,end = " ")
            self.preorder(root.left)
            self.preorder(root.right)

bst = Binarytree()
lst = [1,7,3,8,4,9]
root = None
for i in lst:
    root = bst.insertintree(root,i)

print("Preorder :")
bst.preorder(root)

