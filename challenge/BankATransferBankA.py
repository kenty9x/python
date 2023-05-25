# You are given a list of N transfers (numbered from 0 to N-1)  between two banks: bank A and bank B.
# The K-th transfer is described by two values.
# The banks do not want to go into debt (in other words, their account balance may not drop bewlow 0)

def solution(R, V):
    sum_A = sum_B = 0
    initial_A = initial_B = 0
    for i in range(len(R)):
        if R[i] == 'A':
            sum_A += V[i]
            if sum_B - V[i] < 0:
                initial_B += V[i] - sum_B
                sum_B = 0
            else: 
                sum_B -= V[i]
        else:
            sum_B += V[i]
            if sum_A - V[i] < 0:
                initial_A += V[i] - sum_A
                sum_A = 0
            else: 
                sum_A -= V[i]
    return [initial_A, initial_B]
    pass
