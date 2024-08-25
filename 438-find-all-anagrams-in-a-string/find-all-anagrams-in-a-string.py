class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        curr_window = Counter(s[:len(p)])
        target_window = Counter(p)
        res = []

        if target_window == curr_window:
            res.append(0)
        left, right = 0, len(p)

        while right < len(s):
            if s[right] in curr_window:
                curr_window[s[right]] += 1
            else:
                curr_window[s[right]] = 1
            curr_window[s[left]] -= 1
            if curr_window[s[left]] == 0:
                del curr_window[s[left]]
            if target_window == curr_window:
                res.append(left + 1)
            left += 1
            right += 1
        return res
        