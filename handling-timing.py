import time
b = 44
def method2(a):
    start = time.time()
    a = list(a)
    i = 0
    j = len(a)  -1
    while True:
        if i == j:
            break
        out = a[i] + a[j]
        if out == b:
            print(i, j)
            i += 1
        elif out > b:
            j -= 1
        else:
            i += 1
    print(time.time() - start)


method2(range(1000))