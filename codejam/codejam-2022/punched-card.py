t = int(input())
for i in range(1, t+1):
    n, m = [int(s) for s in input().split(" ")]
    #print("Case #{}: {} {}".format(i, n + m, n * m))
    print("Case #{}:".format(i))
    # First line
    print(".."+"+-"*(m-1)+"+")
    # Second line
    print(".."+"|."*(m-1)+"|")
    for j in range(1, n):
        print("+-"*(m)+"+")
        print("|."*(m)+"|")
    # Last line
    print("+-"*(m)+"+")