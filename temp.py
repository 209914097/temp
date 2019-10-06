#广度优先搜索走迷宫
def f():
    m,n=5,4
    direction=[[0, -1],[0, 1], [-1, 0], [1, 0] ]

    maze=[[False for j in range(n)]for i in range(m)]
    flag=[[False for j in range(n)]for i in range(m)]
    maze[0][2]=True
    maze[2][2]=True
    maze[3][1]=True
    maze[4][3]=True
    maze[3][0] = True

    endx,endy=4,2

    x,y,s=0,0,0
    flag[0][0]=True
    queue=[[0,0,0]]
    head=0
    index=1
    path=[]

    while head<index:

        for i in range(4):
            nx=queue[head][0]+direction[i][0]
            ny=queue[head][1]+direction[i][1]
            s =queue[head][2] +1
            if nx==endx and ny==endy:

                return queue,s

            if nx >=m or ny>=n or  nx<0 or ny<0 :
                continue
            if flag[nx][ny] is True or maze[nx][ny] is True:
                continue
            if flag[nx][ny] is False and maze[nx][ny] is False:
                flag[nx][ny]=True
                queue.append([nx,ny,s])
                index+=1
        head+=1




ans,ss=f()

ss-=1
short=[]

tem=list(filter(lambda nod:nod[2]==ss,ans))[-1]
short.append(tem)
while ss:
    temp = list(filter(lambda nod: nod[2] == ss, ans))
    for nod in temp:
        if (abs(nod[0]-tem[0])+abs(nod[1]-tem[1]))==1:
            tem=nod
            short.append(tem)

    ss-=1
short.reverse()
print(short)
