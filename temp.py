# 编程题| 20分
# 
#       队尾幸运编号
# 
#       时间限制: C/C+ +语言1000MS ;其他语言3000MS内存限制: C/C++语言65536KB ;其他语言589824KB题目描述:
# 
#       N个人排成-队，从1到5轮流报数,报5的人是幸运者，出列。
# 报到队尾后，从队首接着报。依此循环。问:排在队尾的人是第几名幸运者?注: N为小于100000的正整数。例:
#       1人排成一队,他就是第1名幸运者。
#       3人排成一一队，队尾是第2名幸运者。
#       5人排成一队， 队尾是第1名幸运者。
#       8人排成一一队，队尾是第3名幸运者
#       即求: N人排成一队，队尾是第多少名幸运者?
# 输入
#       队伍总人数
# 输出
#       队尾者的幸运编号 
# 样例输入
#       20 
# 样例输出
#       4

def f(l,end):
    ans=0
    N = len(l)
    while N>=5:
        if l[4]==end:
            ans += 1
            return ans
        else:
            l.remove(l[4])
            ans+=1
            N=len(l)
            one=l[4::]
            two=l[0:4]
            one.extend(two)
            l=one
    if (N<5):
        mvindex=5%N-1
        while l[mvindex] != end:
            if(l[mvindex]==end):
                ans += 1
                return ans
            else:
                l.remove(l[mvindex])
                ans += 1
                one = l[mvindex::]
                two = l[0:mvindex]
                one.extend(two)
                l = one
                N = len(l)
                mvindex = 5 % N - 1

        ans += 1
    return ans

# ss=int(input())
ss =8
l=[i for i in range (1,ss+1)]


print(f(l,l[-1]))
