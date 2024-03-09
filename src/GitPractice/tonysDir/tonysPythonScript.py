
n0 = int(input("n0: "))
n1 = int(input("n1: "))
n  = int(input("n: "))

memoiry = { }

def fib(n):
    if n in memoiry:
        return memoiry[n]
    if n <= 1:
        return n
    else:
        memoiry[n] = fib(n - 1) + fib(n - 2)
        return memoiry[n]
    

print(fib(n))
