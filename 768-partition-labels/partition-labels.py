class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, char in enumerate(s):
            lastIndex[char] = i
        
        res = []
        n = len(s)
        i = 0

        while i < n:
            l = r = i
            while i <= r:
                r = max(r, lastIndex[s[i]])
                i += 1
            res.append(r - l + 1)
            
        return res