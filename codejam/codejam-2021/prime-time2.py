# from memory_profiler import profile

#@profile
def solve(val, d, tot, half, j):
    r = 0
    if tot < half:
        return r
    for i in d.keys():
        if d[i] == 0:
            continue 
        if i < j:
            break
        n1 = val*i
        n2 = d.copy()
        n2[i] -= 1
        n3 = tot - i
        if n1 == n3:
            return max(r, n1)
        if tot < half:
            return r
        
        r = max(r, solve(n1, n2, n3, half, j))
    return r

    
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
    half_total = total / 2.0
    for j in dict_prime.keys():
        temp = dict_prime.copy()
        temp[j] -= 1
        
        if j == total-j:
            result = max(j, result)
        result = max(result, solve(j, temp, total-j, half_total, j))
   
    print("Case #{}: {}".format(h, result))
    