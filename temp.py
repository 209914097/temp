import sys
https://www.nowcoder.com/questionTerminal/bf877f837467488692be703735db84e6
s=sys.stdin.readlines()
i=int(s[0].strip().split()[0])
c=int(s[0].strip().split()[1])
w=list(map(int,s[1].strip().split()))
#w=[k  for k in w if k <= c]
# i=3
# c=10
# w=[1,2,4]
def f(w,c):
    if len(w)==0:
        return 1
    elif w[0]<=c:
        return f(w[1:],c)+f(w[1:],c-w[0])
    else:
        return f(w[1:],c)
if (sum(w)<=c):
    result=2**(len(w))
else:
    result=f(w,c)
print(result)
