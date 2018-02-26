import time
b = 23
def method2(a):
    start = time.time()
    a = list(a)
    i = 0
    j = len(a)  -1
    print(j)
    while True:
        if i == j:
            print('Breakkkkkkkkkk')
            break
        out = a[i] + a[j]
        print ('prrr:' +str(out))
        if out == b:
            print(i, j)
            i += 1
        elif out > b:
            j -= 1
            print('greater')
        else:
            i += 1
            print('Elseeeee')
    print(time.time() - start)


method2(range(100))
