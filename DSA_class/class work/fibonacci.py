def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibo_eff(n):
    fib = [0]*(n+1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2,n+1):
        fib[i] = fib[i-2] + fib[i-1]
    return fib[n]

print(fibo_eff(10))
