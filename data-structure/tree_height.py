# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    sign=[0]*n
    max_height = 0
    for vertex in range(n):
        route = []
        if sign[vertex] != 0:
            max_height = max(max_height, sign[vertex])
        else:
            height = 1
            current = parents[vertex]
            route.append(vertex)
            if current == -1:
                sign[vertex] = 1
            while current != -1:
                if sign[current] == 0:
                    route.append(current)
                    height += 1
                    current = parents[current]
                else:
                    height += sign[current]
                    sign[vertex] = height
                    break
            for j in range(0,len(route)):
                sign[route[j]] = height-j
            max_height = max(max_height, height)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
#    n = 5
#    parents = [4, -1, 4, 1, 1]
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
