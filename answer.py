import sys
import random
a = [1, 2, 3, 4, 5]
#random.shuffle(a)
#print(a)
def myshuffle():
    b=a.copy()
    for ii in range(0, len(b)):
        index = random.randint(0, len(b)-1)
        tem1=b[ii]
        tem2=b[index]
        b[ii]=tem2
        b[index]=tem1
    return b

def sub(a,b):
    sublist=[]
    for i in range(len(a)):
        sublist.append(a[i]-b[i])
    # for i in range(len(sublist)):
    if 0 in sublist:return False
    else:return True
if __name__=="__main__":
    result=myshuffle()
    while(not sub(result,a)):
        result=myshuffle()

    print(a)
    print(result)

