class newNode:
    def __init__(self, value):
        self.data = value
        self.left = self.right = None
        
def search(root, key):
    if root is None:
        return False
        
    if root.data == key:
        return True
    
    lleft = search(root.left, key)
    rright = search(root.right, key)
    
    if lleft:
        return True
    
    if rright:
        return True
    
    return False

if __name__ == '__main__':
    root = newNode(50)
    root.left = newNode(20)
    root.right = newNode(70)
    root.left.right = newNode(30)
    root.left.right.left = newNode(25)
    root.left.right.right = newNode(35)
    root.right.right = newNode(80)
    root.right.right.left = newNode(75)
    print(search(root, 75))