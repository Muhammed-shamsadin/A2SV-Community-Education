class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        
        k = 0
        res = ''

        for i in range(len(s)):
            if k < len(spaces) and i == spaces[k]:
                res += " "
                k += 1
            res += s[i]
        return res
        