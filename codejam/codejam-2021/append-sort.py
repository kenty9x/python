#from test import test_random
t = int(input()) 
#t =1
for h in range(1, t+1):
    m = int(input())
    #m=5
    n = [s for s in input().split(" ")]
    #aa = test_random()
    #n = [s for s in aa.split(" ")]
    result = 0
    for i in range(1, m):
        if int(n[i]) > int(n[i-1]): # 10 < 11
            continue
        elif int(n[i]) == int(n[i-1]): #10 = 10
            result += 1
            n[i] += "0"
        else: 
            for j in range(0, len(n[i])):
                if n[i][j] > n[i-1][j]: # 61 > 7
                    tmp = len(n[i-1]) - len(n[i])
                    result += tmp
                    n[i] += "0"*tmp
                    break
                elif n[i][j] == n[i-1][j]:
                    if j != len(n[i]) - 1: 
                        continue
                    else:    # 61 > 6
                        tmp = str(int(n[i-1][j+1:]) + 1)
                        zero = len(n[i-1][j+1:]) - len(tmp)
                        tmp = "0"*zero + tmp
                        result += len(tmp)
                        n[i] += str(tmp)
                        break
                else: # 61 > 60
                    tmp = len(n[i-1]) - len(n[i]) + 1
                    result += tmp
                    n[i] += "0"*tmp
                    break
        print(n)
            
    print("Case #{}: {}".format(h, result))
    