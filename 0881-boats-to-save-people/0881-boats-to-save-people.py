class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        length =len(people)

        # Step 1: Sort the people into increasing order of there weight.
        people.sort()

        # Step 2: Initialise a Variables for the pointers and to keep count of the boats
        boats = 0
        left = 0
        right = length - 1

        while left <= right:
            if (people[left] + people[right]) <= limit:
                left += 1
            boats += 1
            right -= 1

        return boats                

        # TC: O(N) 
        # SC: O(N)
