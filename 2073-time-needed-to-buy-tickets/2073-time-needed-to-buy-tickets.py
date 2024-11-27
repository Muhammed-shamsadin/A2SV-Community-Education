class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        for i in range(len(tickets)):
            queue.append([i, tickets[i]])
        
        ans = 0
        while queue:
            ans += 1
            index, ticket = queue.popleft()
            if ticket - 1 > 0:
                queue.append([index, ticket-1])
            elif index == k:
                return ans
