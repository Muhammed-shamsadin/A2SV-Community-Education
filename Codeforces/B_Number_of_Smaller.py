n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

answer = []
left = right = 0

while left < n and right < m:
    if b[right] > a[left]:
        left += 1
    else:
        answer.append(left)
        right += 1

diff = len(b)  - len(answer)
answer.extend(diff * [n])

print(*answer)







# for up in range(n):
#     if b[down] > a[up]:
#         count += 1
#     down += 1
#     q.append(count)
# print(*q)    
