from queue import Queue
t = int(input()) 
for h in range(1, t+1):
    n = int(input())
    total = 0
    dict_prime = dict()
    q = Queue(maxsize=0)
    result = 0
    for i in range(n):
        m = [int(s) for s in input().split(" ")]
        dict_prime[m[0]] = m[1]
        total += m[0]*m[1]
    half_total = total / 2.0
    
    #Start queue
    for j in dict_prime.keys():
        temp = dict_prime.copy()
        temp[j] -= 1
        if j == total-j:
            result = max(j, result)
        q.put([j,temp,total-j])
    while(not q.empty()):
        tmp = q.get()
        if tmp[0] == tmp[2]:
            result = max(result, tmp[0])
        for i in tmp[1].keys():
            if tmp[1][i] == 0:
                continue
            n2 = tmp[1].copy()
            n1 = tmp[0]*i
            n3 = tmp[2] - i
            n2[i] -= 1
            if (total-n3) <= half_total:
                q.put([n1,n2,n3])
            del n2
        del tmp[1]
        del tmp
            
        if n1 == n3:
            result = max(result, n1)
   
    print("Case #{}: {}".format(h, result))
    