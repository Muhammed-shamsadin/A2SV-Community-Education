class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        counter = defaultdict(int)

        l, max_len = 0, 0

        for r in range(n):
            counter[s[r]] += 1
            while (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len