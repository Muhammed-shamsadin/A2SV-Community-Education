class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = defaultdict(int)
        loser = defaultdict(int)

        for win, lose in matches:
            winner[win] += 1
            loser[lose] += 1
        
        answer = []
        res = []

        for key in winner:
            if key not in loser:
                answer.append(key)
        
        for key, value in loser.items():
            if value == 1:
                res.append(key)

        answer.sort()
        res.sort()

        return [answer, res]
