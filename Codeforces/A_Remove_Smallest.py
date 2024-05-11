def solve():
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    count = 1
    i, j = 0, 1

    while j < n:
        if arr[j] - arr[i] > 1:
            count += 1 

        i += 1
        j += 1
    if count > 1:
        print("NO")
    else:
        print("YES")

t = int(input())
for _ in range(t):
    solve()

