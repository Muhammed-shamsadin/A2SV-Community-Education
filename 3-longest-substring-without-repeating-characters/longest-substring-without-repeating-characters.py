class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        setted = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in setted:
                setted.remove(s[l])
                l += 1
            
            setted.add(s[r])
            res = max(res, r - l + 1)
        
        return res
        