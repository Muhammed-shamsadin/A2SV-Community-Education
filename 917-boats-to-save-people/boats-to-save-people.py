class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        length = len(people)
        people.sort()

        left, right = 0, length - 1
        cnt = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            cnt += 1
        return cnt
            