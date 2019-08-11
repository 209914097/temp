# 给定两个正数N和S找出所有的长度为N的正整数数列中，满足单调递增和总和为S的数列
#输入：共一行，两个数N和S
#输出：满足条件的所有队列
#输入：3 10
#输出：
#[1, 2, 7]
#[1, 3, 6]
#[1, 4, 5]
#[2, 3, 5]
import sys
# ss = input()
# N =int( ss.split(' ')[0]);
# S = int(ss.split(' ')[1]);
N =3;
S =10;
#
# print(S)
# print(N)
re=[]
length =N
def list_add(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c
def ff(num,N,j):
    result=[]
    for i in range(N-num):
        result.append(0)
    for i in range(num):
        result.append(j)

    return result

def f(num,N,S,j):
    global re
    global base

    if re==[]:
        re=[base for i in range (N)]
        num=num-1

    if num>1:
        re=list_add(re,ff(num,N,j))
        if sum(re)<10:
            num=num-1
            f(num,N,S,j)
        else:
            return
    else:
        err=(S-sum(re))
        if err>=0:
            j=j+1
            re=list_add(re,ff(1,N,err))
            print(re)
            re=[]
            f(N, N, S, j)
        else:
            return


for b in range(1,int(S/N)):
    base=b
    re = []
    f(3,3,10,1)
