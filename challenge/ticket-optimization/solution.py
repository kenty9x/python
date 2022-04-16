# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    d = [0]*len(A)
    if len(A) == 0:
        return 0
    d[0] = 2
    for i in range(1,len(A)):
        op = d[i-1]+2
        for v,p in zip([7,30],[7,25]):
            date_last = A[i]
            last = i - 1
            while last >= 0 and A[last] > date_last - v:
                last -= 1
            if last == -1:
                op = min(op, p)
            else:
                op = min(op, p+d[last])
        d[i] = op
    return d[len(A)-1]

