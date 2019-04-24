f=[2,[3,4],[5,[5,6]],[2,[3,4],[5,[5,6]]]]
def g(n):
    r=[]
    for item in n:

        if isinstance(item,(int)):
            r.append(item)
        elif isinstance(item,(list)):
            r.extend(g(item))
    return r

print(g(f))# [2, 3, 4, 5, 5, 6, 2, 3, 4, 5, 5, 6]
