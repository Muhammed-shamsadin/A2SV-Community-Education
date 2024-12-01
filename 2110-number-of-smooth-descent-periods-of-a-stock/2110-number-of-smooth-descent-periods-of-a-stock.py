class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        count = 1
        for index in range(1, len(prices)):
            if prices[index-1]-1 == prices[index]:
                count += 1
            else:
                ans += count * ((count+1)/2)
                count = 1
        ans += count * ((count+1)/2)

        return int(ans)



        
        