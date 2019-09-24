#  题目描述:
# 
#       在N行M列的棋盘上,初始时棋子位于第x行第y列的方格上，且每个方格上都写有N、S. W. E四个字母中的一个。现在重复执行以下操作，直到棋子走出棋盘:
#       每当棋子到达一个方格(包括初始时棋子所在的方格)时,
#       ①若方格上写有字母N,则擦除方格上的字母,并将棋子向上移动格;②若方格上写有字母S ,则擦除方格上的字母，并将棋子向下移动格;③若方格上写有字母W，则擦除方格上的字母,并将棋子向左移动一格;④若方格上写有字母E ,则擦除方格上的字母, 并将棋子向右移动格;⑤若方格上的字母已被擦除，则将棋子沿着京先的方向再移动格。那么棋子总共移动了多少格才走出棋盘?
# 输入:
#       第一行输入两个整数N和M，1<=N，M<=2000。
#       接下来N行,第i行输入一个长度为M且只包含字母N S. W. E的字符串,其中第j个字母即为棋盘第行第j列的方格上写的字母
#       最后一行输入两个整数x和y，表示棋子的初始位置，1≤x≤N, 1≤y≤M。
# 
# 输出
#       输出棋子移动的格子数。
# 
# 样例输入
# 
#       2 2
#       SW
#       EN
#       2 1
# 样例输出 5
#       样例解释
# 
#       棋子先向右移动1格，再向上移动1格,接着向左移动1格,最后向下移动2格,总共移动了5格。

# N,M=map(int,input().split(' '))
# for i in range(N):
#     l=input()
# X,Y=map(int,input().split(' '))

N,M=3,3
mapp=[['E', 'E','S'],
      ['N','S','S'],
      ['N','W','S']]
X,Y=2,2
x=X-1
y=Y-1

# currentx=X
# currenty=Y
tem=''
step=0
try:
    while 0<(x+1)<(N+1) and 0<(x+1)<(M+1):
        if mapp[x][y]== 'E':
            mapp[x][y] = 'b'
            y += 1
            step += 1
            tem='E'


        elif mapp[x][y]== 'W':
            mapp[x][y] = 'b'
            y -= 1
            step += 1
            tem = 'W'

        elif mapp[x][y]== 'S':
            mapp[x][y] = 'b'
            x += 1
            step += 1
            tem = 'S'

        elif mapp[x][y]== 'N':
            mapp[x][y] = 'b'
            x -= 1
            step += 1
            tem = 'N'

        elif mapp[x][y]== 'b':

            if tem == 'E':
                y += 1
                step += 1
                if mapp[x][y]!= 'b':tem =  mapp[x][y]



            elif tem == 'W':
                y -= 1
                step += 1
                if mapp[x][y] != 'b': tem = mapp[x][y]

            elif tem == 'S':
                x += 1
                step += 1
                if mapp[x][y] != 'b': tem = mapp[x][y]

            elif tem == 'N':
                x -= 1
                step += 1
                if mapp[x][y] != 'b': tem = mapp[x][y]

    print(step)
except:
    print(step)