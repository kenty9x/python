t = int(input()) 
for h in range(1, t+1):
    n = int(input())
    total = 0
    dict_prime = dict()
    result = 0
    for i in range(n):
        m = [int(s) for s in input().split(" ")]
        dict_prime[m[0]] = m[1]
        total += m[0]*m[1]
    half_total = int(total / 2)-10
    for j in range(total, max(2, total -40000), -1):
        tmp = j
        cur = 0
        for k in dict_prime.keys():
            while tmp % k == 0:
                cur += k
                tmp /= k
            if tmp == 1:
                break
        if tmp == 1 and cur + j == total:
            result = j
            break                
   
    print("Case #{}: {}".format(h, result))
    