import sys
# 参考文献：https://www.jianshu.com/p/a66d5ce49df5?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
# https://blog.csdn.net/baidu_28312631/article/details/47418773
c=4
w=[1, 4, 3, 1]
w=[k  for k in w if k <= c]
v=[1500, 3000, 2000,2000]
maxs=[[0 for indek in range(c+1)] for index in range(len(w))]

for h in range(len(w)):
    for l in range(c+1):
        if h==0:
            maxs[h][l] =0 if w[0]>l else v[h]
        else :
            top=maxs[h-1][l]
            this =top if w[h]>l else max(maxs[h-1][l-w[h]]+v[h],top)
            maxs[h][l]=this
for h in range(len(w)):
    for l in range(c+1):
        print(maxs[h][l],end=' ')
    print('\n')
