import sys
import math
#http://poj.org/problem?id=1064
#https://blog.csdn.net/ac_gibson/article/details/49121365
s=sys.stdin.readlines()
n1=int(s[0].strip().split()[0])
m=int(s[0].strip().split()[1])
f=s[1].strip().split()
f=list(map(float,f))
sx=max(f)
xx=0
n=1
suma=0
q=0
mx=(sx+xx)/2
while q!=m:
    t=list(map(lambda x:int(x/mx),f))
    suma=sum(t)

    if suma>m:
        xx=mx
        mx=(sx+xx)/2
        suma=0
    if suma<m:
        sx = mx
        mx = (sx + xx) / 2
        suma = 0
    if suma==m:
        break
    if sx==xx:
        break

print('%.2f'%mx)
