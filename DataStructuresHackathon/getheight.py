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

    def height(self,root):
        if not root:
            return -1
        return max(self.height(root.left),self.height(root.right)) + 1

bst = Binarytree()
lst = [1,7,3,8,4,9]
root = None
for i in lst:
    root = bst.insertintree(root,i)

print(bst.height(root))