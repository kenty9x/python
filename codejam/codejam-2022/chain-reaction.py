class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.parent = None  # Initialize next as null
        self.children = []

def max_data(node):
    count_total = 0
    children = node.children # 2 -> 7; 5 -> 1,2
    count_min = 0
    data_min = 0
    if len(children) > 0:
        count_min = max_data(children[0])
        data_min = children[0].data
        for i in range(1,len(children)):
            count_temp = max_data(children[i])
            data_temp = children[i].data
            if data_temp > data_min:
                count_total += count_temp
            else:
                count_total += count_min
                count_min = count_temp
                data_min = data_temp
    else:
        return node.data
    if data_min > node.data:
        node.data = data_min
        count_total += count_min
    else:
        count_total = count_total + node.data + count_min - data_min
    return count_total

t = int(input())
for i in range(1, t+1):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    b = [int(s) for s in input().split(" ")]
    c = [Node(0) for i in range(n)]
    v = [None]*n
    initiator = []
    total = 0
    q = []
    for j in range(n):
        c[j].data = a[j]
        if b[j] == 0:
            initiator.append(c[j])
        else:
            c[b[j]-1].children.append(c[j])

    for j in range(len(initiator)):
        total += max_data(initiator[j])

    print("Case #{}: {}".format(i, total))