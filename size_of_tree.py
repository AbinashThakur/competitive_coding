class newNode:
    def __init__(self, value):
        self.data = value
        self.left = self.right = None
        
def get_size(root):
    if root is None:
        return 0
    
    return get_size(root.left) + 1 + get_size(root.right)

if __name__ == '__main__':
    root = newNode(2)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(6)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(11)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)
    print("data is:", get_size(root))