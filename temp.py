class Solution:
    def jumpFloor(self, number):
        l=[0,1,2,3]
        if number>3:
            for j in range(4,(number+1)):
                l.append(l[j-1]+l[j-2])
        else:
            return l[number]
        return(l[number])
