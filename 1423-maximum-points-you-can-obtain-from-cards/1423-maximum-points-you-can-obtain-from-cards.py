class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)

        left_sum = sum(cardPoints[:k])
        right_sum = 0
        max_score = left_sum

        

        for index in range(1, k + 1):
            left_sum = left_sum - cardPoints[k - index]
            right_sum = right_sum + cardPoints[-index]

            max_score = max(max_score, left_sum + right_sum)
        
        return max_score