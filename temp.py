import sys
import math
def dis(l1,l2):
  r=list(map(lambda a,b:a-b,l1,l2 ))
  r=[k*k for k in r]
  r=math.sqrt(sum(r))
  return r


def in_list(si):
  tem=[]
  inlist=[[0,0]]
  for i,ss in list(enumerate(si)):
    if i%2==1:
      tem.append(int(ss))
      inlist.append(tem)
      tem=[]
    else:
      tem.append(int(ss))
  return inlist

def sortdis(ordinal,comparelist):
  distance_dic={}
  for comparepoint in comparelist:
    distance_dic[dis(ordinal,comparepoint)]=comparepoint
    test_data_1 = sorted(distance_dic.items(), key=lambda x: x[0],reverse=False)
  return test_data_1


def iterbegin(inputlist,totaldistance ):
  if len(inputlist )>1:
    firstpoint = inputlist[0]
    secondlist = inputlist[1::]
    sortdislist=sortdis(firstpoint,secondlist)
    totaldistance+=sortdislist[0][0]

    secondlist =[item[1] for item in sortdislist[::]]
    return iterbegin(secondlist,totaldistance)
  else:
    return totaldistance+dis(inputlist[0],[0,0])

# print(iterbegin([[0,0],[200, 0], [200, 10], [200, 30], [200, 50], [200, 25]],0))


si=sys.stdin.readlines()
si=si[0].strip().split()

print(int(iterbegin(in_list(si),0)))

# [[200, 0], [200, 10], [200, 30], [200, 50], [200, 25]]
#200 0 200 10 200 30 200 50 200 25
#  456
#两个list减
# l1=[1,5,9]
# l2=[2,4,7]
# print(list(map(lambda a,b:a-b,l1,l2)))
