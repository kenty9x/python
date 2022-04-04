t = int(input())
l = [None]*3
for i in range(1, t+1):
    color = [None]*4
    for j in range(3):
        l[j] = [int(s) for s in input().split(" ")]
    for j in range(4):
        color[j] = min(l[0][j], l[1][j], l[2][j])
    sum_color = sum(color)
    if sum_color >= 1000000:
        remain = sum_color - 1000000
        for j in range(4):
            color_reduction = min(remain, color[j])
            color[j] -= color_reduction
            remain -= color_reduction
            if remain == 0:
                break
        print("Case #{}: {} {} {} {}".format(i, *color))
    else:
        print("Case #{}: {}".format(i, "IMPOSSIBLE"))
    