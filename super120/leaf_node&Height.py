#leaf node
class node:
    def __init__(self,data):
        self.value=data
        self.right = None
        self.left = None
def leaf(root):
    if root == None:
        return
    if root.left == None and root.right == None:
        print(root.value,end=' ')
    leaf(root.left)
    leaf(root.right)
def Hight(root):
    if root == None:
        return 0
    lh = Hight(root.left)
    rh = Hight(root.right)
    return max(lh,rh)+1
if __name__ == "__main__":
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    
    root.left.left = node(4)
    root.left.right = node(5)
    
    root.right.right = node(7)
    root.right.left = node(6)
    
    root.right.left.right = node(10)
    root.right.left.left = node(9)

    root.right.right.right = node(11)
    
    root.right.left.right.left = node(12)
    root.right.left.right.right = node(13)
    
    leaf(root)
    print('\n',Hight(root))