import sys,math
def f(x):
    k=x
    k=(x>0) and (k+f(x-1))
    return k
  
 
print(f(5))
