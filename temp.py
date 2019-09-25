# 华为现场写代码
# 广度优先遍历二叉树，找出key所在的层
class node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

n1=node(1)
n2=node(2)
n3=node(3)
n4=node(4)
n5=node(5)
n6=node(6)

n1.right=n2
n1.left=n3
n3.left=n4
n3.right=n5
n2.left=n6


def BFS(node,key):
    queue=[]
    level = 0
    queue.append(node)
    level+=1
    while queue:
        for i in range(len(queue)):
            currentnode=queue.pop(0)
            if(currentnode.value==key):
                print(level)

            if currentnode.left:
                queue.append(currentnode.left)
            if currentnode.right:
                queue.append(currentnode.right)

        level+=1


BFS(n1,6)


def DFS(node):
    stack=[]
    level = 0
    stack.append(node)
    level+=1
    while stack:
        currentnode=stack.pop()
        print(currentnode.value)

        if currentnode.right:
            stack.append(currentnode.right)
        if currentnode.left:
            stack.append(currentnode.left)
DFS(n1)




