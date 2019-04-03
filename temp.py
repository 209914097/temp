import sys
import math
s=sys.stdin.readlines()
i=int(s[0].strip())
ss=s[1::]
for slist in ss:
    numlist=list(map(int,slist.strip().split(' ')))
    first=numlist[0]
    second=numlist[1]
    third=numlist[2]
    four=numlist[3]
    ans=four+math.floor(second/2)+min(first,third)
    second = second-2*math.floor(second/2)
    third =third -min(first,third)
    first = first-min(first,third)

    if second>0 and first>=2:
        ans+=second
        first=first-second*2
    ans +=math.floor(first/4)
    print(ans)

"""
第一行T表示组数，接下来T行，每行四个非负整数A,B,C,D
input:
4
1 2 3 4
4 3 2 1
2 2 2 1
0 2 0 1

ouput:
共T行，每行输出一个队伍数
6
5
4
2
"""

