# Given an interger N, returns the smallest integer greater than N,
# the sum of whose digits is twice as big as the sum of digits of N

def solution(N):
    sum = 0
    tmp = N
    twice_sum_N = 0
    while tmp >0:
        sum += tmp % 10
        tmp //= 10
    count = 0
    while N > 0:
        if sum >= 9-(N%10):
            twice_sum_N += 9*pow(10,count)
            sum -= 9-(N%10)
        else:
            twice_sum_N += ((N%10) + sum)*pow(10,count)
            sum = 0
        N //= 10
        count += 1
        if sum == 0:
            return twice_sum_N + pow(10,count)*N
    while sum > 0:
        if sum > 9:
            twice_sum_N += 9*pow(10,count)
            sum -= 9
        else:
            twice_sum_N += sum*pow(10,count)
            sum = 0
        count += 1
    return twice_sum_N
    pass

print(solution(11))
