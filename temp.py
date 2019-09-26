#输出迷宫的路径
m=4
n=4
flag=[[False for i in range(n)]for j in range(m)]
maze=[[False for i in range(n)] for j in range(m)]
direction=[[1,0],[-1,0],[0,1],[0,-1]]

maze[1][1]=True#障碍物
maze[1][2]=True
maze[1][0]=True
maze[2][2]=True

end=[2,1]
start=[0,0]
minstep=999
path=[]
l=[]
def DFS(x,y,step):
    global minstep
    global path
    global l
    if x==end[0] and y==end[1]:
        if step<minstep:
            minstep=step
            l.append(path.copy())

        return
    for i in range(4):
        nt_x, nt_y = x + direction[i][0], y + direction[i][1]
        if nt_x<0 or nt_x>= m or nt_y<0 or nt_y>=n:

            continue

        if (flag[nt_x][nt_y] is False) and(maze[nt_x][nt_y]is False):
            flag[nt_x][nt_y]=True
            path.append([nt_x,nt_y])
            DFS(nt_x,nt_y,step+1)

            flag[nt_x][nt_y] = False
            path.remove([nt_x,nt_y])

DFS(3,3,0)
# print(l) #输出所有到达出口的所有路径
length=list(map(len,l))
print(l[length.index(min(length))])#输出到达出口的最短路径