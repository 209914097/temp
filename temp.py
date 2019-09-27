# 树的前中后序遍历
class node():
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
        


def f(node):
    global path

    if node is None :return


    f(node.left)
    
    f(node.right)
    path.append(node.value)


n1=node(1)
n2=node(2)
n3=node(3)
n4=node(4)
n5=node(5)

n1.left=n2
n1.right=n5
n2.right=n3
n2.left=n4
path=[]
l=[]
f(n1)

print(path)

