class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def step(x):
            step = 0
            while x > 1:
                if x % 2 == 0:
                    x = x / 2
                else:
                    x = 3 * x + 1
                step += 1
            return step
        
        my_dict = {}

        for num in range(lo, hi + 1):
            ans = step(num)
            my_dict[num] = ans
        
        sorted_list = []
        for key, value in my_dict.items():
            sorted_list.append((value, key))
        
        sorted_list.sort()

        return sorted_list[k - 1][1]
