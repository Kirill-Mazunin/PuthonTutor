c = input() .split()
for k in range(len(c)):
    c[k] = int(c[k])
for k in range(1, len(c)):
    if c[k] > c[k-1]:
        print(c[k], end=' ')