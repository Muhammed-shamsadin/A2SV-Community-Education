n, k = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

nums.sort()

x = nums[k - 1]
if k == 0:
    if nums[0] - 1 > 0:
        print(nums[k] - 1)
    else:
        print(-1)

elif k < n and nums[k] == x:
    print(-1)

else:
    print(x)
