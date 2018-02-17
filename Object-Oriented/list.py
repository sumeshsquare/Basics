a = range(100000)
b = 3

for i in a:
    for j in a:
        if i + j == b:
            print(i, j)


