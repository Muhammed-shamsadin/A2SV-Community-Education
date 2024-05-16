class Solution:
    def similarPairs(self, words: List[str]) -> int:
        frequency = defaultdict(int)
        for word in words:
            setted = tuple(sorted(set(word)))
            frequency[setted] += 1
        
        ans = 0
        for key, values in frequency.items():
            ans += ((values * (values - 1)) // 2)

        return ans






















        freq = defaultdict(int)
        


       
