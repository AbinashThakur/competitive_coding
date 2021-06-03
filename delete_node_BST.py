class newNode:
    def __init__(self, value):
        self.data = value
        self.left = self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
    
def minvaluenode(node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
 
    return current
        
def delete_node_BST(root, key):
 
    if root is None:
        return root
    
    if key < root.data:
        root.left = delete_node_BST(root.left, key)
    
    elif key > root.data:
        root.right = delete_node_BST(root.right, key)
        
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp
            
        temp = minvaluenode(root.right)
        
        root.key = temp.data
        
        root.right = delete_node_BST(root.right, temp.data)
    
    return root

if __name__ == '__main__':
    root = newNode(50)
    root.left = newNode(30)
    root.right = newNode(70)
    root.left.left = newNode(20)
    root.left.right = newNode(40)
    root.right.right = newNode(80)
    root.right.left = newNode(60)
    print("Before Deletion:")
    inorder(root)
    root = delete_node_BST(root, 50)
    print("After Deletion:")
    inorder(root)