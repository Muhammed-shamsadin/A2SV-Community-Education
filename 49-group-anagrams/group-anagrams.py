class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ss = defaultdict(list)

        for i in strs:
            sorted_w = ''.join(sorted(i))
            ss[sorted_w].append(i)

        return list(ss.values())
