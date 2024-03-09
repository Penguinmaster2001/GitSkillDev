
n0 = int(input("n0: "))
n1 = int(input("n1: "))
n  = int(input("n: "))

smallest = min(abs(n0), abs(n1))

memoiry = { }

def fib(n, depth):
    if depth == 0:
        return n;
    if depth in memoiry:
        return memoiry[depth]
    if abs(n) <= smallest:
        return n
    else:
        memoiry[depth] = fib(n - 1, depth - 1) + fib(n - 2, depth - 1)
        return memoiry[depth]
    

print(fib(n1, n))
