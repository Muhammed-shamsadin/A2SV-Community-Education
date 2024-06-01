class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        p_len = len(players)
        t_len = len(trainers)

        count = 0
        left, right = 0, 0

        while left < p_len and right < t_len:
            if players[left] <= trainers[right]:
                count += 1
                left += 1
                right += 1
            else:
                right += 1
            
        
        return count