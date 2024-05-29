from typing import List
from collections import Counter

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n % 2 != 0:
            return -1

        skill_sum = sum(skill)
        if skill_sum % (n // 2) != 0:
            return -1

        target_sum = (skill_sum * 2) // n
        skill_count = Counter(skill)
        result = 0

        for s in skill:
            if skill_count[s] > 0:
                complement = target_sum - s
                if skill_count[complement] > 0:
                    result += s * complement
                    skill_count[s] -= 1
                    skill_count[complement] -= 1
                else:
                    return -1

        return result