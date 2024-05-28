class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)

        people.sort()

        left = 0
        right = n - 1
        boat = 0

        while left <= right:
            remain = limit - people[right]
            right -= 1
            boat += 1

            if left <= right and remain >= people[left]:
                left += 1
        
            
        return boat
                
    
        # people.sort()
        
        # left = 0
        # right = len(people) - 1
        # boats = 0

        # while left <= right:
        #     if left == right:  # If only one person left
        #         boats += 1
        #         break
            
        #     if people[left] + people[right] <= limit:
        #         left += 1  # Both can fit on the boat
        #     right -= 1  # Move the heaviest person to the boat
        #     boats += 1
            
        # return boats
