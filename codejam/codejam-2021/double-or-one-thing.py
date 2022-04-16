t = int(input())
for j in range(1, t+1):
    a = input()
    re = ""
    count = 0
    last = ""
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            if a[i] > a[i-1]:
                re += a[i-1]*2*(count + 1)
            elif a[i] < a[i-1]:
                re += a[i-1]*(count+1)
            count = 0
        else:
            count += 1
            last = a[i]
    if count == 0:     
        re += a[len(a)-1]
    else:
        re += a[len(a)-1]*(count+1)
    print("Case #{}: {}".format(j, re))