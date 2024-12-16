class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        # build up the queue
        for i in range(len(tickets)):
            queue.append(i)

        result = 0

        while queue:
            result += 1

            front = queue.popleft()
            tickets[front] -= 1

            # When our index == k and there is no ticket left anymore
            if k == front and tickets[front] == 0:
                return result
            
            if tickets[front] != 0:
                queue.append(front)
            
