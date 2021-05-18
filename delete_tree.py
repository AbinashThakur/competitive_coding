class newNode:
    def __init__(self, value):
        self.data = value
        self.left = self.right = None
        
def delete_tree(root):
    if root is None:
        return
    
    delete_tree(root.left)
    delete_tree(root.right)
    
    print(" Deleting node:", root.data)

if __name__ == '__main__':
    root = newNode(2)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(6)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(11)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)
    delete_tree(root)
    root = None
    
    print("tree is deleted")