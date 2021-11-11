#import time

def fiblist(n):
    l=[0,1]
    if n<=1:
        return l[n]
    for i in range(2,n+1):
        l.append(l[i-1]+l[i-2])
    return l[n]


if __name__ == "__main__":
    #t0=time.time()
    n=int(input())
    print(fiblist(n))
    #print(time.time()-t0)
    