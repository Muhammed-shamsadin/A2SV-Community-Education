class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        length = len(s)
        pref = [0] * (length + 1)

        for start, end, direction in shifts:
            if direction == 1:
                pref[start] += 1
                pref[end + 1] -= 1
            else:
                pref[start] -= 1
                pref[end + 1] += 1
        
        for i in range(1, length):
            # build the prefix sum
            pref[i] += pref[i - 1]
        
        ans = []
        orderA = ord('a')

        for i, c in enumerate(s):
            curr = (ord(c) - orderA + pref[i]) % 26
            ans.append(chr(curr + orderA))
        
        return ''.join(ans)
