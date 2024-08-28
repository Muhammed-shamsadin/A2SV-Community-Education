class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        length = len(blocks)

        left, right = 0, k - 1
        count_white = blocks[:k].count("W")
        min_operations = count_white

        while right < length - 1:
            right += 1
            left += 1
            if blocks[right] == 'W':
                count_white += 1
            if blocks[left - 1] == "W":
                count_white -= 1
            min_operations = min(min_operations, count_white)
        
        #TC: O(N)
        #SC: O(1)
        
            
        return min_operations
