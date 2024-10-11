class Solution:
    def balancedString(self, s: str) -> int:
        def isValid():
            for char in changed:
                if changed[char] > window[char]:
                    return False
            return True
        
        counter = Counter(s)
        changed = {}
        limit = len(s) // 4
        length = len(s)
        for char in counter:
            if counter[char] > limit:
                changed[char] = counter[char] - limit
        if not changed:
            return 0
        left = right = 0
        ans = float('inf')
        window = defaultdict(int) 

        while right < length:
            # First
            if s[right] in changed:
                window[s[right]] += 1
            # Second
            while left <= right and isValid():
                ans = min(ans, right - left + 1)
                if s[left] in window:
                    window[s[left]] -= 1
                left += 1

            right += 1
       

        
        return ans if ans != float('inf') else 0