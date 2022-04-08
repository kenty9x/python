t = int(input())
for i in range(1, t+1):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    a.sort()
    count = 0
    for j in range(n):
        if a[j] > count:
            count += 1
    print("Case #{}: {}".format(i, count))