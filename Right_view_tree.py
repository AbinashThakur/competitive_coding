class newNode:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0

def printRightView(root):

    if (not root):
        return

    q = []
    q.append(root)
    
    while (len(q)):

        n = len(q)

        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)

            if (i == 1):
                print(temp.data, end=" ")

            if (temp.left != None):
                q.append(temp.left)

            if (temp.right != None)
                q.append(temp.right)


if __name__ == '__main__':

    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    printRightView(root)