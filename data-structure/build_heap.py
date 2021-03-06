# python3
from math import floor


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swap_count = 0
    swap_list = []
    size = len(data) - 1
    for i in range(floor(len(data)), -1, -1):
        swap_count, swap_list, data = sift_down(i, size, data, swap_count, swap_list)
    return swap_count, swap_list

def sift_down(i, size, data, swap_count, swap_list):
    minIndex = i
    l = LeftChild(i + 1)
    if l <= size and data[l] < data[minIndex]:
        minIndex = l
    r = RightChild(i + 1)
    if r <= size and data[r] < data[minIndex]:
        minIndex = r
    if i != minIndex:
        data[i], data[minIndex] = data[minIndex], data[i]
        swap_count += 1
        swap_list.append((i, minIndex))
        swap_count, swap_list, data = sift_down(minIndex, size, data, swap_count, swap_list)
    return swap_count, swap_list, data
  
def LeftChild(i):
    return 2 * i - 1
 
def RightChild(i):
    return 2 * i

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swap_count, swap_list = build_heap(data)
    
    print(swap_count)
    for swap in swap_list:
        print(swap[0], swap[1])


if __name__ == "__main__":
    main()
