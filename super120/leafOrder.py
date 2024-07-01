#lefe order
class node:
    def __init__(self,data):
        self.value=data
        self.right = None
        self.left = None
def levelorder(root):
    q = [root]
    q.append(None)
    while len(q)>0:
        curr = q.pop(0)
        if curr == None:
            if len(q) == 0:
                break
            else:
                print()
                q.append(None)
        else:
            print(curr.value,end=' ')
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
            
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
    root.right.left.right.left = node(12)
    root.right.left.right.right = node(13)
    root.right.right.right = node(11)
    
    
    levelorder(root)
    