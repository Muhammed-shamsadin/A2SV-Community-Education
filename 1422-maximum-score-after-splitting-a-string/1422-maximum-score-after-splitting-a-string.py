class Solution:
    def maxScore(self, s: str) -> int:
        length = len(s)
        max_score = 0
        for i in range(1, length):
            zeros = s[:i].count('0')
            ones = s[i: ].count('1')

            score = zeros + ones
            max_score = max(max_score, score)
        
        return max_score