class newNode:
    def __init__(self, value):
        self.data = value
        self.left = self.right = None
        
def get_max(root):
    if root is None:
        return float('-inf')
    
    res = root.data
    lleft = get_max(root.left)
    rright = get_max(root.right)
    
    # print(res, lleft, rright)
    if lleft > res:
        res = lleft
    if rright > res:
        res = rright

    return res

if __name__ == '__main__':
    root = newNode(2)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(6)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(11)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)
    print("data is:", get_max(root))