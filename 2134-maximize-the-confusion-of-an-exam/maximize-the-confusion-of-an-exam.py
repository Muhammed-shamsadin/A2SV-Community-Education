class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        length = len(answerKey)

        max_count = 0
        max_len = 0
        left = 0
        right = 0
        counts = {"T":0, "F":0}

        while right < length:
            counts[answerKey[right]] += 1
            max_count = max(max_count, counts[answerKey[right]])

            if (right - left + 1) - max_count > k:
                counts[answerKey[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

            right += 1

        return max_len

