class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        length = len(fruits)
        left = 0
        total = 0
        res = 0

        for right in range(length):
            count[fruits[right]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[left]
                count[f] -= 1
                total -= 1
                left += 1

                if not count[f]:
                    count.pop(f)
            
            res = max(res, total)
        
        return res