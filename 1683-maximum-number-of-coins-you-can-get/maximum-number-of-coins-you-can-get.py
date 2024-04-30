'''
Approach: 1. Sort the given piles of coins.
2. Take the last 2 maximum number of coins, that will be for Alice and me
3. The first or 0-indexed coin will be for Bob (which is the minimum number of coin after the array is sorted)
4. the pattern will be clear for us, we start our loop from (length / 3) in which we don't consider the coins that Bob takes
5. Then starting from (length / 3) we collect our coin by jumping 2 times because we will only be 
    adding our coin and not alices.
'''
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        k = len(piles) // 3
        n = len(piles)
        my_coin = 0

        for i in range(k, n, 2):
            my_coin += piles[i]
        
        return my_coin