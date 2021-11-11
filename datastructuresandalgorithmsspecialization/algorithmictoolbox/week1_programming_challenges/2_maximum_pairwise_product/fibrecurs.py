import time

def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    t0=time.time()
    n=int(input())
    print(fib(n))
    print(time.time() - t0)
    