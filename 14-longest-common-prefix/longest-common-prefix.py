class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        miniString, maxString = min(strs), max(strs)

        for i  in range(len(miniString)):
            if miniString[i] != maxString[i]:
                return miniString[:i]
        return miniString