class Solution:
    def similarPairs(self, words: List[str]) -> int:
        frequency = defaultdict(int)
        for word in words:
            setted = tuple(sorted(set(word)))
            frequency[setted] += 1
        answer = 0
        for key, value in frequency.items():
            answer += ((value * (value-1))//2)
        return answer

       
