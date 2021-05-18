class newNode:
    def __init__(self, value):
        self.data = value
        self.left = self.right = None
        
def get_element(root, key):
    if root is None:
        return False
        
    if root.data == key:
        return True
    
    lleft = get_element(root.left, key)
    rright = get_element(root.right, key)
    
    if lleft:
        return True
    
    if rright:
        return True

    return False

if __name__ == '__main__':
    root = newNode(2)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(6)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(11)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)
    print("data is:", get_element(root, 2))