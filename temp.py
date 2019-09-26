# 全排列1,2,3,4
# https://www.ucloud.cn/yun/43129.html
N=4
flag=[False for i in range (N)]
st=[0 for  i in range(N)]

def f (node):
    if node ==3:
        print(st)
        return
    for  i in range(N):
        if flag[i] is False:
            flag[i]=True
            st[node]=i
            f(node+1)
            flag[i]=False

f(0)