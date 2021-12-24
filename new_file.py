def fibo(x):
    if x <= 2:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)


for i in range(1, 20):
    print(fibo(i), end=' ')
