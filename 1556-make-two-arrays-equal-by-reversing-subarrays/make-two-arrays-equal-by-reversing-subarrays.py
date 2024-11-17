class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freq = Counter(arr)
        for num in target:
            if num not in freq or not freq[num]:
                return False
            freq[num] -= 1
        return True