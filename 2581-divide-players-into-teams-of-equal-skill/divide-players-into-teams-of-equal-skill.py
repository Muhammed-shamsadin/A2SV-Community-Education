class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        sum = 0
        l, r = 0, n - 1
        check = skill[0] + skill[-1]

        while l < r:
            k = skill[l] + skill[r]
            if k == check:
                sum += (skill[l] * skill[r])
            else:
                return -1
            l += 1
            r -= 1
        
        return sum