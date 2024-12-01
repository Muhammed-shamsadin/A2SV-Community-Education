class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # length = len(prices)
        # cnt = length
        # x = 0

        # for i in range(length - 1):
        #     if prices[i] - prices[i + 1] == 1:
        #         x += 1

        # # factorial
        # c = x
        # while x > 0:
        #     c = c + (x - 1)
        #     x -= 1
        # return (cnt + c)


        length = len(prices)
        res, idx = 0, 0

        while idx < length:
            start = idx
            while idx < length - 1 and (prices[idx] - prices[idx + 1]) == 1:
                idx += 1
            c = idx - start + 1
            res += (c * (c + 1)) // 2
            idx += 1
        
        return res
