class newNode:
    def __init__(self, value):
        self.data = value
        self.left = self.right = None
        
def isBST(root, l = None, r = None):
 
    if (root == None) :
        return True
 
    if (l != None and root.data <= l.data) :
        return False

    if (r != None and root.data >= r.data) :
        return False
    
    return isBST(root.left, l, root) and isBST(root.right, root, r)

if __name__ == '__main__':
    root = newNode(50)
    root.left = newNode(20)
    root.right = newNode(70)
    root.left.right = newNode(30)
    root.left.right.left = newNode(25)
    root.left.right.right = newNode(35)
    root.right.right = newNode(80)
    root.right.right.left = newNode(75)
    print(isBST(root))