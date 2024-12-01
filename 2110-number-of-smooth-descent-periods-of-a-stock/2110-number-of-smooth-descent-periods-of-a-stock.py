class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        length = len(prices)
        count = 1
        ans = 0

        for i in range(length - 1):
            if prices[i+1] - prices[i] == -1:
                count += 1
            else:
                ans += count * ((count + 1)// 2)
                count = 1
        ans += count * ((count + 1)// 2)

        return ans
