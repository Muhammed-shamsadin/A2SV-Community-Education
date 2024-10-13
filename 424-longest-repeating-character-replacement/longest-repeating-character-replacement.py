class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        length = len(s)
        left = max_len = 0

        for right in range(length):
            counter[s[right]] += 1

            while (right - left + 1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len